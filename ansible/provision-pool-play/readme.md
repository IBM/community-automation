# Provision Hive Pool

This provisioning play is used to provision a hive pool.  This play is wrapper for openshift-hive.  It passes a request to an OCP cluster that is running the hive operator and contains all of the hive custom resources.  The role that supports this play is designed with ansibe templates, available samples are AWS.

**NOTE:** This play is currently implemented for AWS only.  The rest of the clouds are open for other to test and implament.

## How to use

- You can use a shared instance of ACM or Hive, (internal to IBM, contact Ray Ashworth Or Walt Krapohl for details)  
alternatively
- You can install hive on your own OCP cluster [Hive Repository](https://github.com/openshift/hive)
- You can install Redhat Advanced Cluster Management on your OCP cluster [Installing RHACM operator](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.0/html-single/install/index#installing-red-hat-advanced-cluster-management-from-the-console)

## Prereqs

- An instance of RHACM or Hive
- Know your hive cloud credentials
- In the future when VMware is available, the RHACM or Hive OCP instance must live inside your vCenter in order to install into your vCenter. The Redhat OCP IPI installer does not work if RHACM/hive is outside the vCenter.  `However the hive instance in your vCenter can install to public clouds (AWS, google, azure)``

## Supporting roles

The following roles are called by this readme.

- [ocp-login](https://github.com/IBM/community-automation/blob/master/ansible/roles/ocp-login/readme.md)
- [provision-pool](https://github.com/IBM/community-automation/blob/master/ansible/roles/provision-pool/readme.md)

## Top level folder

community-automation/ansible/provision-pool-play

## Important files

- examples/inventory  # example inventory file, rarely changes
- examples/**CLOUD_REF**-pool-vars.yml # Contains cloud specific variables ( example: **aws-pool-vars**.yml )
- examples/common-pool-vars.yml # contains details about your provisioning request

## variable files to be edited

copy appropriate files from the examples folder to the parent play folder

```
cp exampeles/inventory .
cp examples/common-pool-vars.yml .
cp examples/<cloud>-pool-vars.yml .
   where <cloud> is aws|google|azure
```

## edit variable files

- edit common-pool-vars.yml
- edit **\<cloud\>**-pool-vars.yml

Run the collection install command
```
# ansible-galaxy collection install -r requirements.yml
```
## Create cluster

When using variable files
```
ansible-playbook -i inventory provision-pool-play.yml
```

When choosing to add variables to command line
```
ansible-playbook -i inventory provision-pool-play.yml  -e "admin_task=provision" -e "cloud=aws"
```

## Destroy cluster

Following pulls cluster name from common-vars.yml

```
ansible-playbook -i inventory provision-pool-play.yml -e "admin_task=delete"
```
