ocp-cs: Common Services on OCP
=========

This module will install Common Services on OCP. Supported versions starting with 3.3 and above.

Requirements
------------

 - Running OCP 4.x cluster is needed.

Role Variables
--------------

| Variable                 | Required | Default                            | Comments                                                  |
|--------------------------|----------|------------------------------------|-----------------------------------------------------------|
| cs_setup_dir             | no       | ~/setup-files/cs-setup             | Place for config generation of Common Services files      |
| cs_operator_name         | no       | ibm-common-service-operator        | Name for operator subscription                            |
| cs_operator_project_name | no       | common-service                     | Namespace to use for installing Common Services operators |
| cs_subscription_channel  | no       | dev                                | Update channel for operator subscription                  |
| cs_subscription_strategy | no       | Automatic                          | Approval stragergy for operator subscription              |
| cs_operand_list          | no       | []                                 | List of Operands to install, name or pattern. empty list default to everything |
| cs_operand_to_disable    | no       | ["elastic"]                        | List of Operands to disable, name or pattern              |
| storageclass_name        | no       | managed-nfs-storage                | StorageClass name                                         |
| strict_validation        | no       | true                               | Specify if to validate deployment strictly                |

Dependencies
------------

 - None

Example Playbook
----------------

    - name: Install common services
      hosts: bastion
      roles:
      - ocp-cs

License
-------

See LICENCE.txt

Author Information
------------------

Prajyot Parab (prajyot.parab@ibm.com)

