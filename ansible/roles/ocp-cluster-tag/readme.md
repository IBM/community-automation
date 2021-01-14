# Tagging clusters

Details about tagging can be found at the followign playbook link  
https://playbook.cloudpaklab.ibm.com/public-cloud-management/

## NOTES

- ansible playbook was run on Ubuntu 16.04 and 18.04
- This role only works with AWS at this time.

## requirements

see [install-prereq script](http://github.com/IBM/community-automation/scripts/common/README.md)
see [prereq-play](http://github.com/IBM/community-automation/ansible/prereq-play/README.md)

## Variables used for tagging

- cluster_tags
- AWS_REGION
- cloud (aws, google, azure, vsphere)
- AWS_ACCESS_KEY_ID
- aws_access_key
- AWS_SECRET_ACCESS_KEY
- aws_secret_key

## Cluster tag variable

The cluster tag variable is a set of 1 to many key/value pairs as follows (eg. key1: value1, key2: value2)

```
"cluster_tags": { cluster: <cluster_name>, owner: <email>, etc... }
```
