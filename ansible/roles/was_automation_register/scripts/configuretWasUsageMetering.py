#------------------------------------------------------------------------------------
# configuretWasUsageMetering.py - configure tWAS server with usage metering feature  
# https://www.ibm.com/docs/en/ws-automation?topic=vulnerabilities-adding-websphere-application-server-server#cf-t-add-was__wsascript
#------------------------------------------------------------------------------------
#
#  This script configures a traditional WebSphere Application Server with the usage 
#  metering service using the scripting client wsadmin.  This script creates a keystore, 
#  retrieves signer from api-usagemetering-host and store it to keystore. It also creates 
#  was-usage-metering.properties file including all required properties (input) and copy 
#  them to the given node and server. If node and server names are not given, it will copy 
#  keystore and was-usage-metering.properties to all servers. The script also synchronizes
#  the changes to the active nodes and start servers.  We assume an environment in which
#  the scripting client is connected to the Network Deployment manager, but this script 
#  could be used in a base install.
#  
#  This script contains the following required and optional parameters:  
#
#    Required parameters:
#      url    - url for accessing cpd route in "https://<cpd-route>/websphereauto/meteringapi" format 
#      apiKey - API key for authentication token
#      sslRef - SSL name of server SSL configuration
#         or 
#      trustStorePassword - trustStore password to create a new truststore
#
#    If the environment is in WebSphere Application Server 9.0.x and 
#       has the open shift CLI client command tool installed and connected to Open shift 
#       container (oc login), the script can obtain url and apiKey automatically.  User only needs to specify 
#       the "namespace" parameter such as namespace=websphere-automation and other required 
#       (sslRef or trustStorePassword) and optional parameters. If namespace is not specified, default WebSphere
#       Automation namespace will be used.
#  
#      namespace - namespace where WebSphere Automation instance is installed on OpenShift container.  
#                           namespace is needed only when url and apiKey are not specified and the environment 
#                           has installed open shift CLI client tool and connected to OpenShift container.                            
#
#    Optional parameters: 
#      trustStoreName     - truststore name, e.g. meteringTrustStore, if not specified, use default keystore name
#      certAlias          - certificate alias, a unique name to identify a certificate, if not specified, use default certificate alias
#      nodeName           - node name where to register the usage metering service, if not specified, it will configure to all nodes
#      serverName         - server name where to register the usage metering service, if not specified, it will configure to all servers 
#      clusterName        - clusterName where to register the usage metering service
#      startServers       - start all servers or a given server, e.g. startServers=true. By default, it will not start all servers or a given server 
#        
#      note - url and apiKey can be obtained from open shift CLI commands or WebSphere Automation console
#           
#
#  The script syntax: parameters can be passed in random order in paramName=paramValue
# 
#   wsadmin -lang jython -f configuretWasUsageMetering.py url=<url> apiKey=<api_key> sslRef=<ssl_name> 
#        or
#   wsadmin -lang jython -f configuretWasUsageMetering.py url=<url> apiKey=<api_key> trustStorePassword=<trustStore_password>
#        or
#   wsadmin -lang jython -f configuretWasUsageMetering.py namespace=websphere-automation sslRef=<ssl_name>
#
#
#  The syntax including optional parameters something like:  
#  
#    wsadmin -lang jython -f configuretWasUsageMetering.py url=<url> apiKey=<api_key> sslRef=<ssl_name> certAlias=<certificate_alias>
#                                                          nodeName=<node_name> serverName=<server_name> startServer=false
#
#    wsadmin -lang jython -f configuretWasUsageMetering.py url=<url> apiKey=<api_key> trustStorePassword=<trustStore_password> trustStoreName=<trustStore_name> 
#                                                          certAlias=<certificate_alis> nodeName=<node_name> serverName=<server_name>
#
#    wsadmin -lang jython -f configuretWasUsageMetering.py url=<url> apiKey=<api_key> trustStorePassword=<trustStore_password> trustStoreName=<trustStore_name> 
#                                                          certAlias=<certificate_alis> clusterName=<cluster_name>
#
#     
#--------------------------------------------------------------------------------------

import os
import os.path
import sys
import shutil


## Retrieve scripting objects from local name space
try: 
   AdminConfig = sys._getframe(1).f_locals['AdminConfig']
   AdminControl = sys._getframe(1).f_locals['AdminControl']
   AdminTask = sys._getframe(1).f_locals['AdminTask']
except:
   "" 
   

