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

cp $my_dir/ocs/03.local-volumes.yaml ${TMPFILE}

for device in $DEVICES
do
    echo "        - ${device}" >> ${TMPFILE}
done

echo "Creating Local Volumes."

oc apply -f ${TMPFILE}

if [ ! $? -eq 0 ]
then
    echo "There was an error installing Local Volumes."
    exit 1
fi

rm -f ${TMPFILE}

echo -n "Waiting for Local Volumes to be created."
sleep 10

COUNTER=30
POD_COUNT=$(oc get pod -n local-storage | egrep -v '1/1|2/2|3/3|4/4|5/5|6/6|Completed|NAME' | wc -l)
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
    POD_COUNT=$(oc get pod -n local-storage | egrep -v '1/1|2/2|3/3|4/4|5/5|6/6|Completed|NAME' | wc -l)
done

COUNTER=30
SC=$(oc get sc localblock -o name 2> /dev/null)
while [[ $SC != "storageclass.storage.k8s.io/localblock" ]]
do
    COUNTER=$(( ${COUNTER} -1 ))
    if [ "$COUNTER" -lt 1 ]
    then
        echo "Max retries reached, exiting..."
        exit 1
    fi
    sleep 5
    echo -n .
    SC=$(oc get sc localblock -o name 2> /dev/null)
done
echo
echo "Local Volumes created"
