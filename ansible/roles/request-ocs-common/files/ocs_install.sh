#!/bin/bash

ocsChannel=$1
setDefault=$2
# Check the worker nodes have enough cpus
CPUS=$(kubectl get node -o json | jq -r '.items[] | select(.metadata.labels["node-role.kubernetes.io/worker"] != null) | .status.capacity.cpu' | awk '{s+=$1} END {print s}')
if [ $CPUS -lt 48 ]; then
  echo "OCS requires 48 cpus and your cluster only has ${CPUS}"
  echo "If the cluster uses machinesets you can scale up all machinesets using:"
  echo "   oc scale machinesets --replicas=3 -n openshift-machine-api --all"
  exit 1
fi

# Create namespace
echo 'Create namespace and label'
export namespc=openshift-storage
cat << EOF | oc apply -f -
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
  name: ${namespc}
spec: {}
EOF

# Create the OperatorGroup
echo "Creating the operator group"
cat << EOF | oc -n ${namespc} apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-storage-operatorgroup
  namespace: ${namespc}
spec:
  serviceAccount:
    metadata:
      creationTimestamp: null
  targetNamespaces:
  - ${namespc}
EOF

# Create the Subscription object
echo "Creating the Subscription Object"
cat << EOF | oc -n ${namespc} apply -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-storage-operatorgroup
  namespace: ${namespc}
spec:
  channel: ${ocsChannel}
  installPlanApproval: Automatic
  name: ocs-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF


counter=0
until [ "$(oc get ClusterServiceVersion -n ${namespc} -o json | jq -r '.items[] | select(.spec.displayName=="OpenShift Container Storage") | .metadata.name')" != "" ]
do
  echo "Waiting for CSV to be created: ${date}"
  oc get ClusterServiceVersion -n ${namespc}
  sleep 2
  ((counter ++))
  if [ $counter -eq 180 ]; then
   exit 1
  fi
done
csvname=$(oc get ClusterServiceVersion -n ${namespc} -o json | jq -r '.items[] | select(.spec.displayName=="OpenShift Container Storage") | .metadata.name')
echo "csvname=${csvname}"

counter=0
until [ "$(oc get ClusterServiceVersion -n ${namespc} ${csvname} --no-headers -o=custom-columns=LABEL:.status.phase)" == "Succeeded" ]
do
  echo "Waiting for CSV to succeed: $(date)"
  oc get ClusterServiceVersion -n ${namespc} ${csvname}
  sleep 10
  ((counter ++))
  if [ $counter -eq 180 ]; then
   exit 1
  fi
done
oc get ClusterServiceVersion -n ${namespc} ${csvname}

opCounter=0
until [ $( oc -n ${namespc} get deployment ocs-operator --no-headers -o=custom-columns=LABEL:.status.readyReplicas) -ge 1 ]
do
  echo "Waiting for OCS Operator pod to come up: $(date)"
  oc -n ${namespc} get deployment ocs-operator
  sleep 10
  ((opCounter ++))
  if [ $opCounter -eq 60 ]; then
   exit 1
  fi
done
oc -n ${namespc} get deployment ocs-operator

# nCounter=0
# until [ $( oc -n ${namespc} get deployment noobaa-operator --no-headers -o=custom-columns=LABEL:.status.readyReplicas) -ge 1 ]
# do
#   echo "Waiting for Nooba Operator pod to come up: $(date)"
#   sleep 10
#   ((nCounter ++))
#   if [ $nCounter -eq 60 ]; then
#    exit 1
#   fi
# done

# rCounter=0
# until [ $( oc -n ${namespc} get deployment rook-ceph-operator --no-headers -o=custom-columns=LABEL:.status.readyReplicas) -ge 1 ]
# do
#   echo "Waiting for Nooba Operator pod to come up: $(date)"
#   sleep 10
#   ((rCounter ++))
#   if [ $rCounter -eq 60 ]; then
#    exit 1
#   fi
# done

# labeling nodes with label cluster.ocs.openshift.io/openshift-storage= for storage pods to run
echo "labeling worker nodes"
oc label node --selector='!node-role.kubernetes.io/master' cluster.ocs.openshift.io/openshift-storage=""

echo "get the default storageclass to base the OCS on"
sClass=$(oc get sc -o json | jq -r '.items[].metadata | select(.annotations["storageclass.kubernetes.io/is-default-class"] == "true") | .name')

cat << EOF | oc -n ${namespc} apply -f -
apiVersion: ocs.openshift.io/v1
kind: StorageCluster
metadata:
  name: ocs-storagecluster
  namespace: ${namespc}
spec:
  manageNodes: false
  storageDeviceSets:
  - count: 1
    dataPVCTemplate:
      spec:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 2Ti
        storageClassName: ${sClass}
        volumeMode: Block
    name: ocs-deviceset
    placement: {}
    portable: true
    replica: 3
    resources: {}
EOF

# check if storage classes have been created
echo "checking for Storage Classes"
scCounter=0
until [ $( oc get sc | grep openshift | wc -l) -ge 3 ]
do
  echo "Waiting for storage classes to come up: $(date)"
  oc get sc
  sleep 10
  ((scCounter ++))
  if [ $scCounter -eq 60 ]; then
   exit 1
  fi
done
oc get sc
echo "setDefault = $setDefault"
if [ "$setDefault" == "true" ]; then
   defStgClass=$(oc get sc -o json | jq -r '.items[].metadata | select(.annotations["storageclass.kubernetes.io/is-default-class"] == "true") | .name')
   oc patch storageclass $defStgClass -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
   oc patch storageclass ocs-storagecluster-cephfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
   oc get sc
fi
