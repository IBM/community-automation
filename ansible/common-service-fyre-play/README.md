# Ansible Playbook for Fyre OCP+Beta Cluster Common Services Installation

## Overview

- Installs `csi-cephfs` storage on worker nodes using the /dev/vdb drive on each worker node.
  - Creates file storage (rwo/rwx)  storageclass called `csi-cephfs` as the default storageclass.
  - Creates block storageclass (rwo/rwx) `rook-ceph-block`
- Installs `common-services` latest GA by default.

## Assumptions:

 - A healthy Fyre OCP+Beta OpenShift 4.4.6 or later cluster in running state.
 - oc login has been completed to fyre cluster.
 - Running on Ubuntu or Mac.


## How to install oc client

  - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
  - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
  - Extract: tar xf oc.tar.gz
  - Move to /usr/local/bin: cp oc /usr/lcoal/bring
  - Example oc login: `oc login https://api.dev_fyre.cp.fyre.ibm.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`


## Setting up inventory

Make use of sample file at `examples/inventory` (with no changes).

```
cp examples/inventory .
```

## Run playbook

#### Setting up variables for playbook

Make use of the sample file at `examples/cs_vars_fyre.yml`. Modify the values as per your cluster. For more information refer to comments in the file.

```
cp examples/cs_vars_fyre.yml .
```

Once you have configured the vars & inventory file, run the playbook using:

```
ansible-playbook  -i inventory -e @cs_vars_fyre.yml common-services-fyre.yml
```

License
-------

See LICENCE.txt
