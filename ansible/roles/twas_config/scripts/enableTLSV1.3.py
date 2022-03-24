#--------------------------------------------------------------------
# WebSphere TLS V1.3 enablement
# https://www.ibm.com/support/pages/node/6421519
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f enableTLSV1.3.py
# 2016-01-19 schader@us.ibm.com initial version
#--------------------------------------------------------------------

execfile('wsadminlib.py')

print "Starting script..."

#--------------------------------------------------------------------
cellName = AdminControl.getCell()
# enable the TLS2 requirement for every SSL config in the env... UGH>
#productVersion=AdminTask.getNodeBaseProductVersion(['-nodeName', 'dmgr'])
#print "modifying WAS version: " + productVersion

# [1/7/16 10:49:07:747 EST] SSL certificate and key management > SSL configurations > CellDefaultSSLSettings > Quality of protection (QoP) settings
print "-- Setting TLSv1.3 for CellDefaultSSLSettings"
AdminTask.modifySSLConfig(['-alias', 'CellDefaultSSLSettings','-scopeName', '(cell):'+cellName,'-sslProtocol','TLSv1.3' ])
print "-- Setting TLSv1.3 for XDADefaultSSLSettings"
AdminTask.modifySSLConfig(['-alias', 'XDADefaultSSLSettings','-scopeName', '(cell):'+cellName,'-sslProtocol','TLSv1.3' ])
# get the list of nodes and loop on every one minus unmanaged nodes


nodes = _splitlines(AdminConfig.list( 'Node' ))
for node_id in nodes:
        nodename = getNodeName(node_id)
        managedNode=nodeHasServerOfType( nodename, 'NODE_AGENT' )
        dmgrNode=nodeHasServerOfType( nodename, 'DEPLOYMENT_MANAGER' ) 

        if( managedNode ):
		# [1/19/16 9:06:02:610 EST] SSL certificate and key management > SSL configurations > NodeDefaultSSLSettings > Quality of protection (QoP) settings
		print "-- Setting TLSv1.3 for node: " + nodename
		AdminTask.modifySSLConfig(['-alias', 'NodeDefaultSSLSettings', '-scopeName','(cell):'+cellName+':(node):'+nodename,'-sslProtocol', 'TLSv1.3' ]) 
        #endif
#endfor
print "--Saving...."
AdminConfig.save()
print "--completed..."
