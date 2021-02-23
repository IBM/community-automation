# Tagging clusters

Details about tagging can be found at the followign playbook link  
https://playbook.cloudpaklab.ibm.com/public-cloud-management/

## NOTES

- ansible playbook was run on Ubuntu 16.04 and 18.04
- This role only works with AWS at this time.

## Variables used for tagging

other public clouds credentials will become variables

- cluster_tags
- tag_task (add)
- AWS_REGION
- cloud (aws, google, azure, vsphere)
- aws_access_key = AWS_ACCESS_KEY_ID
- aws_secret_key = AWS_SECRET_ACCESS_KEY

## Cluster tag variable

The cluster tag variable is a set of 1 to many key/value pairs as follows (eg. key1: value1, key2: value2)

tag name "cluster_name" will be added automatically

```
"cluster_tags": { cluster: <cluster_name>, owner: <email>, etc... }
```
