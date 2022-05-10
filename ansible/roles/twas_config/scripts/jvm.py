#--------------------------------------------------------------------
# WebSphere Penetration testing jvm props
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f jvm.py initialHeap maxHeap
#--------------------------------------------------------------------
# 
execfile('wsadminlib.py')

print "Starting enable Pen test jvm props script..."

#--------------------------------------------------------------------
if len(sys.argv) == 2:
        initialHeap = sys.argv[0]
        maxHeap = sys.argv[1]
else:
        print("script requires only 2 args\n")
        print(" initialHeap maxHeap \n")
        sys.exit(101)
#endif
cellName = AdminControl.getCell()
# get the list of servers and loop on every one minus webservers
for (nodename,servername) in listServersOfType(None):
    stype = getServerType(nodename,servername)
    if stype == 'APPLICATION_SERVER':
        print("-- set JVM initial heap: " + initialHeap)
        setJvmProperty(nodename,servername,'initialHeapSize',initialHeap)
        print("-- set JVM Max heap: " + maxHeap)
        setJvmProperty(nodename,servername,'maximumHeapSize',maxHeap)

#endfor
print "--Saving...."
AdminConfig.save()
print "--completed..."

