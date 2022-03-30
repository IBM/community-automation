#--------------------------------------------------------------------
# WebSphere updateWebContainerThreadPools.py 
#--------------------------------------------------------------------
#
#
# To invoke the script, type:
#   wsadmin -f updateWebContainerThreadPools.py min max
#--------------------------------------------------------------------
# 
execfile('wsadminlib.py')

print "Starting update updateWebContainerThreadPools.py"

#--------------------------------------------------------------------
if len(sys.argv) == 2:
        minWebPool = sys.argv[0]
        maxWebPool = sys.argv[1]
else:
        print("script requires only 2 args\n")
        print(" minWebPool maxWebPool \n")
        sys.exit(101)
#endif
cellName = AdminControl.getCell()
# get the list of servers and loop on every one minus webservers
for (nodename,servername) in listServersOfType(None):
    stype = getServerType(nodename,servername)
    if stype == 'APPLICATION_SERVER':
        server = AdminConfig.getid("/Server:"+servername+"/" )
        tpList = AdminConfig.list("ThreadPool", server )
        webPool = ""
        for pool in tpList.split("\n"):
            pool = pool.rstrip()
            if (getNameFromId(pool) == "WebContainer"):
                webPool = pool
                break
                #endIf
        #endFor
        attrs = [["maximumSize", maxWebPool], ["minimumSize", minWebPool]]
        print ("-- Updating %s web container...%s %s " % (servername, minWebPool, maxWebPool))
        AdminConfig.modify(webPool, attrs )
#endfor
print "--Saving...."
AdminConfig.save()
print "--completed..."


