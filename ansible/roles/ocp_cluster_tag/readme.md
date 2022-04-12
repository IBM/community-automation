ocp_cluster_tag
=========

Tag a cluster to keep it from being removed by cloud cleanup of any other reason yu might want to tag a cluster

------------

Details about tagging can be found at the following playbook link  

[playbook tagging details](https://playbook.cloudpaklab.ibm.com/public-cloud-management/)

Requirements
------------

- admin access to the cloud
- only works on AWS at this time

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| tag_task                | yes       | add   | add, delete               |                          |
| cluster_tags            | yes      |         |                 |     "cluster_tags": { cluster: <cluster_name>, owner: < email >, etc... }"                     |
| cluster_name          | yes |  | automatically added | | 
| AWS_REGION            |  yes      |       |  | example: us-east1 | |
| cloud                 | yes       | aws | aws, google, azure, vsphere |  aws only |
| aws_access_key = AWS_ACCESS_KEY_ID | yes | | valid aws access key | |
| aws_secret_key = AWS_SECRET_ACCESS_KEY | yes | | valid aws secret access key | |

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - ocp_cluster_tag

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Ray Ashworth (ashworth@us.ibm.com)
