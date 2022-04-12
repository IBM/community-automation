common_services_cat_src_inst
=========

Ansible role for Install the CatalogSource for Common Services Operator.

-----------

Requirements
------------

- Need to be on an linux system, with ansible 2.8 or later installed.

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| catalog_source_version  | no       | latest   | latest, dev-latest       |                          |

Dependencies
------------

N/A

Example Playbook
----------------

    - name: Install common services catalog source
      hosts: bastion
      roles:
      - common_services_cat_src_inst

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Authors
-------

Add author
