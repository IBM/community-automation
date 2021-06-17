#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

echo "Installing Openshift Container Storage Operator."

oc get csv --no-headers=true -n openshift-storage | grep ocs-operator
if [[ $? -ne 0 ]]
then
    oc apply -f $my_dir/01.ocs-operator.yaml

    if [ ! $? -eq 0 ]
    then
        echo "There was an error installing Openshift Container Storage Operator."
        exit 1
    fi
fi


sleep 5
oc project openshift-storage
###
csv_counter=30
oc get csv --no-headers=true | grep ocs-operator
rc_csv=$?
echo -n "Checking for ocs operator csv "
while [[ $rc_csv -eq 1 ]]
do
    csv_counter=$(( ${csv_counter} -1 ))
    if [ "$csv_counter" -lt 1 ]
    then
        echo "Max retries reached for ocs operator csv check, exiting..."
        exit 1
    fi
    sleep 5
    oc get csv | grep ocs-operator
    rc_csv=$?
    echo -n .
done
echo
echo -n "Waiting for Openshift Container Storage Operator to be ready."
COUNTER=60
STATUS=$(oc get csv --no-headers=true | grep ocs-operator | rev | cut -f1 -d' ' | rev | tr -d ' ')
while [[ "${STATUS}" != "Succeeded" ]]
do
    COUNTER=$(( ${COUNTER} -1 ))
    if [ "$COUNTER" -lt 1 ]
    then
        echo "Max retries reached, exiting..."
        exit 1
    fi
    sleep 10
    STATUS=$(oc get csv --no-headers=true | grep ocs-operator | rev | cut -f1 -d' ' | rev | tr -d ' ')
    echo -n $STATUS
    echo -n .
done
echo
echo "OCS Operator Installed"
