#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

echo "Auto-discover Local Volumes."

nodes=$(oc get node | grep worker | cut -f1 -d' ')

echo "Adding nodes to local-volumes-discovery yaml"
for node in $nodes
do
    echo "              - ${node}" >> $my_dir/46.local-volumes-discovery.yaml
done

oc apply -f $my_dir/46.local-volumes-discovery.yaml

if [ ! $? -eq 0 ]
then
    echo "There was an error installing Local Volumes Discovery."
    exit 1
fi

sleep 10

#Wait for diskmaker pods for each worker
NUM_WORKERS=$(oc get no --no-headers=true | grep  worker | awk -F'/' '{print $2}' | wc -l)

oc project openshift-local-storage
echo -n "Waiting for diskmaker-discovery pods to come up for all worker nodes "
COUNTER=60
POD_COUNT=$(oc get pod --no-headers=true | grep diskmaker-discovery | grep Running | wc -l)
while [[ $POD_COUNT -ne $NUM_WORKERS ]]
do
    COUNTER=$(( ${COUNTER} -1 ))
    if [ "$COUNTER" -lt 1 ]
    then
        echo "Max retries checking for Local Volumes Discovery diskmaker pod reached, exiting..."
        exit 1
    fi
    sleep 5
    echo -n .
    POD_COUNT=$(oc get pod --no-headers=true | grep diskmaker-discovery | grep Running | wc -l)
done
echo
echo "Local Volume Discovery Completed"
