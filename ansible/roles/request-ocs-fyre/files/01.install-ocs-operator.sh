#!/bin/bash
my_dir=$(dirname $(readlink -f $0))
source $my_dir/config


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

echo "Installing Openshift Container Storage Operator."

oc apply -f ocs/01.ocs-operator.yaml

if [ ! $? -eq 0 ]
then
    echo "There was an error installing Openshift Container Storage Operator."
    exit 1
fi

echo -n "Waiting for Openshift Container Storage Operator to be ready."
sleep 5

csv_name=$(oc get csv -n openshift-storage -o name | awk -F"/" '{print $2}')

COUNTER=30
STATUS=$(oc get csv $csv_name -n openshift-storage -o jsonpath={.status.phase})
while [[ "${STATUS}" != "Succeeded" ]]
do
    COUNTER=$(( ${COUNTER} -1 ))
    if [ "$COUNTER" -lt 1 ]
    then
        echo "Max retries reached, exiting..."
        exit 1
    fi
    sleep 5
    echo -n .
    STATUS=$(oc get csv $csv_name -n openshift-storage -o jsonpath={.status.phase})
done
echo