## Configure WebSphere Application Server with the usage metering feature
def configuretWasUsageMetering(url, apiKey, sslRef, trustStoreName, trustStorePassword, certAlias, nodeName, serverName, clusterName, startServers, namespace):

   # check required parameters 
   #--------------------------------------------------------------
   if len(url) == 0:
       url = getURL(namespace)
       if len(url) == 0:
          print "Error -- required parameter `url` is missing. Please specify url=<url>"
          return 
        
   if len(apiKey) == 0: 
       apiKey = getApiKey(namespace)
       if len(apiKey) == 0:
          print "Error -- required parameter `apiKey` is missing. Please specify apiKey=<apiKey>"
          return
       
   if len(sslRef) == 0 and len(trustStorePassword) == 0:
       print "Error -- required parameter `sslRef` or `trustStorePassword` is missing. Please specify either one."
       return 
        
   if len(sslRef) != 0 and len(trustStorePassword) != 0:
       print "Error -- both `sslRef` and `trustStorePassword` are specified.  Only one is required." 
       return 
        
   #--------------------------------------------------------------
   # get host and port info from url
   #--------------------------------------------------------------
   r = url.split("https://")
   r1 = r[1]
   
   # url=https://<cpd-route>:443
   if r1.find(":") == -1:
      host = r1
      port = "443"
   else:   
      hostport = r1.split(":")
      host = hostport[0] 
      port = hostport[1]
      
   # url=hthttps://<cpd-route>/websphereauto/meteringapi
   if host.find("/") != -1:
      h = host.split("/")
      host = h[0] 
   
                 
   #-------------------------------------------------------------
   # create keystore if trustStorePassword is specified
   #-------------------------------------------------------------
   if len(trustStorePassword) > 0:
       if len(trustStoreName) == 0:
           # use default keystore if trustStoreName is not specified or does not exist
           trustStoreName = "meteringTrustStore"
       trustStoreLocation = trustStoreName + ".p12"
   
       # delete existing keystore
       ks = AdminConfig.getid('/KeyStore:'+trustStoreName+'/')
       if len(ks) > 0:
           AdminTask.deleteKeyStore(['-keyStoreName', trustStoreName, '-removeKeyStoreFile', 'true' ])
           #delete keystore file to clean up
           delKeyStoreFile(trustStoreLocation)
       
       # create keystore
       print "Creating keystore " + trustStoreName + " ..." 
       ks = AdminTask.createKeyStore(['-keyStoreName', trustStoreName, '-keyStoreType PKCS12', '-keyStoreLocation', trustStoreLocation, '-keyStorePassword', trustStorePassword, '-keyStorePasswordVerify', trustStorePassword, '-keyStoreDescription', 'Usage metering truststore file'])    
                    
       print "Keystore was created: " + ks
       
   #-------------------------------------------------------------
   # Retrieve trustStore info from sslRef
   #-------------------------------------------------------------
   tsLocation = ""
   if len(sslRef) > 0:
       ssl = AdminTask.getSSLConfig(['-alias', sslRef ])
                
       # get trustStore config object from ssl
       trustStoreStart = ssl.find("[trustStore")
       trustStoreEnd = ssl.find("] [trustManager")
       trustStore = ssl[trustStoreStart+12:trustStoreEnd]
       
       # get truststore name, scope and location
       trustStoreName = AdminConfig.showAttribute(trustStore, "name")
       tsManagementScope = AdminConfig.showAttribute(trustStore, "managementScope")
       tsScope = AdminConfig.showAttribute(tsManagementScope, "scopeName")
       tsLocation = AdminConfig.showAttribute(trustStore, "location")
       
       print "Truststore was retrieved from sslRef: " + trustStore

     
   #-------------------------------------------------------------
   # retrieve signer from host and port
   #-------------------------------------------------------------
   if len(certAlias) == 0:
       # use default certificate alias if it is not specified 
       certAlias = "meteringAlias"
       
   # delete certificate if it exists in keystore
   certs = AdminTask.listSignerCertificates(['-keyStoreName', trustStoreName ] )
   certs = _splitlines(certs)
   for cert in certs:
       start = cert.find("alias")
       end = cert.find("] [version")
       alias = cert[start+6:end]
       if alias == certAlias:
           AdminTask.deleteSignerCertificate(['-keyStoreName', trustStoreName, '-certificateAlias', alias ])
   
   # retrieve new certificate from api-usagemetering-host and port
   print "Retrieving signer from port ..."
   
   # store certificate to truststore obtained from sslRef
   if len(sslRef) > 0:        
       AdminTask.retrieveSignerFromPort(['-keyStoreName', trustStoreName, '-host', host, '-port', port, '-keyStoreScope', tsScope, '-certificateAlias', certAlias ])
       
   # store certificate to truststore created from createKeyStore command
   if len(trustStorePassword) > 0:
       AdminTask.retrieveSignerFromPort(['-keyStoreName', trustStoreName, '-host', host, '-port', port, '-certificateAlias', certAlias])
   
   print "Signer was retrieved from host: " + host + ", port: " + port + " and store to keystore: " + trustStoreName 
   AdminConfig.save()

  
   #-------------------------------------------------------------
   # create was-usage-metering.properties file
   #-------------------------------------------------------------
   print "Creating was-usage-metering.properties file with all specified properties ..."
   
   propFileName = "was-usage-metering.properties"
   createPropFile(propFileName, url, apiKey, sslRef, trustStoreName, trustStorePassword)
   
   #----------------------------------------------------------------------------------------
   # copy was-usage-metering.properties and keystore files to given node and server. 
   # If no node name and server name given, copy them to all servers
   # sync changes to node/server and start server if it is not started
   #----------------------------------------------------------------------------------------
   
   # find keystore file from trust store location
   if len(sslRef) > 0 and len(tsLocation) > 0:   
       # replace ${CONFIG_ROOT} with configPath  
       if tsLocation.strip().startswith("${CONFIG_ROOT}/"):
          loc = tsLocation[tsLocation.find("${CONFIG_ROOT}")+14:len(tsLocation)]
          userInstallRoot = java.lang.System.getProperty("user.install.root")
          tsLocation = userInstallRoot + os.sep + "config" + loc 

       # find truststore file 
       keystoreFile = tsLocation[tsLocation.rfind("/")+1:len(tsLocation)] 
   else:    
       keystoreFile = trustStoreName + ".p12"
   
   # copy was-usage-metering.properties and keystore file to a given node and server
   if AdminConfig.getid("/Node:" + nodeName + "/Server:" + serverName + "/") == "":
       print "Error: server " + serverName + " does not exist on node " + nodeName + ". Unable to create documents."
       return
   else: 
       if len(nodeName) > 0 and len(serverName) > 0:
           # copy files to given node and server
           print "Copying keystore " + keystoreFile + " and was-usage-metering.properties to the node " + nodeName + " and server " + serverName + " ..."
           createDocumentsToGivenNodeServer(propFileName, keystoreFile, nodeName, serverName, tsLocation)
            
           if whatEnv() == 'base':
               print "No sync on WebSphere Base Server!"
               return
                
           else:
               # sync changes to active node 
               print "Syncing config changes to node " + nodeName + " ..."
                
               nodeagent = AdminControl.queryNames("type=NodeAgent,node="+nodeName+",*")
               if (len(nodeagent) == 0):      
                   print "WARNING: was unable to sync node. The node agent is not running!"
               else:    
                   result = syncActiveNodes()
                   print "Sync nodes were done!"
            
               # start server if it is not started
                   
   # copy was-usage-metering.properties and keystore file to all servers on a given node
   if len(nodeName) > 0 and len(serverName) == 0:
      if AdminConfig.getid("/Node:" + nodeName + "/") == "":
          print "Error: node " + nodeName + " does not exist. Unable to create documents."
          return 
      else: 
          # copy files to all servers of a given node
          print "Copying keystore " + keystoreFile + " and was-usage-metering.properties to all servers under the node " + nodeName + " ..."
          createDocumentsToAllServerOfGivenNode(propFileName, keystoreFile, nodeName, tsLocation)
      
          if whatEnv() == 'base':
              print "No sync on WebSphere Base Server!"
              return
          else:
              # sync changes to active node
              print "Syncing config changes to node " + nodeName + " ..."
              
              nodeagent = AdminControl.queryNames("type=NodeAgent,node="+nodeName+",*")
              if (len(nodeagent) == 0):      
                  print "WARNING: was unable to sync node. The node agent is not running!"
              else:      
                  result = syncActiveNodes()
                  print "Sync node was done!"
                         
              # start all servers on a given node 
              if len(startServers) > 0  and startServers == "true":
                  startServer(nodeName, "")
              else:
                  # do not start servers by default
                  return
                   

   # copy was-usage-metering.properties and keystore file to all servers
   if len(nodeName) == 0 and len(serverName) == 0 and len(clusterName) == 0: 
      # copy files to all servers of all nodes
      print "Copying keystore " + keystoreFile + " and was-usage-metering.properties to all servers ..."
      createDocumentsToAllServers(propFileName, keystoreFile, tsLocation)
      
      # sync changes to all nodes 
      if whatEnv() == 'base':
          print "No sync on WebSphere Base Server!"
          return
      
      else:
          print "Syncing config changes to all nodes ..."
          
          result = syncActiveNodes()
          if len(result) > 0:
              print "Sync nodes were done!"
          else:
              print "WARNING: was unable to sync node. Node agents are not running!" 
             
          # start all servers 
          if len(startServers) > 0  and startServers == "true":
              startAllServers()
          else:
              # do not start servers by default
              return
               

   # copy was-usage-metering.properties and keystore file to servers by the given server name of all nodes
   if len(nodeName) == 0 and len(serverName) > 0: 
       # copy files to all servers of all nodes
       print "Copying keystore " + keystoreFile + " and was-usage-metering.properties to server name " + serverName + " ..."
       nodenames = getNodeNamesFromGivenServer(serverName)
       
       if len(nodenames) == 0:
           print "Error: server " + serverName + " does not exist. Unable to create documents."
           return
       else:    
           for nodeName in nodenames:
               createDocumentsToGivenNodeServer(propFileName, keystoreFile, nodeName, serverName, tsLocation)
                      
               if whatEnv() == 'base':
                   print "On sync on WebSphere Base Server!"
                   return
                  
               else:       
                   # sync changes to all active nodes
                   print "Syncing config changes to node " + nodeName + " ..."
                   
                   nodeagent = AdminControl.queryNames("type=NodeAgent,node="+nodeName+",*")
                   if (len(nodeagent) == 0):      
                       print "WARNING: was unable to sync node. The node agent is not running!"
                   else: 
                       result = syncActiveNodes()
                       print "Sync nodes were done!"
                  
                   # start server
                   if len(startServers) > 0  and startServers == "true":
                       startServer(nodeName, serverName)
                   else:
                       # do not start server by default
                       return
                      
   # copy was-usage-metering.properties and keystore file to a given cluster
   if len(clusterName) > 0: 
      if AdminConfig.getid("/ServerCluster:" + clusterName + "/") == "":
          print "Error: cluster: " + clusterName + " does not exist. Unable to create documents to cluster"
          return
      else:
          # copy files to cluster
          print "Copying keystore " + keystoreFile + " and was-usage-metering.properties to cluster " + clusterName + " ..."
          createDocumentsToCluster(propFileName, keystoreFile, clusterName, tsLocation)
      
          # sync changes to all cluster members
          syncCluster(clusterName)

          # start all cluster members 
          if len(startServers) > 0  and startServers == "true":
              startClusterMembers(clusterName)
          else:
              # do not start cluster members by default
              return
               
 
