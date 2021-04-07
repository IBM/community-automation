# Provision OCP cluster

This provisioning play is used to create OCP cluster on all cloud (AWS,vsphere, google, and azure).  This play is wrapper for openshift-hive.  It passes a request to an OCP cluster that is running the hive operator and contains all of the hive custom resources.  The role that supports this play is designed with ansibe templates, available samples are AWS, google, azure and vSphere.

## How to use

- You can use a shared instance of ACM or Hive, (internal to IBM, contact Ray Ashworth Or Walt Krapohl for details)  
alternatively
- You can install hive on your own OCP cluster [Hive Repository](https://github.com/openshift/hive)
- You can install Redhat Advanced Cluster Management on your OCP cluster [Installing RHACM operator](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.0/html-single/install/index#installing-red-hat-advanced-cluster-management-from-the-console)

## Prereqs

- An instance of RHACM or Hive
- know your cloud credentials
- If you want to use with VMWare, the RHACM or Hive OCP instance must live inside your vCenter in order to install into your vCenter. The Redhat OCP IPI installer does not work if RHACM/hive is outside the vCenter.  However the hive instance in your vCenter can install to public clouds (AWS, google, azure)

## Supporting roles

See the following readmes for details about the roles

- [ocp_login](https://https://github.com/IBM/community-automation/blob/provision-ocp-cluster/ansible/provision-ocp-cluster-play/readme.md)
- [ocp_cluster_tag](https://github.com/rayashworth/community-automation/blob/provision-ocp-cluster/ansible/provision-ocp-cluster-play/readme.md)

## Tagging clusters

Example tags can be found at the following link.  (Used by content team)
[Interal IBM Playbook](https://playbook.cloudpaklab.ibm.com/public-cloud-management/#Info_Needed_for_Tags)

Tag settings can be found in common-vars.yml. See vars file for tag details

## Top level folder

community-automation/ansible/provision-ocp-cluster-play

## Important files

- examples/inventory  # example inventory file, rarely changes
- examples/**CLOUD_REF**-vars.yml # Contains cloud specific variables ( example: **aws-vars**.yml )
- examples/common-vars.yml # contains details about your provisioning request

## variable files to be edited

copy appropriate files from the examples folder to the parent play folder

```
cp exampeles/inventory .
cp examples/common-vars.yml .
cp examples/<cloud>-vars.yml .
   where <cloud> is aws|google|azure
```

## edit variable files

- edit common-vars.yml
- edit **\<cloud\>**-vars.yml

Run the collection install command
```
# ansible-galaxy collection install -r requirements.yml
```

## Create cluster

When using variable files
```
ansible-playbook -i inventory provision-ocp-cluster-play.yml
```

When choosing to add variables to command line
```
ansible-playbook -i inventory provision-ocp-cluster-play.yml -e "CLSUTER_NAME=your_cluster_name" -e "admin_task=provision" -e "cloud=aws"
```

## Destroy cluster

Following pulls cluster name from common-vars.yml

```
ansible-playbook -i inventory provision-ocp-cluster-play.yml -e "admin_task=delete"
```

Following uses command line to specify extra params that will overwrite what is in common-var.yml

```
ansible-playbook -i inventory provision-ocp-cluster-play.yml -e "CLSUTER_NAME=your_cluster_name" -e "admin_task=delete" -e "cloud=aws"
```
