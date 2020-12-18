# Provision OCP cluster 

This provisioning play is used to create OCP cluster on all cloud (AWS,vsphere, google, and azure).  This play is wrapper for openshift-hive.  It passes a request to an OCP cluster that is running the hive operator and contains all of the hive custom resources.  The role that supports this play is designed with ansibe templates, available samples are AWS and vSphere.

**NOTE:** This play is currently implemented for AWS only.  The rest of the clouds are open for other to test and implament.

## Prereqs

- contact Ray Ashworth or Walt Krapohl for ACM/Hive URL details.
- know your cloud credentials

## Tagging clusters

Details on tagging your cluster can be found at the following link.  
https://playbook.cloudpaklab.ibm.com/public-cloud-management/#Info_Needed_for_Tags

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

copy appropriate files from the examples directory
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
ansible-playbook -i inventory provision-ocp-cluster-play.yml -e "admin_task=delete" -e "cloud=aws" 
```
