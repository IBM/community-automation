import sys

# this is the full script that needs to be broken down into 2
#-----------------------------------------------------------------
# WARNING: Jython/Python is extremely sensitive to indentation
# errors. Please ensure that tabs are configured appropriately
# for your editor of choice.
#-----------------------------------------------------------------

#-----------------------------------------------------------------
# daytrader_config_base.py - DayTrader Single Server Install Script
#-----------------------------------------------------------------
#
# This script is designed to configure the JDBC and JMS resource required by
# the DayTrader application. Both single server and clustered environments are
# supported. A "silent install" option is also supported after manually setting
# the default config options in this file.
#  
# To invoke the script type:
#   wsadmin -f daytrader_config_base.py [all|configure|cleanup|install|uninstall] nodename servername
#      where:   all        -  configures JDBC and JMS resources and installs the app
#               configure  -  only configures the JDBC and JMS resource
#               cleanup    -  removes the JDBC and JMS resources
#               install    -  installs the DayTrader ear
#               uninstall  -  uninstalls the DayTrader ear
#
# If no parameters are specified, "all" is assumed!
#

print "daytrader_config_base.py"

# Process the resource file containing all of the admin task definitions 
resources = "resource_scripts.py"
wsadminlib = "wsadminlib.py"
execfile(wsadminlib)
execfile(resources)

# Edit this parameter to switch between Interactive and Silent installs
SilentInstall = "true"

#---------------------------------------------------------------------
# Default Properties for Silent Install
#
# Edit the variables in this section to perform a silent install. 
#---------------------------------------------------------------------

# Silent install properties for Managed Node
# - Modify these properties to specify the target node and server

TargetNodeName =   "server1"
TargetServerName = "server1"

# Security options
# Note: If global security is enabled or will be enabled at some point and
#   time, the AdminAuthAlias should be updated with a valid administrative
#   userid and password. In single-server configurations, this can be provided
#   by role-based auth (default), local OS auth, LDAP, etc. For cluster 
#   configurations, LDAP, Windows Active Directory or some other form of 
#   centralized authentication mechanism must be used to validate the userid.
SecurityEnabled = "true"
DefaultAdminUser =   "persona1"
DefaultAdminPasswd = "ppersona1"

# JDBC provider options
# JDBC provider types include:
DefaultProviderType =   "DB2 Using IBM JCC Driver"
DefaultNativePathName = ""
implementationClassName="com.ibm.db2.jcc.DB2ConnectionPoolDataSource"

# Datasource options
# Note: For Oracle, default port is 1521. For DB2, 50000.
DefaultDatabaseName = "TRADEDB"
DefaultHostname =     "yourdb.rtp.raleigh.ibm.com"
DefaultPort =         "50000"
DefaultUser =         "db2inst1"
DefaultPasswd =       "yourpass"

# Deploy options
# Deploy types include:
#   "DB2UDB_V82","DB2UDBOS390_V8","DB2UDBISERIES_V54","DERBY_V10","MSSQLSERVER_2005","ORACLE_V10G","INFORMIX_V100"
DefaultEJBDeployType = "DB2UDB_V95"

# JMS Messaging Engine Datastore options
# Note: true - file store will be used
#       false - database data store will be used
DefaultMEFileStore = "true"
DefaultMEFileStoreLocation = "default" 


#---------------------------------------------------------------------
#  Misc options
#---------------------------------------------------------------------

CmdOptions =      ["all", "configure", "cleanup"]
DefaultOptions =  ["yes", "no"]
BooleanOptions =  ["true", "false"]

#---------------------------------------------------------------------
# Application specific config information
#
# NOTE: This should NOT be modified!!!
#---------------------------------------------------------------------
DefaultTradeAppName = "{{ DefaultAppName }}"
DefaultEarFile = "{{ DefaultEarFile }}"

# Deployment options
# Deployment options
DefaultRunEJBDeploy = "false"
DefaultRunWSDeploy =  "false"
DefaultBindings =     "true"
DefaultUseMetadata =  "true"

# JDBC Driver and DataSource Config Parameters
# Datasource properties
DefaultDatasourceName = "TradeDataSource"
DefaultDatasourceAuthAliasName =  "TradeDataSourceAuthData"
DefaultNoTxDatasourceName = "NoTxTradeDataSource"

DefaultStmtCacheSize =  100
DefaultXA = "false"

# JMS (Messaging) Config Parameters
# Global Security properties for JMS
DefaultAdminAuthAliasName = "TradeAdminAuthData"

