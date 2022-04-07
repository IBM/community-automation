ocp_pool_claim
=========

claim a cluster from a hive pool

------------

Requirements
------------

An OCP cluster with hive installed

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| pool_name               | yes      |    | string               | |
| admin_task              | yes      |  claim  | claim, release        | |
| claim_name              | yes      |    |                 | |
| pool_namespace          | yes      |    |                 | |

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - ocp_pool_claim

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Ray Ashworth (ashworth@us.ibm.com)
