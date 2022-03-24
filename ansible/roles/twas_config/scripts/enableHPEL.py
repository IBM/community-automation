#--------------------------------------------------------------------
# WebSphere HEPL enablement
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f enableHPEL.py
# 2016-01-19 schader@us.ibm.com initial version
#--------------------------------------------------------------------

### need the wsaminlib.py from autowas in the current directory
### < autowas root dir>/data/wsadminlib.py
### using autowas batch file you can run all of this from autowas box
### assuming your autwas dir is in /opt/automation2/autowas
### create a batch file with this in it:
# START OF THE BATCH FILE - Do not include the # or this line
# dmgr start
# dmgr put /opt/automation2/autowas/data/wsadminlib.py bin/wsadminlib.py
# dmgr put enableHPEL.py bin/enableHPEL.py
# dmgr run bin/wsadmin{EXT} -username user1 -password security -lang jython -f bin/enableHPEL.py
# // optional run the sync node - this will stop all nodeagents and servers
# // sync_node dmgr
# END OF THE BATCH FILE - Do not include this line

#### NOW RUN THIS:
# run this command: cfg -cfg < your config file > batch enableHPEL.batch
#


execfile('bin/wsadminlib.py')

print "Starting script..."

#--------------------------------------------------------------------
cellName = AdminControl.getCell()
# enable the HPEL requirement for every SSL config in the env... UGH>
#productVersion=AdminTask.getNodeBaseProductVersion(['-nodeName', 'dmgr'])
#print "modifying WAS version: " + productVersion

# get the list of servers and loop on every one minus webservers
for (nodename,servername) in listServersOfType(None):
    stype = getServerType(nodename,servername)
    # sometimes, dmgr has no type... who knows why
    if stype == 'DEPLOYMENT_MANAGER' or stype == 'NODE_AGENT' or stype == 'APPLICATION_SERVER' or stype == 'PROXY_SERVER' or stype == 'ONDEMAND_ROUTER':
        print "-- Enabling HPEL for node: " + nodename + " server:" + servername
        parm1="/Cell:"+cellName+"/Node:"+nodename+"/Server:"+servername+"/HighPerformanceExtensibleLogging:/"
        HPELService = AdminConfig.getid(parm1)
        AdminConfig.modify(HPELService, "[[enable true]]")
        HPELLog = AdminConfig.list("HPELLog", HPELService)
        AdminConfig.modify(HPELLog, "[[purgeMaxSize 10000] [fileSwitchTime 01] [fileSwitchEnabled true]]")
        HPELTrace = AdminConfig.list("HPELTrace", HPELService)
        AdminConfig.modify(HPELTrace, "[[purgeMaxSize 10000] [fileSwitchTime 02] [fileSwitchEnabled true]]")
        HPELTextLog = AdminConfig.list("HPELTextLog", HPELService)
        AdminConfig.modify(HPELTextLog,"[[enabled false]]")

        
        parm2="/Cell:"+cellName+"/Node:"+nodename+"/Server:"+servername+"/RASLoggingService:/"
        RASLogging = AdminConfig.getid(parm2)
        AdminConfig.modify(RASLogging, "[[enable false]]")

	#endif
#endfor
print "--Saving...."
AdminConfig.save()
print "--completed..."
