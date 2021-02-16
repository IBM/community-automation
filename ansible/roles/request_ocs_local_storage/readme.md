# Ansible Role for installing Openshift Container Storage (OCS) using Local Storage OCP clusters.

## Overview

- This role installs Openshift Container Storage (OCS) on OCP 4.4, 4.5 and 4.6 or newer clusters (`Takes between 8 and 10 minutes`).
- To install OCS using `local storage` the OCP clusters require need the following min requirements.
  - Min of 3 worker nodes.
  - Total CPUs across all workers must total 48 CPUs. For example if you have only three worker nodes then you require each worker to have 16 CPUs each. If you have 6 worker nodes then each worker needs of min of 8 CPUs.
  - Each worker node must have 64G of memory.
  - Each workernode must have an `additional disk` on it (For example on fyre this is the /dev/vdb disk, on VMware it will be the /dev/sdb disk). The sum of all `additional disks` across all workers will be the total amount of OCS storage you will have available. Min amount across all workers is 500G.
    - Example, you have 3 workers with `additional disks` of 500G then you have total OCS storage of 1.5T.
- Dynamically installs the Local Storage operator found in the `OperatorHub` to create a base `localblock` storageclass, which uses the  `addtional disk` on each worker node, for OCS to use.
- Dynamically determines what OCP cluster version your on and automatically installs the correct OCS and Local Storage operator version on it.
  - On OCP 4.4 and 4.5 clusters it will install and run the `stable-4.5` OCS operator and the `4.5` Local Storage operator found in the `OperatorHub` catalog.
  - Currently, on any cluster greater or equal to OCP 4.6, it will install OCS `stable-4.6` (current latest version of OCS) and Local Storage operator `4.6`. When a newer OCS version comes out then this code will need updating.
- OCS creates the following 4 storageclass's
  - `ocs-storagecluster-ceph-rbd` - Block storage (RWX)
  - `ocs-storagecluster-ceph-rgw` - Bucket storage
  - `ocs-storagecluster-cephfs` - File storage (RWX)
  - `openshift-storage.noobaa.io` - Object storage
- Sets `ocs-storagecluster-cephfs` as the default storageclass by default.

## Assumptions:

 - Ansible 2.9 or later installed, with python3.

## Default parameters set in the defaults/main.yml

### Variables for specific user needs
 - ocs_bastion_setup_dir: ~/setup-files/ocs-setup # Where scripts/templates are copied.
 - setdefault: true  #Set parm defatul_sc as default storageclass when true
 - default_sc: ocs-storagecluster-cephfs # Default Storageclass
### Do not change the following ... dynamically changed to 4.6 values when "oc version" is 4.6 or greater
 - local_storage_namespace: local-storage
 - device_set: ocs-deviceset
 - localstore_version: 4.5
 - ocs_channel: stable-4.5
### Change to the additional definition for your cluster type. Only used for OCP 4.5 or 4.4 clusters when OCS 4.5 is installed. Not used for OCP 4.6 clusters when OCS 4.6 is installed.
 - ocs_device: /dev/vdb # First additional disk drive definition. Currently setup for a fyre additional disk. 

## Example Playbook use of role
----------------

    - name: Install OCS fyre
      hosts: bastion
      roles:
      - request_ocs_local_storage
