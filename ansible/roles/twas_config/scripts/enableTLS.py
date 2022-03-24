#--------------------------------------------------------------------
# WebSphere TLS enablement
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f enableTLS.py
# 2016-01-19 schader@us.ibm.com initial version
#--------------------------------------------------------------------
import sys
execfile('wsadminlib.py')

print "Starting enableTLS.py script..."

#--------------------------------------------------------------------
if 1 <= len(sys.argv) < 2:
        sslProtocol = sys.argv[0]
else:
        print("script requires only 1 arg \n")
        print("[ SSL_TLSv2 | TLS | TLSv1.1 | TLSv1.2 | TLSv1.3 | SSL_TLS | SSL |SSLv2 | SSLv3 ]\n")
        sys.exit(101)
#endif

cellName = AdminControl.getCell()
# enable the TLS requirement for every SSL config in the env... UGH>
#productVersion=AdminTask.getNodeBaseProductVersion(['-nodeName', 'dmgr'])
#print "modifying WAS version: " + productVersion

# get the list of nodes and loop on every one minus unmanaged nodes
nodes = _splitlines(AdminConfig.list( 'Node' ))
for node_id in nodes:
        nodename = getNodeName(node_id)
        managedNode=nodeHasServerOfType( nodename, 'NODE_AGENT' )
        appNode=nodeHasServerOfType( nodename, 'APPLICATION_SERVER' )
        dmgrNode=nodeHasServerOfType( nodename, 'DEPLOYMENT_MANAGER' ) 

        if( dmgrNode ):
          # [1/7/16 10:49:07:747 EST] SSL certificate and key management > SSL configurations > CellDefaultSSLSettings > Quality of protection (QoP) settings
          print "-- Setting " + sslProtocol + " for CellDefaultSSLSettings"
          AdminTask.modifySSLConfig(['-alias', 'CellDefaultSSLSettings','-scopeName', '(cell):'+cellName,'-sslProtocol',sslProtocol ])
          print "-- Setting " + sslProtocol + " for XDADefaultSSLSettings"
          AdminTask.modifySSLConfig(['-alias', 'XDADefaultSSLSettings','-scopeName', '(cell):'+cellName,'-sslProtocol',sslProtocol ])
        #endif
        if( managedNode or appNode ):
		# [1/19/16 9:06:02:610 EST] SSL certificate and key management > SSL configurations > NodeDefaultSSLSettings > Quality of protection (QoP) settings
		print "-- Setting " + sslProtocol + " for node: " + nodename
		AdminTask.modifySSLConfig(['-alias', 'NodeDefaultSSLSettings', '-scopeName','(cell):'+cellName+':(node):'+nodename,'-sslProtocol', sslProtocol ]) 
        #endif
#endfor
print "--Saving...."
AdminConfig.save()
print "--completed..."
