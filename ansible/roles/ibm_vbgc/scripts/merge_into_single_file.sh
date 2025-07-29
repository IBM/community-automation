#!/usr/bin/env bash
# locate valid Liberty IBM and Oracle Jdk verbose gc files
find . -name verbosegc* > fileList.txt
find . -name verboseGC* >> fileList.txt
gcdir=""
prevgcdir=""

while read line
do
    # logic to concat all verbose* files 
    gcdir=$(dirname $line)
    if [ "$prevgcdir" != "$gcdir" ] ; then
        prevgcdir=$gcdir
        cd $gcdir
        # check to see if there are more than 1 gc file
        read countgc _ _ <<< $(ls -1 verbose* | wc)
        if [ "$countgc" -gt "1" ] ; then
            list=$(ls -1 verbose*)
            params=" "
            while read gcfile
                do
                params="${params} ${gcfile}"
            done <<< "$list"
            
            echo "creating verbosegc.$$.log using params: ${params}"
            
            time cat $params > verbosegc.$$.log
            rm -f $params 
        else # only 1 file rename it
            tmpbasename=$(basename $line)
            mv $tmpbasename verbosegc.$$.log
        fi

        cd -
    fi
done < fileList.txt # end while read
rm -f fileList.txt
	