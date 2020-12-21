# Provision OCP cluster 

This provisioning play is used to create OCP cluster on all cloud (AWS,vsphere, google, and azure).  This play is wrapper for openshift-hive.  It passes a request to an OCP cluster that is running the hive operator and contains all of the hive custom resources.  The role that supports this play is designed with ansibe templates, available samples are AWS and vSphere.

**NOTE:** This play is currently implemented for AWS only.  The rest of the clouds are open for other to test and implament.

## How to use

- You can install hive on your own OCP cluster [Hive Repository](https://github.com/openshift/hive)
- You can install Redhat Advanced Cluster Management on your OCP cluster [Installing RHACM operator](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.0/html-single/install/index#installing-red-hat-advanced-cluster-management-from-the-console)
- You can use a shared instance of ACM or Hive, (internal to IBM, contact Ray Ashworth Or Walt Krapohl for details)

## Prereqs

- An instance of RHACM or Hive
- know your cloud credentials
- If you want to use with VMWare, the RHACM or Hive OCP instance must live inside your vCenter in order for the Redhat OCP IPI installer to work properly. 

## Tagging clusters

Details on tagging your cluster can be found at the following link.  
[Interal IBM Playbook](https://playbook.cloudpaklab.ibm.com/public-cloud-management/#Info_Needed_for_Tags)

Tag settings can be found in common-vars.yml  

**Current tags** used by cleanup script
| Tag  | Values  | Description  |
|---|---|---|
| owner  | email   | on google use FirstnameLastname  |
| cluster  | name of cluster |   |
| Review_freq  |   | 3day,week,month,quarter, half   |
| Usage |     | temp, demo, infra (long term, must be reviewed regularly ) |
| Usage_desc | description | |
| team | team name | "Team" when Azure |
| Delete_date | YYYY-MM-DD | Azure ONLY |

## Important files

- examples/inventory  # example inventory file, rarely changes
- examples/**\<cloud\>**-vars.yaml # Contains cloud specific variables
- examples/common-vars.yaml # contains details about your provisioning request

## variable files to be edited

copy appropriate files from the examples folder to the parent play folder
```
cp exampeles/inventory .
cp examples/common-vars.yaml .
cp examples/\<cloud\>-vars.yaml .
```

edit common-vars.yaml and **\<cloud\>**-vars.yaml

## Create cluster

When using variable files
```
ansible-playbook -i inventory provision-ocp-cluster-play.yml
```

When choosing to add variables to command line
```
ansible-playbook -i inventory provision-ocp-cluster-play.yml -e "admin_task=provision" -e "cloud=aws" 
```

## Destroy cluster

```
ansible-playbook -i inventory provision-ocp-cluster-play.yml -e "admin_task=delete" 
```
