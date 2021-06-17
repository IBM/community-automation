#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

oc_nodes=$(oc get node | grep worker | cut -f1 -d' ')

echo "Labeling nodes for storage usage"
for node in $oc_nodes
do
    oc label --overwrite node/$node cluster.ocs.openshift.io/openshift-storage=''
done