#-------------------------------------------------------------
# private methods
#-------------------------------------------------------------

## Return config id of the Dmgr node
def getDmgrNode():
    node_ids = _splitlines(AdminConfig.list( 'Node' ))
    for node_id in node_ids:
        nodename = getNodeName(node_id)
        if nodeIsDmgr(nodename):
            return node_id
    return None

## Return node name of the Dmgr node
def getDmgrNodeName():
    return getNodeName(getDmgrNode())
    
## Return node name of the standalone node
def getStandAloneNodeName():
    node_ids = _splitlines(AdminConfig.list('Node'))
    if len(node_ids) == 1:
       for node in node_ids:
           nodename = getNodeName(node)
           return nodename
    return None  
   
## Return the WebSphere version of the node
def getNodeVersion(nodename):
    version = AdminTask.getNodeBaseProductVersion(  '[-nodeName %s]' %  nodename   )
    return version
  
## Return true if the node is the deployment manager
def nodeIsDmgr( nodename ):
    return nodeHasServerOfType( nodename, 'DEPLOYMENT_MANAGER' )
   
## Return true if the node is an unmanaged node.
def nodeIsUnmanaged( nodename ):
    return not nodeHasServerOfType( nodename, 'NODE_AGENT' )

## Check if node has server types 
def nodeHasServerOfType( nodename, servertype ):
    node_id = getNodeId(nodename)
    serverEntries = _splitlines(AdminConfig.list( 'ServerEntry', node_id ))
    for serverEntry in serverEntries:
        sType = AdminConfig.showAttribute( serverEntry, "serverType" )
        if sType == servertype:
            return 1
    return 0

