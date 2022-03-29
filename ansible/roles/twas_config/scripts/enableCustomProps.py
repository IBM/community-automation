#--------------------------------------------------------------------
# WebSphere Penetration testing custom props
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f pentest_custom.py
#--------------------------------------------------------------------
# 
execfile('wsadminlib.py')

print "Starting enable Pen test custom props script..."

#--------------------------------------------------------------------
# candidate to add to -> https://github.com/wsadminlib/wsadminlib/blob/master/bin/wsadminlib.py
def setapiDiscovery( nodename, servername, apiDiscovery, ):
    """Sets whether to use the apiDiscovery"""
    m = "setapiDiscovery:"
    #sop(m,"Entry. Sets whether to use the setapiDiscovery. nodename=%s servername=%s setapiDiscovery=%s" % ( repr(nodename), repr(servername), repr(setapiDiscovery) ))
    server_id = getServerByNodeAndName( nodename, servername )
    #sop(m,"server_id=%s " % ( repr(server_id), ))
    webcontainer = AdminConfig.list('WebContainer', server_id)
    #sop(m,"webcontainer=%s " % ( repr(webcontainer), ))
    result = AdminConfig.modify(webcontainer, [['setapiDiscovery', setapiDiscovery]])
    #sop(m,"Exit. result=%s" % ( repr(result), ))

cellName = AdminControl.getCell()
# get the list of servers and loop on every one minus webservers
for (nodename,servername) in listServersOfType(None):
    stype = getServerType(nodename,servername)
    # sometimes, dmgr has no type... who knows why
    if stype == 'APPLICATION_SERVER':
        # hard coded for Pentest setup https://ibm.ent.box.com/notes/846078834982
        setWebContainerCustomProperty(nodename,servername,'com.ibm.ws.webcontainer.addStrictTransportSecurityHeader','max-age=31536000; includeSubDomains')
        setWebContainerCustomProperty(nodename,servername,'com.ibm.ws.webcontainer.disablexPoweredBy','true')
        setWebContainerCustomProperty(nodename,servername,'trusthostheaderport','true')
        setWebContainerCustomProperty(nodename,servername,'com.ibm.ws.webcontainer.extractHostHeaderPort','true')
        setapiDiscovery( nodename, servername, 'true', )

# singleSignOn SSL very close to what is needed
#https://github.com/wsadminlib/wsadminlib/blob/c3913bac556094989ac5de40afbee772858f806c/bin/wsadminlib.py#L6880

#endfor
print "--Saving...."
AdminConfig.save()
print "--completed..."