#reliability = "ASSURED_PERSISTENT"
reliability = "EXPRESS_NONPERSISTENT"

#deliveryMode = "Persistent"
deliveryMode = "NonPersistent"

#durability = "Durable"
durability = "NonDurable"

# Queue/Topic Names
brokerSIBDest =  "TradeBrokerJSD"
topicSpace =     "Trade.Topic.Space"
brokerJMSQCF =   "TradeBrokerQCF"
streamerJMSTCF = "TradeStreamerTCF"
brokerQueue =    "TradeBrokerQueue"
streamerTopic =  "TradeStreamerTopic"
brokerMDB =      "TradeBrokerMDB"
streamerMDB =    "TradeStreamerMDB"

WebbrokerJMSQCF =   "QueueConnectionFactory"
WebstreamerJMSTCF = "TopicConnectionFactory"
WebbrokerQueue =    "BrokerQueue"
WebstreamerTopic =  "StreamerTopic"
WebbrokerMDB =      "BrokerMDB"
WebstreamerMDB =    "StreamerMDB"

#---------------------------------------------------------------------
# Common JDBC Driver Paths 
#---------------------------------------------------------------------
# Note: wsadmin parses the command line based on ";" regardless of platform type
DB2WinJccPath =         "c:/sqllib/java/db2jcc.jar;c:/sqllib/java/db2jcc_license_cu.jar;"
DB2zSeriesNativePath =  "/usr/lpp/db2/db2810/jcc/lib"
DB2CliPath =            "c:/sqllib/java/db2java.zip"
OraclePath =            "c:/oracle/product/10.1.0/db_1/jdbc/lib/ojdbc14.jar"
DerbyPath =             "$\{WAS_INSTALL_ROOT\}/derby/lib/derby.jar"
DB2iSeriesNativePath =  "/QIBM/ProdData/Java400/ext/db2_classes.jar"
DB2iSeriesToolboxPath = "/QIBM/ProdData/HTTP/Public/jt400/lib/jt400.jar"


# NOTE: edit daytrader_vars.py for custom settings
#       if any of the defaults in this script need changing, move to the daytrader_vars.py
dtvars = "daytrader_vars.py"
execfile(dtvars)

# Deploy types include:
DefaultPathName = "${WAS_INSTALL_ROOT}/db2jars/db2jcc4.jar;${WAS_INSTALL_ROOT}/db2jars/db2jcc_license_cu.jar"
DefaultEJBDeployType = "DB2UDB_V82"
#---------------------------------------------------------------------
#  Basic App Administration Procedures
#---------------------------------------------------------------------

def printUsageAndExit ():
	print ""
	print "Usage: wsadmin -f daytrader_config_base.py [all|configure|cleanup|install|uninstall] nodename servername username password db2DriverLocation"
	print ""
	print "   where:  all        -  configures JDBC and JMS resources and installs the app"
	print "           configure  -  only configures the JDBC and JMS resource"
	print "           cleanup    -  removes the JDBC and JMS resources"
	print "..."
	print "...nodename:    Node to install to"
	print "...servername:  Server to install to"
	print "...username:    Security user name"
	print "...password:    Security password"
	print ""
	sys.exit()
#endDef 


#---------------------------------------------------------------------
#  Parse Command Line
#---------------------------------------------------------------------

if (len(sys.argv) == 0):
	operation = "all"
elif (sys.argv[0] in CmdOptions):
	operation = sys.argv[0]
else:
	printUsageAndExit( )
#endElse 


print ""
print "------------------------------------------------"
print " Daytrader Install/Configuration Script"
print ""
print " Operation:  		" + operation
print " Silent:     		" + SilentInstall
print " SecurityEnabled:	",SecurityEnabled
print " DefaultAdminUser:	",DefaultAdminUser 
print " DefaultAdminPasswd:	",DefaultAdminPasswd
print " DefaultProviderType:	",DefaultProviderType
print " DefaultNativePathName:	",DefaultNativePathName
print " DefaultDatabaseName:	",DefaultDatabaseName
print " DefaultHostname:	",DefaultHostname
print " DefaultPort:		",DefaultPort
print " DefaultPathName:	",DefaultPathName
print " DefaultUser:		",DefaultUser
print " DefaultPasswd:		",DefaultPasswd
print " DefaultTradeAppName:	",DefaultTradeAppName
print " DefaultEarFile:		",DefaultEarFile
print "------------------------------------------------"

