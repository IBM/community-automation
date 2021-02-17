#!/bin/bash
rookRelease=$1
device=$2
oc login -u kubeadmin -p "$(cat /root/auth/kubeadmin-password)" https://api.$(hostname | cut -f1 -d'.' | rev | cut -f1 -d'-' --complement | rev).cp.fyre.ibm.com:6443 --insecure-skip-tls-verify=true

# Install ceph
rm -rf rook
echo "Doing clone of rook release $rookRelease"
git clone https://github.com/rook/rook.git -b $rookRelease
# if rook-ceph is version 1.5, then need to create/apply crd
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
echo "Doing sed of useAllDevices false"
sed -i 's/useAllDevices: true/useAllDevices: false/g' rook/cluster/examples/kubernetes/ceph/cluster.yaml
echo "Exit from useAllDevice $?"
echo "Doing sed of deviceFilter"
sed -i "s/#deviceFilter:/deviceFilter: $device/g" rook/cluster/examples/kubernetes/ceph/cluster.yaml
echo "Exit from deviceFilter $?"
echo "Doing cluster.yaml create"
oc create -f rook/cluster/examples/kubernetes/ceph/cluster.yaml
echo "Exit from cluster.yaml $?"
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
echo "Set default storageclass to csi-cephfs"
oc patch storageclass csi-cephfs -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
oc create -f rook/cluster/examples/kubernetes/ceph/csi/rbd/storageclass-test.yaml
