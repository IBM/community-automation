#!/usr/bin/python3
#######################################################################
# Author: schader@us.ibm.com 2014
#
# THIS WORKS For *nix db2 hosts
#
# FUNCTION: purge the existing daytrader SIB tables and schema
#
# HOWTO:
# AutoWAS batch:
# dbms put DayTrader_dropsib.py DayTrader_dropsib.py
# dbms runNoRC Trader_dropsib.py < dbname > 
#
######################################################################
import os
import shutil
import sys 
from  stat import *
from subprocess import call

# argv[0] = this file
if len(sys.argv) != 2:  # the program name and one argument
                        # stop the program and print an error message
    sys.exit("{ERROR} dbname argument missing.")

dbname = sys.argv[1]

# look for this schema IBMME
findme = 'IBMME'
findme2 = 'IBMWSSIB'
fileName1 = '/tmp/db2tablelist.txt'
fileName2 = '/tmp/db2IBMMEtablelist.ddl'

f1 = open(fileName1, "w")

call(["db2start"])
call(["db2", "connect to "+dbname])
rc = call(["db2", "list tables for all"], stdin=None, stdout=f1, stderr=None)
f1.flush()
f1.close()

f1 = open(fileName1, "r")
f2 = open(fileName2, "w")
# sample line
# table                          schema
#SIB000                          IBMME0          T     2014-02-10-10.43.22.871391
lines = f1.readlines()
for line in lines:
	if ( -1 != line.find(findme)):
		# find the first white space , this will provide the table name
		table = line[0:line.find(' ')]
		# schema names are 8chars or less
		schema = (line[line.find(findme):line.find(findme)+8]).rstrip()
		# drop table IBMME0.SIB000;
		f2.write("drop table "+schema+"."+table+"\n")
	if ( -1 != line.find(findme2)):
		# find the first white space , this will provide the table name
		table = line[0:line.find(' ')]
		# schema names are 8chars or less
		schema = (line[line.find(findme2):line.find(findme2)+8]).rstrip()
		# drop table IBMWSSIB.SIB000;
		f2.write("drop table "+schema+"."+table+"\n")

#endfor
f2.flush()
f2.close()
call(["chmod","777",fileName1])
call(["chmod","777",fileName2])

print ("-- start purge the IBMME SIB tables from database:"+dbname)

tmpFile='/tmp/db2IBMMEtablelist.out'

f1 = open(tmpFile,"w")
rc = call(["db2","-f",fileName2 ], stdin=None, stdout=f1, stderr=None)
print ("-- purge results -> "+tmpFile)
f1.flush()
f1.close()
call(["chmod","777",tmpFile])

print ("-- completed purge the IBMME SIB tables from database:"+dbname)
call(["db2", "terminate"])
