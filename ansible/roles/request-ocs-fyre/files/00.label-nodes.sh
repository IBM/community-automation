#!/bin/bash

. ./config

WHOAMI=$(oc whoami)
if [[ $? > 0 ]]
then
    oc login -u $OC_USERNAME -p $OC_PASSWORD
    if [[ $? > 0 ]] 
    then
        echo "Unable to login to Openshift cluster with given credentials. Update config file with correct credentials."
        exit 1
    fi
fi

oc_nodes=$(oc get node -o name | grep worker)
nodes=$(oc get node -o name | grep worker | awk -F'/' '{print $2}')

echo "Labeling nodes for storage usage"
for node in $oc_nodes
do
    oc label $node cluster.ocs.openshift.io/openshift-storage=''
done

echo "Persistently enable container use of the Ceph file system in SELinux on all worker nodes."
for node in $nodes
do
    if ! grep $(ssh-keyscan -H $node | awk '{ if ($2=="ssh-rsa")  print $3 }') ~/.ssh/known_hosts > /dev/null 2>&1; then
        ssh-keyscan -H $node >> ~/.ssh/known_hosts
    fi
    ssh core@$node sudo setsebool -P container_use_cephfs on
done

