#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

echo "Auto-discover Local Volumes."

nodes=$(oc get node -o name | grep worker | awk -F'/' '{print $2}')

echo "Labeling nodes for storage usage"
for node in $nodes
do
    echo "              - ${node}" >> $my_dir/76.local-volumes-discovery.yaml
done

oc create -f $my_dir/76.local-volumes-discovery.yaml

if [ ! $? -eq 0 ]
then
    echo "There was an error installing Local Volumes."
    exit 1
fi

sleep 10

#Wait for diskmaker pods for each worker
NUM_WORKERS=$(oc get no --no-headers=true | grep  worker | awk -F'/' '{print $2}' | wc -l)
echo "Waiting for diskmaker pods to come up for all nodes "
oc project openshift-local-storage
COUNTER=60
POD_COUNT=$(oc get pod --no-headers=true | grep diskmaker | grep Running | wc -l)
while [ ${POD_COUNT} -eq ${NUM_WORKERS} ]
do
    COUNTER=$(( ${COUNTER} -1 ))
    if [ "$COUNTER" -lt 1 ]
    then
        echo "Max retries reached, exiting..."
        exit 1
    fi
    sleep 5
    echo -n .
    POD_COUNT=$(oc get pod --no-headers=true | grep diskmaker | grep Running | wc -l)
done
