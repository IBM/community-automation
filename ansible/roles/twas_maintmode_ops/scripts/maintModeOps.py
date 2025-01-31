#--------------------------------------------------------------------
# WebSphere Maint Mode enablement
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f enableMaintMode.py < nodename > < mode >
# 2017-03-10 schader@us.ibm.com initial version
#--------------------------------------------------------------------
#
#    false: This value disables the maintenance mode.
#    break: This value stops any traffic from being routed to the server.
#    affinity: Default value. This value routes only traffic with affinity to the server.
#    stop: This value stops the server, and persistently sets it in break mode.
#

def printUsageAndExit (  ):
        print ("")
        print ("Usage: wsadmin -f enableMaintMode.py [nodeName] [ mode ] ")
        print ("")
        sys.exit()
#endDef 
#---------------------------------------------------------------------
#  Parse Command Line
#---------------------------------------------------------------------

if (len(sys.argv) == 2):
        arg_nodeName = sys.argv[0]
        arg_mode = sys.argv[1]
else:
	 printUsageAndExit( )
#endElse 

execfile('wsadminlib.py')

print ("Starting script maint mode...")

#--------------------------------------------------------------------
#cellName = AdminControl.getCell()
#productVersion=AdminTask.getNodeBaseProductVersion(['-nodeName', 'dmgr'])
#print "modifying WAS version: " + productVersion

# get the list of servers and loop on every one minus webservers
for (nodename,servername) in listServersOfType(None):
    if arg_nodeName == nodename:
        stype = getServerType(nodename,servername)
        # sometimes, dmgr has no type... who knows why
        if stype == 'APPLICATION_SERVER' or stype == 'PROXY_SERVER' or stype == 'ONDEMAND_ROUTER':
            print ("-- maint mode op" + arg_mode +" for node: " + nodename + " server:" + servername)
            AdminTask.setMaintenanceMode (nodename,['-name',servername,'-mode',arg_mode])
        #endif
    #endif
#endfor
AdminConfig.save()
print ("--completed...")
