ocp-cs: Common Services on OCP
=========

This module will install Common Services on OCP. Supported versions starting with 3.3 and above.

Requirements
------------

 - Running OCP 4.x cluster is needed.

Role Variables
--------------

| Variable                  | Required | Default                                            | Comments                                                  |
|---------------------------|----------|----------------------------------------------------|-----------------------------------------------------------|
| cs_action                 | no       | install                                            | `install` to install Common Services, `uninstall` to uninstall |
| cs_setup_dir              | no       | ~/setup-files/cs-setup                             | Place for config generation of Common Services files      |
| cs_operator_name          | no       | ibm-common-service-operator                        | Name for operator subscription                            |
| cs_operator_project_name  | no       | common-service                                     | Namespace to use for installing Common Services operators |
| cs_operator_catalog_image | no       | icr.io/cpopen/ibm-common-service-catalog:latest    | `latest` for v3, `3.6.6` `3.14.0` are also valid          |
| cs_subscription_channel   | no       | v3                                                 | stable-v1, v3                                             |
| cs_subscription_strategy  | no       | Automatic                                          | Approval stragergy for operator subscription              |
| cs_operand_list           | no       | []                                                 | List of Operands to install, name or pattern. empty list default to everything |
| cs_operand_to_disable     | no       | ["elastic"]                                        | List of Operands to disable, name or pattern              |
| storageclass_name         | no       | cluster default sc                                 | StorageClass name                                         |
| strict_validation         | no       | true                                               | Specify if to validate deployment strictly                |

Dependencies
------------

 - None

Example Playbook
----------------

    - name: Install common services
      hosts: bastion
      roles:
      - common_services

License
-------

See LICENCE.txt

Author Information
------------------

Xinchun Liu (xcliu@ca.ibm.com)
Prajyot Parab (prajyot.parab@ibm.com)

