request_ocs_local_storage
=======

Ansible Role for installing Openshift Container Storage (OCS) using Local Storage OCP clusters.

---------

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

Requirements
---------

- Ansible 2.9 or later installed, with python3.
- worker nodes must have equal number of extra drives

Role Variables
------------

Default parameters set in the defaults/main.yml

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| ocs_bastion_setup_dir   | yes       | ~/setup-files/ocs-setup   |               |                          |
| setdefault              | yes      | true        |                  |                          |
| default_sc              | yes      |  ocs-storagecluster-cephfs       |                  |                          |
| local_storage_namespace | yes     | openshift-local-storage | string | | 
| fyre_ui_build          | yes      |  false       | true, false                  |  cluster was built using the fyre web UI      |
| ocs_channel_prefix     | yes      |  stable       | stable, fast, candidate       |  cluster was built using the fyre web UI      |
| ocs_channel            | yes | stable-4.6 | | | 
| ocs_channel_override    | yes      |  empty       |       |  used when you need to override the version of OCS      |
| ocs_type               | yes      |  ocs       | odf, ocs       |        |
| device_set               | yes      |   ocs-deviceset-localblock      |        |        |
| localstore_version       | yes      |   4.6      |        | Redhat local storage operator version        |
| num_devices            | yes   |   1      |    number    | devices are detected automatically using autoDiscovery   |

Dependencies
--------

Uses ocp_login role

Example Playbook
---------

see [request-ocs-fyre-play](https://github.com/IBM/community-automation/tree/master/ansible/request-ocs-fyre-play)

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Ray Ashworth (ashworth@us.ibm.com)