## Given a node name, get its config ID
def getNodeId( nodename ):
    return AdminConfig.getid( '/Cell:%s/Node:%s/' % ( getCellName(), nodename ) )

## Return the name of the cell
def getCellName():
    cellObjects = getObjectsOfType('Cell')  # should only be one
    cellname = getObjectAttribute(cellObjects[0], 'name')
    return cellname

## Return the config object ID of the cell we're connected to
def getCellId(cellname = None):
    if cellname == None:
        cellname = getCellName()
    return AdminConfig.getid( '/Cell:%s/' % cellname )

## Return the value of the named attribute of the config object with the given ID.  
def getObjectAttribute(objectid, attributename):
    result = AdminConfig.showAttribute(objectid, attributename)
    if result != None and result.startswith("[") and result.endswith("]"):
        # List looks like "[value1 value2 value3]"
        result = _splitlist(result)
    return result
  
## Return a python list of objectids of all objects of the given type in the given scope  
def getObjectsOfType(typename, scope = None):
    if scope:
        return _splitlines(AdminConfig.list(typename, scope))
    else:
        return _splitlines(AdminConfig.list(typename))

## Get the OS of the named node. Some confirmed values: 'linux', 'windows', 'os390', 'solaris', 'hpux'
def getNodePlatformOS(nodename):
    return AdminTask.getNodePlatformOS('[-nodeName %s]' % nodename)

## Get the name of the node with the given config object ID
def getNodeName(node_id):
    return getObjectAttribute(node_id, 'name')

## Return the absolute path of the given node's profile directory
def getWasProfileRoot(nodename):
    return getNodeVariable(nodename, "USER_INSTALL_ROOT")

## Return the value of a variable for the node -- or None if no such variable or not set
def getNodeVariable(nodename, varname):                                                     
    vmaps = _splitlines(AdminConfig.list('VariableMap', getNodeId(nodename)))
    if 0 < len(vmaps):  # Tolerate nodes with no such maps, for example, IHS nodes.
        map_id = vmaps[-1] # get last one
        entries = AdminConfig.showAttribute(map_id, 'entries')
        # this is a string '[(entry) (entry)]'
        entries = entries[1:-1].split(' ')
        for e in entries:
            name = AdminConfig.showAttribute(e,'symbolicName')
            value = AdminConfig.showAttribute(e,'value')
            if name == varname:
                return value
    return None

## Return list of node names, excluding the dmgr node.
def listNodes():
    node_ids = _splitlines(AdminConfig.list( 'Node' ))
    result = []
    for node_id in node_ids:
        nodename = getNodeName(node_id)
        if not nodeIsDmgr(nodename):
            if nodename not in result:
               result.append(nodename)
       
    return result

## Return list of server names, excluding the node agent 
def listServers(nodeName):
    result = []
    servers = _splitlines(AdminConfig.getid("/Node:"+nodeName+"/Server:/"))
    for server in servers:
        servername = AdminConfig.showAttribute(server,"name")
        if servername != "nodeagent":
            if servername not in result:
               result.append(servername)
    return result 
    
## create was-usage-metering.properties file
def createPropFile(propFileName, url, apiKey, sslRef, trustStoreName, trustStorePassword):
   if os.path.exists(propFileName):
       os.remove(propFileName)
   
   propsFile= open(propFileName,"w+")
   propsFile.write("## required. Obtain url and apiKey from websphere automation console \n")
   propsFile.write("url=" + url + "\n")
   propsFile.write("apiKey=" + apiKey + "\n")
   propsFile.write("\n")
   
   propsFile.write("## One of the following is required for SSL\n")
   if len(sslRef) > 0:
       propsFile.write("sslRef=" + sslRef + "\n")
       propsFile.write("# Or the following 3 properties\n")
       propsFile.write("#trustStore=\n")
       propsFile.write("#trustStorePassword=\n")
       propsFile.write("#httpsProtocol=\n")
        
   if len(trustStorePassword) > 0: 
       propsFile.write("# sslRef=<SSL name of server SSL configuration>\n")
       propsFile.write("# Or the following 3 properties\n")
       propsFile.write("trustStore=" + trustStoreName + ".p12" + "\n")
       propsFile.write("trustStorePassword=" + trustStorePassword + "\n")
       propsFile.write("httpsProtocol=TLSv1.2\n")
   
   propsFile.write("\n")

   propsFile.write("## proxy only - to use, remove # and define proxy configuration\n")
   propsFile.write("# proxyUrl=<proxyURL>\n")
   propsFile.write("# proxyUser=<proxyUserName>\n")
   propsFile.write("# proxyPassword=<proxyPassword>\n")
   propsFile.write("\n")
   
   propsFile.write("## optional - to use, remove #\n")
   propsFile.write("# group=<group>\n")
   propsFile.write("# logData=<csv|json|all>\n")   
   propsFile.close()
   
