# Ansible Playbook for installing Openshift Container Storage (OCS) onto Fyre OCP+ clusters and Quickburn large clusters.

## Overview

- Installs Openshift Container Storage (OCS) on fyre 4.6 and newer clusters
  To begin clone this repository to a VM that meets the ansible requirements specified in README here
  - cd to the request-ocs-fyre-play dir.

  - Install using the `fyre inf` node.
    - Copy to current folder from the examples folder the `inventory_remote_inf_node` and  rename to inventory.
      - Ansible will use the oc already installed on the `inf` node and push all the scripts and templates to the `inf` node for running. You only need to enter into the inventory file your fyre root user PW  and inf IP.
  - Install using a `local  ubuntu VM` using `oc login`.
    - Run oc login locally on local VM to your fyre cluster.
    - Copy from examples to current dir the `inventory_local`, renaming to `inventory`. Ansible will run scripts locally on the `ubuntu VM` and use the `oc` on the local VM.

- To install OCS on Fyre `bare metal` clusters requires clusters with follow min resource requirements.
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

- OCS creates the following 4 storageclass's
  - `localblock`
  - `ocs-storagecluster-ceph-rbd` - Block storage (RWX)
  - `ocs-storagecluster-ceph-rgw` - Bucket storage
  - `ocs-storagecluster-cephfs` - File storage (RWX)
  - `openshift-storage.noobaa.io` - Object storage 

- Sets `ocs-storagecluster-cephfs` as the default storageclass, but will check first for any current default sc and make it not the default. This is configurable, change the `examples/ocs_install_vars.yaml` file and move to current dir if you want something different, or change the variable in the run of the playbook per the example below.

## Assumptions:

- Ansible 2.9 or later installed, with python3.
- A healthy Fyre OCP+/quickburn cluster in running state.
  - Min 3 worker nodes with /dev/vdb additional storage, 16 CPS and 64G mem. (32GB will work)
- oc client installed and oc login done to OCP cluster, if running local using `examples/inventory_local` on ubuntu VM.
- Fyre root user password, if running remote mode using `examples/inventory_remote_inf_node`, on cluster `inf` node.

## edit variables file

- cp examples/ocs_install_vars.yml

```code
setdefault: true  #Set the default storageclass to the value in defatult_sc
default_sc: ocs-storagecluster-cephfs # OCS storageclass to set as the default.

ocp_client_version: "4.9.15"
client_os: "linux" # mac|windows|linux

login_retries: 10
kubeadmin_password: "ASDAS"  # your cluster kubeadmin password
ocp_api_url: "api.myocp.cp.fyre.ibm.com" 
```

## Run playbook

Once you have configured the `inventory` file, run the playbook using one of the following methods:

```bash
ansible-playbook  -i inventory request-ocs-fyre.yml

```bash
or pass parameters (This example sets storageclass `ocs-storagecluster-ceph-rbd` as the default storageclass)

```bash
ansible-playbook  -i inventory request-ocs-fyre.yml -e "default_sc=ocs-storagecluster-ceph-rbd"
```

Playbook run example for `Quickburn` or `fyre UI` clusters

```bash
ansible-playbook  -i inventory request-ocs-fyre.yml -e "fyre_ui_build=true"
```

Playbook run example if using ocs_install_vars.yaml

```bash
ansible-playbook  -i inventory -e @ocs_install_vars.yml request-ocs-fyre.yml
```

### License

See LICENCE.txt
