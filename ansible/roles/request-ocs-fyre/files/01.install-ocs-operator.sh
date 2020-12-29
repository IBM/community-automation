#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

echo "Installing Openshift Container Storage Operator."

oc apply -f $my_dir/01.ocs-operator.yaml

if [ ! $? -eq 0 ]
then
    echo "There was an error installing Openshift Container Storage Operator."
    exit 1
fi

echo -n "Waiting for Openshift Container Storage Operator to be ready."
sleep 5

csv_name=$(oc get csv -n openshift-storage -o name | awk -F"/" '{print $2}')

COUNTER=60
STATUS=$(oc get csv $csv_name -n openshift-storage -o jsonpath={.status.phase})
while [[ "${STATUS}" != "Succeeded" ]]
do
    COUNTER=$(( ${COUNTER} -1 ))
    if [ "$COUNTER" -lt 1 ]
    then
        echo "Max retries reached, exiting..."
        exit 1
    fi
    sleep 10
    echo -n .
    STATUS=$(oc get csv $csv_name -n openshift-storage -o jsonpath={.status.phase})
    echo "$STATUS"
done
echo