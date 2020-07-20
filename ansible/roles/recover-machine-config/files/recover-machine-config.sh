#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

# example: rendered-master-49cf574b7d19fc505c33440b19464d2b
machine_config=$1

NODES=$(oc get nodes -l node-role.kubernetes.io/master="" -o name)
for NODE in $NODES; do 
  oc debug $NODE -- chroot /host touch /run/machine-config-daemon-force; 
done

for NODE in $NODES; do 
  oc patch $NODE -p '{"metadata": {"annotations": {"machineconfiguration.openshift.io/currentConfig": "'$machine_config'"}}}';
done
