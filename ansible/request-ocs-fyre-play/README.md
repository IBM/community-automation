# Ansible Playbook for installing Openshift Container Storage (OCS) onto Fyre OCP+ clusters and Quickburn large clusters.

## Overview

- Installs Openshift Container Storage (OCS) on fyre 4.4, 4.5 and 4.6 or newer clusters (`Takes between 8 and 10 minutes`).
  - Install using the `fyre inf` node. Copy to current folder from the examples folder the `inventory_remote_inf_node` and  rename to inventory.
    - Ansible will use the oc already installed on the `inf` node and push all the scripts and templates to the `inf` node for running. You only need your fyre root user PW to use.
  - Install using a `local ubuntu VM` using `oc login`. To run oc login locally on an ubuntu VM to your fyre cluster, copy from examples to current dir the `inventory_local`, renaming to `inventory`. Ansible will run scripts locally on the `ubuntu VM` and use the `oc` on the ubuntu VM.
- To install OCS on Fyre `bare metal` clusters requires clusters with follow min requirements.
  - Min of 3 worker nodes.
  - Total CPUs across all workers must total 48 CPUs. For example if you have only three worker nodes then you require each worker to have 16 CPUs each. If you have 6 worker nodes then each worker needs of min of 8 CPUs.
  - Each worker should have 64G of memory, but 32G will allow you to do a min install.
  - Each worker must have an `additional disk` on it (/dev/vdb disk). The sum of all `additional disks` across all workers will be the total amount of OCS storage you will have available. Min amount across all workers is 200G.
    - Example, you have 3 workers with `additional disks` of 500G then you have total OCS storage of 1.5T.
- To create Fyre clusters with the resources needed for OCS, use one of the following methods.
  - Use the fyre.ibm.com GUI OCP+ cluster option with large size selected. This is the smallest cluster you can use with OCS on it.
  - Use the Fyre API to create an OCP+ cluster. See example of API use in the examples folder, `example_fyre_api`.
  - Create an OCP+ cluster using the Ansible play in this repo called `request-ocp-fyre-play`. Use from the example folder the  `ocp_vars_example.yaml` to modify the size of the cluster.
  - From fyre.ibm.com use the Quickburn large cluster support. Use the additon of `-e quickburn=true` to the ansible play call.  
- Dynamically installs the Local Storage operator found in the `OperatorHub` to create a base `localblock` storageclass, which uses the /dev/vdb `addtional disk` on each worker node, for OCS to use.
- Dynamically determines what OCP cluster version your on and automatically installs the correct OCS and Local Storage operator version on it.
  - On OCP 4.4 and 4.5 clusters it will install and run the `stable-4.5` OCS operator and the `4.5` Local Storage operator found in the `OperatorHub` catalog.
  - Currently, on any cluster greater or equal to OCP 4.6, it will install OCS `stable-4.6` (current latest version of OCS) and Local Storage operator `4.6`. When a newer OCS version comes out then this code will need updating.

- OCS creates the following 4 storageclass's
  - `ocs-storagecluster-ceph-rbd` - Block storage (RWX)
  - `ocs-storagecluster-ceph-rgw` - Bucket storage
  - `ocs-storagecluster-cephfs` - File storage (RWX)
  - `openshift-storage.noobaa.io` - Object storage
- Sets `ocs-storagecluster-cephfs` as the default storageclass, but will check first for any current default sc and make it not the default. This is configurable, change the `examples/ocs_install_vars.yaml` file and move to current dir if you want something different, or change the variable in the run of the playbook per the example below.

## Assumptions:

 - Ansible 2.9 or later installed, with python3.
 - A healthy Fyre OCP+ OpenShift 4.4 or newer cluster in running state.
  - Min 3 worker nodes with /dev/vdb additional storage, 16 CPS and 64G mem.
 - oc client installed and oc login done to OCP cluster, if running local using `examples/inventory_local` on ubuntu VM.
 - Fyre root user password, if running remote mode using `examples/inventory_remote_inf_node`, on cluster `inf` node.

## How to install oc client

  - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
  - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
  - Extract: tar xf oc.tar.gz
  - Move to /usr/local/bin: cp oc /usr/local/bin
  - Example oc login: `oc login https://api.ocp446ocs.cp.fyre.ibm.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`

## Run playbook

Once you have configured the `inventory` file, or done a `oc login`, run the playbook using:

```
ansible-playbook  -i inventory request-ocs-fyre.yml
```
or pass parameters (This example sets storageclass `ocs-storagecluster-ceph-rbd` as the default storageclass)

```
ansible-playbook  -i inventory request-ocs-fyre.yml -e "default_sc=ocs-storagecluster-ceph-rbd"
```

Playbook run example for `Quickburn` clusters
```
ansible-playbook  -i inventory request-ocs-fyre.yml -e "quickburn=true"
```

Playbook run example if using ocs_install_vars.yaml
```
ansible-playbook  -i inventory -e @ocs_install_vars.yml request-ocs-fyre.yml
```
License
-------

See LICENCE.txt