## create keystore and was-usage-properties files to a given node and server
def createDocumentsToGivenNodeServer(propFileName, keystoreFile, nodeName, serverName, tsLocation):
    if whatEnv() == 'base':
        etcDir = os.path.join(getWasProfileRoot(nodeName), 'etc')  
        configDir = os.path.join(getWasProfileRoot(nodeName), 'config')  
        # get node's platform
        platform = getMachinePlatform(nodeName)
        version = getNodeVersion(nodeName)
    else: 
        dmgrNodeName = getDmgrNodeName()
        etcDir = os.path.join(getWasProfileRoot(dmgrNodeName), 'etc')  
        configDir = os.path.join(getWasProfileRoot(dmgrNodeName), 'config')  
        # get node's platform
        platform = getMachinePlatform(dmgrNodeName)
        version = getNodeVersion(dmgrNodeName)

    keystoreEtcName = etcDir + os.sep + keystoreFile
    serverConfigDir = configDir+os.sep+"cells"+os.sep+getCellName()+os.sep+"nodes"+os.sep+nodeName+os.sep+"servers"+os.sep+serverName+os.sep
    
    # copy files to dmgr config
    if len(tsLocation) > 0: 
        copyFile(tsLocation, serverConfigDir, platform, version)
    else:    
        copyFile(keystoreEtcName, serverConfigDir, platform, version)
                 
    print "keystoreFile " + keystoreFile + " was created on node: " + nodeName + " and server: " + serverName + "."
    print "was-usage-metering.properties was created on node: " + nodeName + " and server: " + serverName + "." 
 
                              
## create keystore and was-usage-properties files to all servers of a given node 
def createDocumentsToAllServerOfGivenNode(propFileName, keystoreFile, nodeName, tsLocation):
    if whatEnv() == 'base':
        etcDir = os.path.join(getWasProfileRoot(nodeName), 'etc')  
        configDir = os.path.join(getWasProfileRoot(nodeName), 'config')
        # get node's platform
        platform = getMachinePlatform(nodeName)
        version = getNodeVersion(nodeName)
    else: 
        dmgrNodeName = getDmgrNodeName()
        etcDir = os.path.join(getWasProfileRoot(dmgrNodeName), 'etc')  
        configDir = os.path.join(getWasProfileRoot(dmgrNodeName), 'config')  
        # get node's platform
        platform = getMachinePlatform(dmgrNodeName)
        version = getNodeVersion(dmgrNodeName)

    keystoreEtcName = etcDir + os.sep + keystoreFile
    nodeConfigDir = configDir+os.sep+"cells"+os.sep+getCellName()+os.sep+"nodes"+os.sep+nodeName
       
    # get server config paths
    serverpaths = getServerPaths(nodeConfigDir)
    for path in serverpaths:
        copyFile(propFileName, path, platform, version)
        if len(tsLocation) > 0: 
           copyFile(tsLocation, path, platform, version)
        else:    
           copyFile(keystoreEtcName, path, platform, version)
           
    print "keystoreFile " + keystoreFile + " was created on all servers of node: " + nodeName + "."
    print "was-usage-metering.properties was created on all server of node: " + nodeName + "."
                 
        
## create keystore and was-usage-properties files to all servers
def createDocumentsToAllServers(propFileName, keystoreFile, tsLocation): 
    if whatEnv() == 'base':
        nodeName = getStandAloneNodeName()
        etcDir = os.path.join(getWasProfileRoot(nodeName), 'etc')  
        configDir = os.path.join(getWasProfileRoot(nodeName), 'config')  
        # get node's platform
        platform = getMachinePlatform(nodeName)
        version = getNodeVersion(nodeName)
    else: 
        dmgrNodeName = getDmgrNodeName()
        etcDir = os.path.join(getWasProfileRoot(dmgrNodeName), 'etc')  
        configDir = os.path.join(getWasProfileRoot(dmgrNodeName), 'config') 
        # get node's platform
        platform = getMachinePlatform(dmgrNodeName)
        version = getNodeVersion(dmgrNodeName)

    keystoreEtcName = etcDir + os.sep + keystoreFile
    nodeConfigDir = configDir+os.sep+"cells"+os.sep+getCellName()+os.sep+"nodes"
       
    # get server config paths
    serverpaths = getServerPaths(nodeConfigDir)
    for path in serverpaths:
        copyFile(propFileName, path, platform, version)
        if len(tsLocation) > 0: 
           copyFile(tsLocation, path, platform, version)
        else:    
           copyFile(keystoreEtcName, path, platform, version)
           
    print "keystoreFile " + keystoreFile + " was created on all servers."
    print "was-usage-metering.properties was created on all servers."
    
                
## create keystore and was-usage-properties files to a given cluster
def createDocumentsToCluster(propFileName, keystoreFile, clusterName, tsLocation):
    dmgrNodename = getDmgrNodeName()
    etcDir = os.path.join(getWasProfileRoot(dmgrNodename), 'etc')  
    configDir = os.path.join(getWasProfileRoot(dmgrNodename), 'config')  
    keystoreEtcName = etcDir + os.sep + keystoreFile
    clusterConfigDir = configDir+os.sep+"cells"+os.sep+getCellName()+os.sep+"clusters"+os.sep+clusterName+os.sep
    
    # get node's platform
    platform = getMachinePlatform(dmgrNodename)
    
    version = getNodeVersion(dmgrNodename)
    
    # copy files to dmgr config
    copyFile(propFileName, clusterConfigDir, platform, version)
    
    if len(tsLocation) > 0: 
        copyFile(tsLocation, clusterConfigDir, platform, version)
    else:    
        copyFile(keystoreEtcName, clusterConfigDir, platform, version)
           
