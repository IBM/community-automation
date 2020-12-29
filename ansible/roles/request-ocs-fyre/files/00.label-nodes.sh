#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

CPUS=$(oc get node -o json | jq -r '.items[] | select(.metadata.labels["node-role.kubernetes.io/worker"] != null) | .status.capacity.cpu' | awk '{s+=$1} END {print s}')
echo "Total CPUs is $CPUS"
if [ $CPUS -lt 48 ]; then
  echo "OCS requires 48 cpus and your cluster only has ${CPUS}"
  echo "If the cluster uses machinesets you can scale up all machinesets using:"
  echo "   oc scale machinesets --replicas=3 -n openshift-machine-api --all"
  exit 1
fi

oc_nodes=$(oc get node -o name | grep worker)
nodes=$(oc get node -o name | grep worker | awk -F'/' '{print $2}')

echo "Labeling nodes for storage usage"
for node in $oc_nodes
do
    oc label $node cluster.ocs.openshift.io/openshift-storage=''
done
