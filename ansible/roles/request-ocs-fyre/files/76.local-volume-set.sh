#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

echo "Auto-discover Local Volumes."


nodes=$(oc get node -o name | grep worker | awk -F'/' '{print $2}')

echo "Labeling nodes for storage usage"
for node in $nodes
do
    echo "              - ${node}" >> $my_dir/76.local-volume-set.yaml
done

oc apply -f $my_dir/76.local-volume-set.yaml

if [ ! $? -eq 0 ]
then
    echo "There was an error installing Local Volumes."
    exit 1
fi

sleep 10

#Wait for diskmaker pods for each worker
NUM_WORKERS=$(oc get no --no-headers=true | grep  worker | awk -F'/' '{print $2}' | wc -l)
echo "Waiting for diskmaker pods to come up for all nodes "
COUNTER=60
PV_COUNT=$(oc get pv --no-headers=true | grep local-pv | grep Available | wc -l)
while [ ${PV_COUNT} -eq ${NUM_WORKERS} ]
do
    COUNTER=$(( ${COUNTER} -1 ))
    if [ "$COUNTER" -lt 1 ]
    then
        echo "Max retries reached, exiting..."
        exit 1
    fi
    sleep 5
    echo -n .
    PV_COUNT=$(oc get pv --no-headers=true | grep local-pv | grep Available | wc -l)
done
