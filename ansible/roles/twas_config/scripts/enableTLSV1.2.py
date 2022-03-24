#--------------------------------------------------------------------
# WebSphere TLS V2 enablement
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f enableTLSV2.py
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
# dmgr put enableTLSV2.py bin/enableTLSV2.py
# dmgr run bin/wsadmin{EXT} -username user1 -password security -lang jython -f bin/enableTLSV2.py
# // optional run the sync node - this will stop all nodeagents and servers
# // sync_node dmgr
# END OF THE BATCH FILE - Do not include this line

#### NOW RUN THIS:
# run this command: cfg -cfg < your config file > batch enableTSLV2.batch
#


execfile('bin/wsadminlib.py')

print "Starting script..."

#--------------------------------------------------------------------
cellName = AdminControl.getCell()
# enable the TLS2 requirement for every SSL config in the env... UGH>
#productVersion=AdminTask.getNodeBaseProductVersion(['-nodeName', 'dmgr'])
#print "modifying WAS version: " + productVersion

# [1/7/16 10:49:07:747 EST] SSL certificate and key management > SSL configurations > CellDefaultSSLSettings > Quality of protection (QoP) settings
print "-- Setting SSL_TLSv2 for CellDefaultSSLSettings"
AdminTask.modifySSLConfig(['-alias', 'CellDefaultSSLSettings','-scopeName', '(cell):'+cellName,'-sslProtocol','SSL_TLSv2' ])
print "-- Setting SSL_TLSv2 for XDADefaultSSLSettings"
AdminTask.modifySSLConfig(['-alias', 'XDADefaultSSLSettings','-scopeName', '(cell):'+cellName,'-sslProtocol','SSL_TLSv2' ])
# get the list of nodes and loop on every one minus unmanaged nodes


nodes = _splitlines(AdminConfig.list( 'Node' ))
for node_id in nodes:
        nodename = getNodeName(node_id)
        managedNode=nodeHasServerOfType( nodename, 'NODE_AGENT' )
        dmgrNode=nodeHasServerOfType( nodename, 'DEPLOYMENT_MANAGER' ) 

        if( managedNode ):
		# [1/19/16 9:06:02:610 EST] SSL certificate and key management > SSL configurations > NodeDefaultSSLSettings > Quality of protection (QoP) settings
		print "-- Setting SSL_TLSv2 for node: " + nodename
		AdminTask.modifySSLConfig(['-alias', 'NodeDefaultSSLSettings', '-scopeName','(cell):'+cellName+':(node):'+nodename,'-sslProtocol', 'SSL_TLSv2' ]) 
        #endif
#endfor
print "--Saving...."
AdminConfig.save()
print "--completed..."
