# Ansible Role for installing Openshift Container Storage (OCS) using Local Storage OCP clusters.

## Overview

- This will automatically login to your cluster
- This role installs Openshift Container Storage (OCS) on OCP 4.6 or newer clusters.
- Works on X, P, and Z clusters
- To install OCS using `local storage` the OCP clusters require need the following min requirements.
  - Min of 3 worker nodes.
  - Total CPUs across all workers must total 48.
  - Each worker node must have 64G of memory.
  - Each workernode must have an `additional disk` on it (For example on fyre this is the /dev/vdb disk, on VMware it will be the /dev/sdb disk). The sum of all `additional disks` across all workers will be the total amount of OCS storage you will have available. Min amount across all workers is 500G.
- Dynamically installs the Local Storage operator found in the `OperatorHub` to create a base `localblock` storageclass, which uses the  `addtional disk` on each worker node, for OCS to use.
- Dynamically determines what OCP cluster version your on and automatically installs the correct OCS and Local Storage operator version on it.
- OCS creates the following 4 storageclass's
  - `ocs-storagecluster-ceph-rbd` - Block storage (RWX)
  - `ocs-storagecluster-ceph-rgw` - Bucket storage
  - `ocs-storagecluster-cephfs` - File storage (RWX)
  - `openshift-storage.noobaa.io` - object storage
- Sets `ocs-storagecluster-cephfs` as the default storageclass by default.

## Assumptions:

- Ansible 2.9 or later installed, with python3.

## Default parameters set in the defaults/main.yml

### Variables for specific user needs

- ocs_bastion_setup_dir: ~/setup-files/ocs-setup # Where scripts/templates are copied.
- setdefault: true  #Set parm defatul_sc as default storageclass when true
- default_sc: ocs-storagecluster-cephfs # Default Storageclass
- fyre_ui_build: false # true when cluster was built using the fyre website
- ocs_channel_prefix: "stable" # update if you need to use another channel
- ocs_channel_override: "" # used when you need to specify an override for the ocs channel.  (eg. using 4.9 OCS on OCP 4.10)

see [oc_login](https://github.com/IBM/community-automation/tree/master/ansible/roles/ocp_login) role

## Example Playbook use of role

see [request-ocs-fyre-play](https://github.com/IBM/community-automation/tree/master/ansible/request-ocs-fyre-play)
