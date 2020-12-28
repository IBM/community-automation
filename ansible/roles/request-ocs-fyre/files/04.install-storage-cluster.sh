#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

echo "Creating Storage Cluster."

oc apply -f $my_dir/04.storage-cluster.yaml

if [ ! $? -eq 0 ]
then
    echo "There was an error installing Local Volumes."
    exit 1
fi

echo -n "Waiting for RBD storage class creation."

sleep 5

COUNTER=30
SC=$(oc get sc ocs-storagecluster-ceph-rbd -o name 2> /dev/null)
while [[ $SC != "storageclass.storage.k8s.io/ocs-storagecluster-ceph-rbd" ]]
do
    COUNTER=$(( ${COUNTER} -1 ))
    if [ "$COUNTER" -lt 1 ]
    then
        echo "Max retries reached, exiting..."
        exit 1
    fi
    sleep 5
    echo -n .
    SC=$(oc get sc ocs-storagecluster-ceph-rbd -o name 2> /dev/null)
done

echo "Setting ocs-storagecluster-ceph-rbd storage class as default"

oc patch sc ocs-storagecluster-ceph-rbd -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

echo -n "Waiting for pods in openshift-storage project."

COUNTER=100
POD_COUNT=$(oc get pod -n openshift-storage | egrep -v '1/1|2/2|3/3|4/4|5/5|6/6|Completed|NAME' | wc -l)
while [ ${POD_COUNT} -gt 0 ]
do
    COUNTER=$(( ${COUNTER} -1 ))
    if [ "$COUNTER" -lt 1 ]
    then
        echo "Max retries reached, exiting..."
        exit 1
    fi
    sleep 5
    echo -n .
    POD_COUNT=$(oc get pod -n openshift-storage | egrep -v '1/1|2/2|3/3|4/4|5/5|6/6|Completed|NAME' | wc -l)
done
echo
echo "Openshift Container Storage Setup complete."
