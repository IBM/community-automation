# wsadminlib.py is needed
#https://github.com/wsadminlib/wsadminlib/blob/master/bin/wsadminlib.py
wsadminlib = "wsadminlib.py"
execfile(wsadminlib)
enableDebugMessages()
#---------------------------------------------
# Check/Print Usage
#---------------------------------------------

def printUsageAndExit (  ):
        print ("Usage: wsadmin -lang jython -f twas_cell_start_cluster.py cluster <cluster1>")
        print ("or:")
        print ("Usage: wsadmin -lang jython -f twas_cell_start_cluster.py cluster <cluster1> <cluster2>")
        sys.exit()
#endDef 

#---------------------------------------------
# Parse command line arguments
#---------------------------------------------

print ("Parsing command line arguments...")

clusterNamesList = []
if (len(sys.argv) < 2):
        printUsageAndExit( )
else:
        scope = sys.argv[0]
        print ("Scope:   "+scope)
        if (scope == "cluster"):
                clusterNamesList.append(sys.argv[1])
                print ("Cluster: "+clusterNamesList[0])
                if ( len(sys.argv) == 3 ):
                        clusterNamesList.append(sys.argv[2])
                        print ("Cluster: "+clusterNamesList[1])
        else:
                print ("Error: Invalid Argument ("+scope+")")
                printUsageAndExit( )
        #endElse 
#endElse 

for clusterName in clusterNamesList:
        startCluster( clusterName )
