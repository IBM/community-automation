#!/usr/bin/env bash
set -x
export DISPLAY=:1
IBM_GCMV=$1

find . -name verbosegc* > vbgcfiles.txt
while read line
do
    outputDir=$( dirname $line)
    mkdir -p $outputDir/IBM_GCMV
    t1="$(dirname $line)/gctmp"
    export JAVA_TOOL_OPTIONS="-Djava.io.tmpdir=$t1 -Dosgi.configuration.area=$t1 -Duser.home=$t1"
    echo 'debug' >> /tmp/gcmv.debug.out
    pwd >> /tmp/gcmv.debug.out
    ls -l >> /tmp/gcmv.debug.out
    $IBM_GCMV -data=$t1 -p gcmv.genheap.epf -f $line -o $outputDir/IBM_GCMV
    rm -rf $line $t1
done < vbgcfiles.txt
# purge the temp dir's for the GCMV
find . -name gcmemoryvisualizerhtmlDataset1 -type d | xargs rm -rf
set +x