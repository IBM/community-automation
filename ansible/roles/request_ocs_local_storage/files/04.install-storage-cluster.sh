#!/bin/bash

my_dir=$(dirname $(readlink -f $0))

echo "Creating Storage Cluster."

oc apply -f $my_dir/04.storage-cluster.yaml

if [ ! $? -eq 0 ];
then
    echo "There was an error installing storage-cluster."
    exit 1
fi

# check if storage classes have been created
echo "Checking for noobaa Storage Class"
scCounter=0
rc=1
until [ $rc -eq 0 ]
do
  echo "Waiting for noobaa storageclass to come up $(date)"
  sleep 10
  ((scCounter ++))
  if [ $scCounter -eq 60 ]; then
   echo "noobaa storageclass never became available."
   exit 1
  fi
  oc get sc --no-headers | cut -f1 -d' ' | grep noobaa >/dev/null
  rc=$?
done

echo
echo "Openshift Container Storage Setup complete."