#---------------------------------------------------------------------
# Daytrader configuration procedures
#---------------------------------------------------------------------

scope = ""

if (operation == "all" or operation == "configure"):
	# Create the JDBC/Datasource config objects
	
	if (scope == ""):
		scope = AdminConfig.getid("/Node:"+TargetNodeName+"/Server:"+TargetServerName+"/")
	#endIf

	print ""
	print "------------------------------------------------"
	print " Configuring JDBC/Datasource Resources"
	print " Scope: "+scope
	print "------------------------------------------------"

	createJAASAuthData(DefaultDatasourceAuthAliasName, DefaultUser, DefaultPasswd )

	provider = createJDBCProvider(DefaultProviderType, DefaultXA, scope, DefaultPathName, DefaultNativePathName )

	datasource = createDatasource(DefaultDatasourceName, "jdbc/"+DefaultDatasourceName, DefaultStmtCacheSize, DefaultDatasourceAuthAliasName, provider)
	noTxDatasource = createDatasource(DefaultNoTxDatasourceName, "jdbc/"+DefaultNoTxDatasourceName, 10, DefaultDatasourceAuthAliasName, provider)
	addDatasourceProperty(noTxDatasource, "nonTransactionalDataSource", "true")

	updateDB2orDerbyDatasource(datasource, DefaultDatabaseName, DefaultHostname, DefaultPort, DefaultDB2DriverType)
	updateDB2orDerbyDatasource(noTxDatasource, DefaultDatabaseName, DefaultHostname, DefaultPort, DefaultDB2DriverType)
	
	#endIf

	productVersion=AdminTask.getNodeBaseProductVersion(['-nodeName', TargetNodeName])
	if ( productVersion.find('9') == 0 ):
		print "  Setting JPA level 2.0"
		AdminTask.modifyJPASpecLevel(scope,'[-specLevel 2.0]')

	print ""
	print "------------------------------------------------"
	print " JDBC Resource Configuration Completed!!!"
	print "------------------------------------------------"

	# Create the JMS config objects

	print ""
	print "------------------------------------------------"
	print " Configuring JMS Resources"
	print " Scope: "+scope
	print "------------------------------------------------"

	createJAASAuthData(DefaultAdminAuthAliasName, DefaultAdminUser, DefaultAdminPasswd )

	sibus = createSIBus(getName(scope ), DefaultAdminAuthAliasName )
	fileStore = [DefaultMEFileStore, DefaultMEFileStoreLocation]
	target = [TargetNodeName, TargetServerName]
	dsParms = ["true", "dummy"]
	addSIBusMember(sibus, fileStore, target, dsParms)

	if (SecurityEnabled == "true"):
		createSIBusSecurityRole(sibus, DefaultAdminUser )
	#endIf 

	# Create the Trade Broker Queue and Trade TopicSpace Destinations

	createSIBDestination(sibus, brokerSIBDest, "Queue", reliability, target )
	createSIBDestination(sibus, topicSpace, "TopicSpace", reliability, [] )

	createJMSConnectionFactory(sibus, brokerJMSQCF, "Queue", "jms/"+brokerJMSQCF, DefaultAdminAuthAliasName, scope )
	createJMSConnectionFactory(sibus, streamerJMSTCF, "Topic", "jms/"+streamerJMSTCF, DefaultAdminAuthAliasName, scope )

	createJMSConnectionFactory(sibus, WebbrokerJMSQCF, "Queue", "web/jms/"+WebbrokerJMSQCF, DefaultAdminAuthAliasName, scope )
	createJMSConnectionFactory(sibus, WebstreamerJMSTCF, "Topic", "web/jms/"+WebstreamerJMSTCF, DefaultAdminAuthAliasName, scope )

	createJMSQueue(brokerQueue, "jms/"+brokerQueue, brokerSIBDest, deliveryMode, scope )
	createJMSTopic(streamerTopic, "jms/"+streamerTopic, topicSpace, deliveryMode, scope )

	createJMSQueue(WebbrokerQueue, "web/jms/"+WebbrokerQueue, brokerSIBDest, deliveryMode, scope )
	createJMSTopic(WebstreamerTopic, "web/jms/"+WebstreamerTopic, topicSpace, deliveryMode, scope )

	createMDBActivationSpec(brokerMDB, "eis/"+brokerMDB, sibus, "jms/"+brokerQueue, "javax.jms.Queue", DefaultAdminAuthAliasName, scope, durability )
	createMDBActivationSpec(streamerMDB, "eis/"+streamerMDB, sibus, "jms/"+streamerTopic, "javax.jms.Topic", DefaultAdminAuthAliasName, scope, durability )

	createMDBActivationSpec(WebbrokerMDB, "eis/"+WebbrokerMDB, sibus, "web/jms/"+WebbrokerQueue, "javax.jms.Queue", DefaultAdminAuthAliasName, scope, durability )
	createMDBActivationSpec(WebstreamerMDB, "eis/"+WebstreamerMDB, sibus, "web/jms/"+WebstreamerTopic, "javax.jms.Topic", DefaultAdminAuthAliasName, scope, durability )

	print ""
	print "------------------------------------------------"
	print " JMS Resource Configuration Completed!!!"
	print "------------------------------------------------"

	print ""
	print "Saving..."
	AdminConfig.save( )
