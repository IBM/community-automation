#--------------------------------------------------------------------
# WebSphere HEPL enablement
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f enableHPEL.py
# 2016-01-19 schader@us.ibm.com initial version
#--------------------------------------------------------------------
# 
execfile('wsadminlib.py')

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
