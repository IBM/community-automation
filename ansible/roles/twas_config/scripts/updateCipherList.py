#--------------------------------------------------------------------
# WebSphere cipher adjustment
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f updateCipherList.py
# 2016-01-19 schader@us.ibm.com initial version
#--------------------------------------------------------------------
import sys
execfile('wsadminlib.py')

print "Starting updateCipherList.py script..."

#--------------------------------------------------------------------

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
            print "-- Setting custom cipher for CellDefaultSSLSettings"
            AdminTask.modifySSLConfig(['-alias', 'CellDefaultSSLSettings', '-scopeName','(cell):'+cellName,'-securityLevel','CUSTOM', '-enabledCiphers','SSL_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 SSL_ECDHE_RSA_WITH_AES_256_GCM_SHA384 SSL_ECDH_ECDSA_WITH_AES_256_GCM_SHA384 SSL_ECDH_RSA_WITH_AES_256_GCM_SHA384 TLS_AES_256_GCM_SHA384 TLS_AES_128_GCM_SHA256 TLS_CHACHA20_POLY1305_SHA256'])
            print "-- Setting custom cipher list for XDADefaultSSLSettings"
            AdminTask.modifySSLConfig(['-alias', 'XDADefaultSSLSettings', '-scopeName','(cell):'+cellName,'-securityLevel','CUSTOM', '-enabledCiphers','SSL_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 SSL_ECDHE_RSA_WITH_AES_256_GCM_SHA384 SSL_ECDH_ECDSA_WITH_AES_256_GCM_SHA384 SSL_ECDH_RSA_WITH_AES_256_GCM_SHA384 TLS_AES_256_GCM_SHA384 TLS_AES_128_GCM_SHA256 TLS_CHACHA20_POLY1305_SHA256'])
        #endif
        if( managedNode or appNode ):
            print "-- Setting custom cipher list for node: " + nodename
            AdminTask.modifySSLConfig(['-alias', 'NodeDefaultSSLSettings', '-scopeName','(cell):'+cellName+':(node):'+nodename,'-securityLevel','CUSTOM', '-enabledCiphers','SSL_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 SSL_ECDHE_RSA_WITH_AES_256_GCM_SHA384 SSL_ECDH_ECDSA_WITH_AES_256_GCM_SHA384 SSL_ECDH_RSA_WITH_AES_256_GCM_SHA384 TLS_AES_256_GCM_SHA384 TLS_AES_128_GCM_SHA256 TLS_CHACHA20_POLY1305_SHA256'])
        #endif
#endfor
print "--Saving...."
AdminConfig.save()
print "--completed..."

