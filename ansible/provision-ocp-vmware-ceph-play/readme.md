# Provision OCP cluster

This provisioning play is used to create OCP  vmware-ipi clusters with rook-ceph installed.  This play is a replacement for the terraform tf_openshift_4 vmware installations. I does everything the tf_openshift_4 vmware installer/uninstaller does but uses the vmware-ipi instead of doing a vmware upi install.  It passes a request to an OCP cluster that is running the hive operator and contains all of the hive custom resources.  The role that supports this play is designed with ansibe templates.

## How to use

- You can use a shared instance of ACM or Hive, (internal to IBM, contact Ray Ashworth Or Walt Krapohl for details)  
alternatively
- You can install hive on your own OCP cluster [Hive Repository](https://github.com/openshift/hive)
- You can install Redhat Advanced Cluster Management on your OCP cluster [Installing RHACM operator](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.0/html-single/install/index#installing-red-hat-advanced-cluster-management-from-the-console)

## Prereqs

- The prereq installer script has been run from `community-automation/scripts/common/install-prereqs.sh`. This will install all the prereq's need to use this play.
- DHCP server is setup on the vmware network within the vCenter.
- An instance of RHACM or Hive is installed in the VMware network on the vCenter.
- Know your hive and vsphere vCenter credentials.

## Supporting roles

See the following readmes for details about the roles

- [ocp_login](https://https://github.com/IBM/community-automation/blob/provision-ocp-cluster/ansible/provision-ocp-cluster-play/readme.md)
- [ocp_cluster_tag](https://github.com/rayashworth/community-automation/blob/provision-ocp-cluster/ansible/provision-ocp-cluster-play/readme.md)

## Top level folder

community-automation/ansible/provision-ocp-vmware-ceph-play

## Important files

- examples/inventory  # example inventory file
- examples/vsphere-vars.yml # Contains vmware specific variables
- examples/common-vars.yml # contains details about your provisioning request

## variable files to be edited

copy appropriate files from the examples folder to the parent play folder

```
cp exampeles/inventory .
cp examples/common-vars.yml .
cp examples/vSphere-vars.yml .
```

## edit variable files

- edit common-vars.yml
- edit vsphere-vars.yml

## Create cluster

When using variable files
```
ansible-playbook -i inventory provision-ocp-vmware-ceph-play.yml
```

When choosing to add variables to command line
```
ansible-playbook -i inventory provision-ocp-vmware-ceph-play.yml -e "CLSUTER_NAME=your_cluster_name" -e "admin_task=provision"
```

## Destroy cluster

Following pulls cluster name from common-vars.yml

```
ansible-playbook -i inventory provision-ocp-vmware-ceph-play.yml -e "admin_task=delete"
```

Following uses command line to specify extra params that will overwrite what is in common-var.yml

```
ansible-playbook -i inventory provision-ocp-vmware-ceph-play.yml -e "CLSUTER_NAME=your_cluster_name" -e "admin_task=delete"
```