#endIf 


#---------------------------------------------------------------------
# Daytrader install procedures
#---------------------------------------------------------------------

if (operation == "all" or operation == "install"):
	print " "
	print "------------------------------------------------"
	print " Installing DayTrader"
	print "------------------------------------------------"

	target = [TargetNodeName, TargetServerName]

	addHostAliasToDefaultHost( defaultWebServerHostPort )
	addHostAliasToDefaultHost( defaultWebServerHostPortS )
	# hard code in case the proxy fall on 81/82
	addHostAliasToDefaultHost( "81" )
	addHostAliasToDefaultHost( "82" )
	# hard code - not sure what's wrong with the port check function
	addHostAliasToDefaultHost( "9081" )
	addHostAliasToDefaultHost( "9082" )

	installApp(DefaultTradeAppName, DefaultEarFile, DefaultRunEJBDeploy, DefaultRunWSDeploy, "true", "false", DefaultEJBDeployType, target )
	# if there is a webserver map it
	# [7/23/14 10:56:50:931 EDT] WebServer
	webServerList = AdminTask.listServers('[-serverType WEB_SERVER ]').split(lineSeparator)
	for webServer in webServerList:
		#example: webServer=webserver1(cells/server1/nodes/srs07.rtp.raleigh.ibm.com-node/servers/webserver1|server.xml)
		TargetWebNodeName=webServer[webServer.find("nodes/"):len(webServer)]
		TargetWebNodeName=TargetWebNodeName[len("nodes/"):TargetWebNodeName.rfind("/servers/")]
		webServer = getName(webServer)

		if ( DTVERSION == "DT70" ):     
			# [10/12/16 10:40:12:922 EDT] Enterprise Applications > Enterprise Applications
			AdminApp.edit(DefaultTradeAppName, '[  -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -appname DayTrader7011 -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule -clientMode isolated -novalidateSchema -MapMessageDestinationRefToEJB [[ "DayTrader Enterprise Bean Definitions" TradeSLSBBean daytrader-ee7-ejb.jar,META-INF/ejb-jar.xml com.ibm.websphere.samples.daytrader.ejb3.TradeSLSBBean/tradeBrokerQueue jms/TradeBrokerQueue ][ "DayTrader Enterprise Bean Definitions" TradeSLSBBean daytrader-ee7-ejb.jar,META-INF/ejb-jar.xml com.ibm.websphere.samples.daytrader.ejb3.TradeSLSBBean/tradeStreamerTopic jms/TradeStreamerTopic ][ "DayTrader Web" "" daytrader-ee7-web.war,WEB-INF/web.xml jms/StreamerTopic jms/TradeStreamerTopic ][ "DayTrader Web" "" daytrader-ee7-web.war,WEB-INF/web.xml jms/BrokerQueue jms/TradeBrokerQueue ]] -MapResEnvRefToRes [[ "DayTrader Web" "" daytrader-ee7-web.war,WEB-INF/web.xml com.ibm.websphere.samples.daytrader.web.prims.PingManagedExecutor/mes javax.enterprise.concurrent.ManagedExecutorService wm/default ][ "DayTrader Web" "" daytrader-ee7-web.war,WEB-INF/web.xml com.ibm.websphere.samples.daytrader.web.prims.PingManagedThread/managedThreadFactory javax.enterprise.concurrent.ManagedThreadFactory wm/default ][ "DayTrader Enterprise Bean Definitions" TradeSLSBBean daytrader-ee7-ejb.jar,META-INF/ejb-jar.xml com.ibm.websphere.samples.daytrader.ejb3.TradeSLSBBean/managedThreadFactory javax.enterprise.concurrent.ManagedThreadFactory wm/default ]]]' )

			# [4/16/19 9:09:38:257 EDT] Enterprise Applications > DayTrader-ee7.0.11-editionPersistence01 > Security role to user/group mapping
			AdminApp.edit(DefaultTradeAppName, '[  -MapRolesToUsers [[ grp1 AppDeploymentOption.No AppDeploymentOption.Yes "" "" AppDeploymentOption.No "" "" ][ grp2 AppDeploymentOption.No AppDeploymentOption.Yes "" "" AppDeploymentOption.No "" "" ][ grp3 AppDeploymentOption.No AppDeploymentOption.Yes "" "" AppDeploymentOption.No "" "" ][ grp4 AppDeploymentOption.No AppDeploymentOption.Yes "" "" AppDeploymentOption.No "" "" ][ grp5 AppDeploymentOption.No AppDeploymentOption.Yes "" "" AppDeploymentOption.No "" "" ]]]' )
		else:
			print " --Daytrader - -MapModulesToServers:"+webServer
			parms = "[  -MapModulesToServers [[ \"DayTrader Web\" web.war,WEB-INF/web.xml WebSphere:cell="
			parms += getName(getCellId())
			parms +=  ",node="
			parms += TargetNodeName
			parms +=  ",server="
			parms += TargetServerName
			parms +=  "+WebSphere:cell="
			parms += getName(getCellId())
			parms +=  ",node="
			parms += TargetWebNodeName
			parms +=  ",server="
			parms +=  webServer

			if ( DTVERSION == "DT30" ):
				parms += " ][ Rest.war Rest.war,WEB-INF/web.xml WebSphere:cell="
				parms += getName(getCellId())
				parms +=  ",node="
				parms += TargetNodeName
				parms +=  ",server="
				parms += TargetServerName
				parms +=  "+WebSphere:cell="
				parms += getName(getCellId())
				parms +=  ",node="
				parms += TargetWebNodeName
				parms +=  ",server="
				parms +=  webServer
			#endif
			parms += " ]]]"
			print "AdminApp.edit Manage Modules parms="+parms

			AdminApp.edit(DefaultTradeAppName, parms )
		#endif



	print ""
	print "------------------------------------------------"
	print " DayTrader Installation Completed!!!"
	print "------------------------------------------------"

	print ""
	print "Saving..."
	AdminConfig.save( )
