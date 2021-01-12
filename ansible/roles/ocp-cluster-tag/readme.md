# Tagging clusters

Details about tagging can be found at the followign playbook link  
https://playbook.cloudpaklab.ibm.com/public-cloud-management/

Create the following file in your play

NOTE: ansible playbook was run on Ubuntu 18.04

```
---
    collections:
      - name: community.general
        source: https://galaxy.ansible.com
      - name: community.aws
        source: https://galaxy.ansible.com
      - name: google.cloud
        source: https://galaxy.ansible.com
```

Run the collection install command
```
# ansible-galaxy collection install -r requirements.yml
```

```
AWS prereq
# pip3 install --upgrade six
# pip3 install boto
# pip3 install boto3
# pip3 install botocore

Google prereq
# pip3 insetall google-api-python-client
# pip3 install google-auth
# pip3 insteall google-auth-httplib2

Azure prereq

```

## Cluster tag variable
The cluster tag variable is a set of 1 to many key/value pairs as follows

```
"cluster_tags": { cluster: <cluster_name>, owner: <email>, etc... }
```
