#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

oc_nodes=$(oc get node -o name | grep worker)
nodes=$(oc get node -o name | grep worker | awk -F'/' '{print $2}')

echo "Labeling nodes for storage usage"
for node in $oc_nodes
do
    oc label $node cluster.ocs.openshift.io/openshift-storage=''
done