## Return a list of all server members in the specified cluster
def listServersInCluster(clusterName):
    clusterMembers = []
    if AdminConfig.getid("/ServerCluster:" + clusterName + "/") != "":
        clusterId = AdminConfig.getid("/ServerCluster:" + clusterName + "/")
        clusterMembers = _splitlines(AdminConfig.list("ClusterMember", clusterId ))
    return clusterMembers

## Returns 'nd' if connected to a dmgr, 'base' if connected to an unmanaged server
def whatEnv():
    # Simpler version - should work whether connected or not
    servers = getObjectsOfType('Server')
    for server in servers:
        servertype = getObjectAttribute(server, 'serverType')
        if servertype == 'DEPLOYMENT_MANAGER':
            return 'nd'  # we have a deployment manager
    return 'base'  # no deployment manager, must be base
    
## Return a list of node names for a given server name
def getNodeNamesFromGivenServer(serverName):
    result = []
    
    if whatEnv() == 'base':
        node = AdminConfig.list('Node')
        nodeName = AdminConfig.showAttribute(node, 'name')
        result.append(nodeName)     
    else:    
        nodenames = listNodes()
        for nodeName in nodenames:
            servernames = listServers(nodeName)
            for name in servernames:
                if name == serverName:
                    result.append(nodeName)
                    break
               
    return result

## Sync config to nodes - return 0 on success, non-zero on error
def syncCluster(clusterName): 
    if len(clusterName) > 0:
       clusterMembers = listServersInCluster(clusterName)
       for clusterMember in clusterMembers:
           nodeName = AdminConfig.showAttribute( clusterMember, "nodeName" )
           
           # sync changes to all active nodes
           print "Syncing config changes to node " + nodeName + " ..."
           
           nodeagent = AdminControl.queryNames("type=NodeAgent,node="+nodeName+",*")
           if (len(nodeagent) == 0):      
               print "WARNING: was unable to sync node. The node agent is not running!"
           else: 
               result = syncActiveNodes()
               print "Sync nodes were done!"

## sync active node
def syncActiveNodes():
    repository = AdminControl.queryNames("type=ConfigRepository,process=dmgr,*")
    AdminControl.invoke(repository, "refreshRepositoryEpoch")
    dp = AdminControl.queryNames("type=DeploymentManager,*")
    result = AdminControl.invoke(dp, "syncActiveNodes", "true")
    return result
         
## sync node
def syncNode(nodeName):
    if whatEnv() == 'base':
       print "No sync on WebSphere Base Server!"
       return

    if len(nodeName) == 0:
        nodenames = listNodes()
        for nodename in nodenames:
            syncNode(nodename)
    else:
        if not nodeIsDmgr( nodeName ) and not nodeIsUnmanaged( nodeName ):
            print "Syncing config changes to node " + nodeName + " ..."
            sync = AdminControl.completeObjectName( "type=NodeSync,node=%s,*" % nodeName )
            if sync != "":
                rc = AdminControl.invoke( sync, 'sync' )
                if rc != 'true':  # failed
                   print "Sync of node " + nodeName + " FAILED"
                else:
                   print "Sync was done on node " + nodeName + " !"   
            else:
                print "WARNING: was unable to get sync object for node " + nodeName + " . The node agent is not running!" 
                print "Start node and rerun the script!"
                  
## start servers on a given node
def startServer(nodeName, serverName):
    if whatEnv() == 'base':
       print "WebSphere Base Server, server was started already!"
       return

    nodeagent = AdminControl.queryNames("type=NodeAgent,node="+nodeName+",*")
    if (len(nodeagent) == 0):      
        print "WARNING: was unable to start server " + serverName + " on node " + nodeName + ". The node agent is not running!"
        print "Start node and rerun the script!" 
    else:
        if len(serverName) == 0:
            servernames = listServers(nodeName)
            for serverName in servernames:
                if (serverName != "nodeagent"):
                    runningServer = AdminControl.queryNames("type=Server,node="+nodeName+",name="+serverName+",*")
                    if len(runningServer) == 0 or AdminControl.getAttribute(runningServer, "state") != "STARTED":
                        print "Starting server " + serverName + " on node " + nodeName + " ..."
                        AdminControl.startServer(serverName, nodeName)
        else:
            runningServer = AdminControl.queryNames("type=Server,node="+nodeName+",name="+serverName+",*")
            if len(runningServer) == 0 or AdminControl.getAttribute(runningServer, "state") != "STARTED":
                print "Starting server " + serverName + " on node " + nodeName + " ..."
                AdminControl.startServer(serverName, nodeName)
                     
## start all servers
def startAllServers():
    nodenames = listNodes()
    for nodeName in nodenames:
        servernames = listServers(nodeName)
        for serverName in servernames:
            startServer(nodeName, serverName)
            
## start all cluster members
def startClusterMembers(clusterName):
    clusterMembers = listServersInCluster(clusterName)
    for clusterMember in clusterMembers:
        nodeName = AdminConfig.showAttribute( clusterMember, "nodeName" )
        serverName = AdminConfig.showAttribute( clusterMember, "memberName" )
        startServer(nodeName, serverName)

