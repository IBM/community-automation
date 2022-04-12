provision_pool
=========

Provision an OCP cluster pool using HIVE operator

------------

Requirements
------------

OCP cluster with hive installed

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| foo                     | no       | false   | true, false               | example variable                         |
| bar                     | yes      |         | eggs, spam                | example variable                         |

Dependencies
------------

None

Templates
------------

These templates were created using the hiveutil command and contain token variable that will be replaced during runtime.  These templates may need updates to keep up with changes coming from the hive team. The only one the works is the aws-pool-template right now.

- aws-install-config-template.j2
- aws-pool-template.j2
- google-pool-template.j2
- azure-pool-template.j2
- vsphere-pool-template.j2
- ibmcloud-pool-template.j2 (not supported yet.)
- image-set-tempolate.j2

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - provision_pool

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Ray Ashworth (ashworth@us.ibm.com)
