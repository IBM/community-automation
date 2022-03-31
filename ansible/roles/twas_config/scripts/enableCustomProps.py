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
def modifyCookiesSessionName(nodename,servername,enabled,sessionname):
    server_id = getServerByNodeAndName(nodename,servername)
    sessionmanager = AdminConfig.list('SessionManager', server_id)
    AdminConfig.modify(sessionmanager, [['enableCookies',enabled]])
    cookie_id = AdminConfig.list('Cookie',sessionmanager)
    AdminConfig.modify(cookie_id,[['name', sessionname]])

def setapiDiscovery( nodename, servername, apiDiscovery, ):
    """Sets whether to use the apiDiscovery"""
    m = "setapiDiscovery:"
    #sop(m,"Entry. Sets whether to use the setapiDiscovery. nodename=%s servername=%s setapiDiscovery=%s" % ( repr(nodename), repr(servername), repr(setapiDiscovery) ))
    server_id = getServerByNodeAndName( nodename, servername )
    #sop(m,"server_id=%s " % ( repr(server_id), ))
    webcontainer = AdminConfig.list('WebContainer', server_id)
    #sop(m,"webcontainer=%s " % ( repr(webcontainer), ))
    result = AdminConfig.modify(webcontainer, [['apiDiscovery', apiDiscovery]])
    #sop(m,"Exit. result=%s" % ( repr(result), ))

def ssossl():
    ltpaId = _getLTPAId()
    attrs1 = [["singleSignon", [["requiresSSL", "true"], ["enabled", "true"]]]]

    if len(ltpaId) > 0:
        try:
            AdminConfig.modify(ltpaId, attrs1)
        except:
            print "AdminConfig.modify(%s,%s) caught an exception" % (ltpaId,repr(attrs1))
            raise
    else:
        raise "SSO configId was not found"
    return

cellName = AdminControl.getCell()
# get the list of servers and loop on every one minus webservers
for (nodename,servername) in listServersOfType(None):
    stype = getServerType(nodename,servername)
    # sometimes, dmgr has no type... who knows why
    if stype == 'APPLICATION_SERVER':
        # hard coded for Pentest setup https://ibm.ent.box.com/notes/846078834982
        print("-- setting custom prop: com.ibm.ws.webcontainer.addStrictTransportSecurityHeader")
        setWebContainerCustomProperty(nodename,servername,'com.ibm.ws.webcontainer.addStrictTransportSecurityHeader','max-age=31536000; includeSubDomains')
        print("-- setting custom prop: com.ibm.ws.webcontainer.disablexPoweredBy")
        setWebContainerCustomProperty(nodename,servername,'com.ibm.ws.webcontainer.disablexPoweredBy','true')
        print("-- setting custom prop: trusthostheaderport")
        setWebContainerCustomProperty(nodename,servername,'trusthostheaderport','true')
        print("-- setting custom prop: com.ibm.ws.webcontainer.extractHostHeaderPort")
        setWebContainerCustomProperty(nodename,servername,'com.ibm.ws.webcontainer.extractHostHeaderPort','true')
        print("-- setting custom prop: apiDiscovery")
        setapiDiscovery( nodename, servername, 'true', )
        print("-- setting CookieName: PTSESSIONID")
        modifyCookiesSessionName( nodename, servername, 'true', 'PTSESSIONID' )
        print("-- set single signon ssl: true")
        ssossl()
        print("-- set JVM initial heap: 50")
        setJvmProperty(nodename,servername,'initialHeapSize','50')
        print("-- set JVM Max heap: 1024")
        setJvmProperty(nodename,servername,'maximumHeapSize','1024')
        # example to add port
        # ensureHostAlias( 'default_host', '*', '9080' )
        DEBUG_SOP=1
        getHostAliasID( 'admin_host', '*', '9043' )
        getHostAliasID( 'default_host', '*', '9080' )
        getHostAliasID( 'default_host', '*', '80' )
        getHostAliasID( 'default_host', '*', '5060' )
        getHostAliasID( 'default_host', '*', '9443' )
        getHostAliasID( 'default_host', '*', '5061' )
        getHostAliasID( 'admin_host', '*', '9060' )
        getHostAliasID( 'admin_host', '*', '9043' )
        DEBUG_SOP=0

# singleSignOn SSL very close to what is needed
#https://github.com/wsadminlib/wsadminlib/blob/c3913bac556094989ac5de40afbee772858f806c/bin/wsadminlib.py#L6880

#endfor
print "--Saving...."
AdminConfig.save()
print "--completed..."

