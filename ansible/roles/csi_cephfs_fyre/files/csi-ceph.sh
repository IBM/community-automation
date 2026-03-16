#!/bin/bash
rookRelease=$1
device=$2
new_default_sc=$3
registry=$4
registry_user=$5
registry_pwd=$6

if [[ -n $registry ]]; then
  if [[ -z $registry_user || -z $registry_pwd ]]; then
    echo "If setting custom Docker registry authentication, then you must specify valid registry user and registry password arguments"
    exit 1
  fi
fi

# Install ceph
rm -rf rook
echo "Doing clone of rook release $rookRelease"
git clone https://github.com/rook/rook.git
if [[ $rookRelease != "master" ]]; then 
  cd rook
  rook_branch_version=$(echo $rookRelease | cut -f1 -d'-' | cut -f3 -d'.' --complement | sed 's/v//g')
  echo "For tag $rookRelease we are using branch release-$rook_branch_version"
  git checkout tags/$rookRelease -b release-$rook_branch_version
  cd ..
fi
# if rook-ceph is version 1.5, then need to create/apply crd
majorRelease=$(echo ${rookRelease:0:4})

rookPath="rook/cluster/examples/kubernetes/ceph"
[[ $(cut -d '.' -f2 <<< $majorRelease) -ge 8 ]] && rookPath=rook/deploy/examples || true
if [[ $majorRelease != "v1.4" ]]
then
  echo "Doing crds.yaml"
  oc create -f $rookPath/crds.yaml
  echo "crds.yaml exit $?"
else
  echo "No reason to apply crds.yaml as file may not exist"
fi
echo "Doing common.yaml"
oc create -f $rookPath/common.yaml
echo "common.yaml exit $?"

echo "Setting up Docker registry image pull secrets"
if [[ -z $registry ]]; then
  echo "Using unauthenticated Docker registry pulls. Skipping ServiceAccount patching"
else 
  echo "Creating image pull secret for $registry and patching rook-ceph ServiceAccounts"
  oc project rook-ceph
  oc create secret docker-registry dockerhub-secret --docker-server=$registry --docker-username=$registry_user --docker-password=$registry_pwd --docker-email=unused
  oc patch serviceaccount default -p '{"imagePullSecrets": [{"name": "dockerhub-secret"}]}' || true
  oc patch serviceaccount rook-ceph-system -p '{"imagePullSecrets": [{"name": "dockerhub-secret"}]}' || true
  oc patch serviceaccount rook-ceph-mgr -p '{"imagePullSecrets": [{"name": "dockerhub-secret"}]}' || true
  oc patch serviceaccount rook-ceph-osd -p '{"imagePullSecrets": [{"name": "dockerhub-secret"}]}' || true
  oc patch serviceaccount rook-ceph-cmd-reporter -p '{"imagePullSecrets": [{"name": "dockerhub-secret"}]}' || true
fi
echo "setup Docker registry image pull secrets exit"

echo "Doing operator-openshift.yaml"
cat $rookPath/operator-openshift.yaml | sed 's#image: rook/ceph#image: docker-na-public.artifactory.swg-devops.com/sec-guardium-next-gen-dockerhub-docker-remote/rook/ceph#'  | kubectl apply -f -
oc create -f /tmp/operator-openshift.yaml 
echo "operator-openshift.yaml exit $?"
sleep_count=30
while [[ $sleep_count -gt 0 ]]; do
  oc  get po -n rook-ceph | grep  -e  rook-ceph-operator | tr -s ' ' | grep Running
  if [ $? -ne 0 ] ; then
    echo "Waiting for ceph operator to go to Running"
    sleep 1m
    ((sleep_count--))
  else
    echo "ceph operator Running"
    break
  fi
done
echo "Doing sed of useAllDevices false"
sed -i 's/useAllDevices: true/useAllDevices: false/g' $rookPath/cluster.yaml
echo "Exit from useAllDevice $?"
echo "Doing sed of deviceFilter"
sed -i 's/#deviceFilter:/deviceFilter: ^vd[b-z]$/g' $rookPath/cluster.yaml
echo "Exit from deviceFilter $?"
echo "Doing cluster.yaml create"
cat $rookPath/cluster.yaml | sed 's#image: ceph/ceph#image: docker-na-public.artifactory.swg-devops.com/sec-guardium-next-gen-dockerhub-docker-remote/ceph/ceph#' | kubectl apply -f -
oc create -f /tmp/cluster.yaml
echo "Exit from cluster.yaml $?"

num_worker_nodes=$(oc get no | tr -s ' ' | cut -f3 -d' ' | grep worker  | wc -l)
echo "Check for the number of ceph nodes running is equal to numbers of worker nodes - wait up to 2 hour"
ceph_sleep_count=60
while [[ $ceph_sleep_count -ne 0 ]]; do
  num_ceph_nodes=$(oc get po -n rook-ceph | grep rook-ceph-osd | grep -v prepare | grep -e Running | wc -l)
  if [[ $num_ceph_nodes -ge $num_worker_nodes ]] ; then
    echo "Waiting for ceph nodes to come active"
    sleep 1m
    ((ceph_sleep_count--))
    echo "ceph_sleep_count = $ceph_sleep_count"
  else
    echo "ceph nodes are active."
    break
  fi
done
echo "Doing filessystem-test.yaml"
oc create -f $rookPath/filesystem-test.yaml
echo "Exit from filesystem-test.yaml $?"
oc create -f $rookPath/csi/cephfs/storageclass.yaml
sed -i "s/rook-cephfs/csi-cephfs/g" $rookPath/csi/cephfs/storageclass.yaml
oc create -f $rookPath/csi/cephfs/storageclass.yaml
default_storage_class=$(oc get sc  | grep -e default | cut -f1 -d' ' | tr -s ' ')
echo "default_storage_class is $default_storage_class"
if [[ -z $default_storage_class ]]; then
  echo "No default storage class defined"
else
  echo "Set storageclass $default_storage_class to not be default"
  oc patch storageclass $default_storage_class -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
fi
echo "Set default storageclass to $new_default_sc"
oc patch storageclass $new_default_sc -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
oc create -f $rookPath/csi/rbd/storageclass-test.yaml
