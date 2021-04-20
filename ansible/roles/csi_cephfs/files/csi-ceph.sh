#!/bin/bash
rookRelease=$1
device=$2
new_default_sc=$3

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
sleep 3m
majorRelease=$(echo ${rookRelease:0:4})
if [[ $majorRelease != "v1.4" ]]
then
  echo "Doing crds.yaml"
  oc create -f rook/cluster/examples/kubernetes/ceph/crds.yaml
  echo "crds.yaml exit $?"
else
  echo "No reason to apply crds.yaml as file may not exist"
fi
echo "Doing common.yaml"
oc create -f rook/cluster/examples/kubernetes/ceph/common.yaml
echo "common.yaml exit $?"
echo "Doing operator-openshift.yaml"
oc create -f rook/cluster/examples/kubernetes/ceph/operator-openshift.yaml
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
sed -i 's/useAllDevices: true/useAllDevices: false/g' rook/cluster/examples/kubernetes/ceph/cluster.yaml
echo "Exit from useAllDevice $?"
echo "Doing sed of deviceFilter"
sed -i "s/#deviceFilter:/deviceFilter: $device/g" rook/cluster/examples/kubernetes/ceph/cluster.yaml
echo "Exit from deviceFilter $?"
echo "Doing cluster.yaml create"
oc create -f rook/cluster/examples/kubernetes/ceph/cluster.yaml
echo "Exit from cluster.yaml $?"

num_worker_nodes=$(oc get no | tr -s ' ' | cut -f3 -d' ' | grep worker  | wc -l)
echo "Check for the number of ceph nodes running is equal to numbers of worker nodes - wait up to 1 hour"
ceph_sleep_count=60
while [[ $ceph_sleep_count -ne 0 ]]; do
  num_ceph_nodes=$(oc get po -n rook-ceph | grep rook-ceph-osd | grep -v prepare | grep -e Running | wc -l)
  if [[ $num_worker_nodes -ne $num_ceph_nodes ]] ; then
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
oc create -f rook/cluster/examples/kubernetes/ceph/filesystem-test.yaml
echo "Exit from filesystem-test.yaml $?"
oc create -f rook/cluster/examples/kubernetes/ceph/csi/cephfs/storageclass.yaml
sed -i "s/rook-cephfs/csi-cephfs/g" rook/cluster/examples/kubernetes/ceph/csi/cephfs/storageclass.yaml
oc create -f rook/cluster/examples/kubernetes/ceph/csi/cephfs/storageclass.yaml
default_storage_class=$(oc get sc  | grep -e default | cut -f1 -d' ' | tr -s ' ')
echo "default_storage_class is $default_storage_class"
if [[ -z $default_storage_class ]]; then
  echo "No default storage class defined"
else
  echo "Set storageclass $default_storage_class to not be default"
  oc patch storageclass $default_storage_class -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
fi
echo "Set default storageclass to $new_default_cs"
oc patch storageclass $new_default_sc -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
oc create -f rook/cluster/examples/kubernetes/ceph/csi/rbd/storageclass-test.yaml