##  Get the machine Platform. Return win if the OS is Windows, otherwise return unix         
def getMachinePlatform(nodename):
    platformOS = getNodePlatformOS(nodename)
    if platformOS == "windows":
        platform = "win"
    else:
        platform = "unix"
    return platform

 
# search all server directories
def getServerPaths(configNodedir):
    paths = []
    for file in os.listdir(configNodedir):
        if configNodedir.endswith("nodes"):
           d = os.path.join(configNodedir, file)
           s = os.path.join(d, "servers") 
           for s1 in os.listdir(s):
               if s1 != "dmgr" and s1 != "nodeagent":
                  path = os.path.join(s, s1)
                  paths.append(path)
         
        else: # ends with nodename
           if file == "servers":
              ss = os.path.join(configNodedir, file)
                        
              for s1 in os.listdir(ss):
                  if s1 != "dmgr" and s1 != "nodeagent":
                     path = os.path.join(ss, s1)
                     paths.append(path)
    return paths   
    
# obtain url value from openshift container
def getURL(namespace): 
    url=""

    # get machine platform
    if whatEnv() == 'base':
       nName = getStandAloneNodeName()
    else: 
       nName = getDmgrNodeName()   
       
    # get node's platform
    platform = getMachinePlatform(nName)
    
    # get node's WAS version
    version = getNodeVersion(nName)
  
    # only support for WAS V9.0
    if version.startswith("9.0"):
       
       import subprocess
       
       # check if user is login to open shift container"
       output = ""
       try: 
          command = "oc whoami"
          output = subprocess.check_output(command, shell=True)
       except:
          print "Warning: user is not login to open shift container and please login to openshift or specify url parameter."

       # execute oc command to get url
       if len(output) > 0:  
          if platform == "win":
             if len(namespace) == 0:
                # use default WebSphereAutomation namespace
                namespace = "websphere-automation"
                print "Using WebSphere Automation default namespace: " + namespace
      
             # set namespace environment varialbe
             os.environ["namespace"] = namespace
            
             # invoke oc comamnd to get cpd route url
             try: 
                command = "oc get route cpd -n %namespace% -o jsonpath=https://{.spec.host}/websphereauto/meteringapi"
                             
             except subprocess.CalledProcessError:
                print "Error: oc command failed and unable to obtain url from openshift."
          # unix 
          else:  
             if len(namespace) == 0:
                # use default WebSphereAutomation namespace
                namespace = "websphere-automation"
                print "Using WebSphere Automation default namespace: " + namespace
       
             # set namespace environment varialbe
             os.environ["namespace"] = namespace
             
             # invoke oc comamnd to get cpd route url
             try:
                command = "oc get route cpd -n $namespace -o jsonpath=https://{.spec.host}/websphereauto/meteringapi"   
             except subprocess.CalledProcessError:
                print "Error: oc command failed and unable to obtain url from openshift."

          url = subprocess.check_output(command, shell=True)

          if len(url) > 0:
             print "Obtained from open shift:"  
             print "  url: " + url
    else:
         print "Unable to obtain url value in WebSphere Application Server v8.5.5"   
   
    return url
    
       
# obtain apiKey value from openshift container
def getApiKey(namespace):
    apiKey = ""

    # get machine platform
    if whatEnv() == 'base':
       nName = getStandAloneNodeName()
    else: 
       nName = getDmgrNodeName()   
    platform = getMachinePlatform(nName)
    
    # get node's platform
    platform = getMachinePlatform(nName)
    
    # get node's WAS version
    version = getNodeVersion(nName)

    # only support for WAS V9.0
    if version.startswith("9.0"):
      
       import subprocess

       # check if user is login to open shift"
       output = ""
       try: 
          command = "oc whoami"
          output = subprocess.check_output(command, shell=True)
       except:
          print "Warning: user is not login to open shift container and please login to openshift or specify apiKey parameter."
          
       if len(output) > 0: 
          if platform == "win":
             if len(namespace) == 0:
                # use default WebSphereAutomation namespace
                namespace = "websphere-automation"
                print "Using WebSphere Automation default namespace: " + namespace

             # set namespace environment varialbe
             os.environ["namespace"] = namespace

             # invoke oc command to get apiKey
             try:
                command = "oc get WebSphereSecure -n %namespace% -o jsonpath={.items[?(@.kind=='WebSphereSecure')].metadata.name}"
                instance_name = subprocess.check_output(command, shell=True) 
                command = "oc -n %namespace% get secret "+instance_name+"-metering-apis-encrypted-tokens -o jsonpath={.data."+instance_name+"-metering-apis-sa}"
                output = subprocess.check_output(command, shell=True)
                apiKey = output.decode('base64', 'strict')
             
             except subprocess.CalledProcessError:
                print "oc command failed and unable to obtain apiKey from openshift."
 
          # unix environment
          else:
             if len(namespace) == 0:
                # use default WebSphereAutomation namespace
                namespace = "websphere-automation"
                print "Using WebSphere Automation default namespace: " + namespace

             # set namespace environment varialbe
             os.environ["namespace"] = namespace

             # invoke oc command to get apiKey
             try: 
                command = "oc get WebSphereSecure -n $namespace -o jsonpath='{.items[?(@.kind==\"WebSphereSecure\")].metadata.name}'"
                instance_name = subprocess.check_output(command, shell=True) 
                command = "oc -n $namespace get secret "+instance_name+"-metering-apis-encrypted-tokens -o jsonpath='{.data."+instance_name+"-metering-apis-sa}' | base64 -d"
                apiKey = subprocess.check_output(command, shell=True)
             except subprocess.CalledProcessError:
                print "oc command failed and unable to obtain apiKey from openshift."
            
          if len(apiKey) > 0:
             print "  apiKey: " + apiKey
            
    else:
        print "Unable to obtain apiKey value in WebSphere Application Server v8.5.5"   
 
    return apiKey   
    
   