#endIf

if (operation == "uninstall"):
	print " "
	print "------------------------------------------------"
	print " Uninstalling DayTrader"
	print "------------------------------------------------"

	uninstallApp(DefaultTradeAppName)

	print ""
	print "------------------------------------------------"
	print " DayTrader Uninstall Completed!!!"
	print "------------------------------------------------"

	print ""
	print "Saving..."
	AdminConfig.save( )
#endIf

if (operation == "cleanup"):
	print " "
	print "------------------------------------------------"
	print " Uninstalling JMS Resources"
	print "------------------------------------------------"

	deleteMDBActicationSpec(brokerMDB)
	deleteMDBActicationSpec(streamerMDB)

	deleteJMSQueue(brokerQueue)
	deleteJMSTopic(streamerTopic)

	deleteJMSQueue(WebbrokerQueue)
	deleteJMSTopic(WebstreamerTopic)

	deleteJMSConnectionFactory(brokerJMSQCF)
	deleteJMSConnectionFactory(streamerJMSTCF)
	deleteJMSConnectionFactory(WebbrokerJMSQCF)
	deleteJMSConnectionFactory(WebstreamerJMSTCF)

	deleteSIBDestination(brokerSIBDest)
	deleteSIBDestination(topicSpace)

	deleteSIBus(getName(getNodeIdDT("")))

	removeJAASAuthData(DefaultAdminAuthAliasName)

	print " "
	print "------------------------------------------------"
	print " Uninstalling JDBC Resources"
	print "------------------------------------------------"

	removeDatasource(DefaultDatasourceName)
	removeDatasource(DefaultNoTxDatasourceName)
	removeJAASAuthData(DefaultDatasourceAuthAliasName)

	print ""
	print "------------------------------------------------"
	print " DayTrader Resource Cleanup Completed!!!"
	print "------------------------------------------------"

	print ""
	print "Saving..."
	AdminConfig.save( )
#endIf

print ""
print "Saving config..."
AdminConfig.save( )