# delete existing keystore file
def delKeyStoreFile(fileName):
    if whatEnv() == 'base':
        nodeName = getStandAloneNodeName()
        etcDir = os.path.join(getWasProfileRoot(nodeName), 'etc')  
    else: 
        dmgrNodeName = getDmgrNodeName()
        etcDir = os.path.join(getWasProfileRoot(dmgrNodeName), 'etc')  
      
    keystoreEtcName = etcDir + os.sep + fileName

    if os.path.exists(keystoreEtcName):
        os.remove(keyStoreEtcName)
        

# copy file from src to target     
def copyFile(fileName, targetDir, platform, version):
    file = java.io.File(fileName)
    srcPath = file.getAbsolutePath()
    
    target = java.io.File(targetDir)
    if (target.exists() == 0):
       dir = java.io.File(targetDir)
       dir.mkdir()
    else:
       dir = targetDir
    
    # in case paths have space on
    if platform == "unix": 
       srcPath = "\"" + srcPath + "\""
       targetDir = "\"" + targetDir + "\""
    
    if platform == "win":
       srcPath = srcPath.replace("\\", "/")
       targetDir = targetDir.replace("\\", "/")
       shutil.copy2(srcPath, targetDir)
    else:  
       command = "cp " + srcPath + " " + targetDir
       os.system(command)
       

## Split a line
def _splitlines(s):
    rv = [s]
    if '\r' in s:
       rv = s.split('\r\n')
    elif '\n' in s:
       rv = s.split('\n')
    if rv[-1] == '':
       rv = rv[:-1]
    return rv
 
## Given a string of the form [item item item], return a list of strings, one per item.
def _splitlist(s):
    if s[0] != '[' or s[-1] != ']':
       raise "Invalid string: %s" % s
    return s[1:-1].split(' ')

      
#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if (len(sys.argv) == 0):
    print "configuretWasUsageMetering: this script requires parameters: url, apiKey, sslRef or trustStorePassword (required), trustStoreName, certAlias, nodeName, serverName or clusterName, startServers (optional) or "
    print "requires parameters: sslRef or trustStorePassword (required), namespace (used to obtain url and apiKey from openshift), trustStoreName, certAlias, nodeName, serverName or clusterName, startServers (optional)" 
    print "e.g.: wsadmin -lang jython -f configuretWasUsageMetering url=https://cpdRoute.test.com:443 apikey=abcd sslRef=mySSL" 
    print "e.g.: wsadmin -lang jython -f configuretWasUsageMetering url=https://cpdRoute.test.com:443 apikey=abcd trustStorePassword=password"
    print "e.g.: wsadmin -lang jython -f configuretWasUsageMetering namespace=websphere-automation sslRef=mySSL" 
    print "e.g.: wsadmin -lang jython -f configuretWasUsageMetering url=https://cpdRoute.test.com:443 apikey=abcd trustStorePassword=password trustStoreName=meteringTrustStore certAlias=meteringAlias"
else:     
    url = ""
    apiKey = ""
    sslRef = ""
    trustStoreName = ""
    trustStorePassword = ""
    certAlias = ""
    nodeName = ""
    serverName = ""
    clusterName = ""
    startServers = ""
    namespace = ""

    # Get full command-line arguments
    args = sys.argv
    argslist = args[0:]
    for arg in argslist:
        if arg.find("=") != -1:
            argName = arg.split("=")[0].strip()
            argValue = arg.split("=")[1].strip()
            if argName.lower() == "url":
                url = argValue
            if argName.lower() == "apikey":
                apiKey = argValue
            if argName.lower() == "sslref":
                sslRef = argValue
            if argName.lower() == "truststorepassword":
                trustStorePassword = argValue
            if argName.lower() == "truststorename":
                trustStoreName = argValue
            if argName.lower() == "certalias":
                certAlias = argValue
            if argName.lower() == "nodename":        
                nodeName = argValue
            if argName.lower() == "servername":
                serverName = argValue
            if argName.lower() == "clustername":
                clusterName = argValue 
            if argName.lower() == "startservers":
                startServers = argValue   
            if argName.lower() == "namespace":
                namespace = argValue
                   
    print "Input arguments:"   
        
    if len(url) > 0:
        print "  url: " + url
    if len(apiKey) > 0:
        print "  apiKey: " + "********"  #### schader@us.ibm.com - do not echo sensitive info
    if len(sslRef) > 0:
        print "  sslRef: " + sslRef
    if len(trustStoreName) > 0:
        print "  trustStoreName: " + trustStoreName
    if len(trustStorePassword) > 0:    
        print "  trustStorePassword: " + "********"
    if len(certAlias) > 0:    
        print "  certAlias: " + certAlias
    if len(nodeName) > 0:
        print "  nodeName: " + nodeName
    if len(serverName) > 0:   
        print "  serverName: " + serverName
    if len(clusterName) > 0:
        print "  clusterName: " + clusterName  
    if len(startServers) > 0:
        print "  startServers: " + startServers  
    if len(namespace) > 0:
        print "  namespace: " + namespace
   
    configuretWasUsageMetering(url, apiKey, sslRef, trustStoreName, trustStorePassword, certAlias, nodeName, serverName, clusterName, startServers, namespace)
   
#endIf
