common-services-cat-src-inst: Install the CatalogSource for Common Services Operator
=========

Ansible role for Install the CatalogSource for Common Services Operator.

Description
-----------

 - Install the CatalogSource for the Common Services Operation .
 - It takes as input the version of the Common Services CatalogSource to install.
 - Valid Common Services versions are `latest` or `dev-latest`.

Requirements:
------------

 - Need to be on an linux system, with ansible 2.8 or later installed.

Example Playbook
----------------

    - name: Install ova to vCenter
      hosts: bastion
      roles:
      - common-services-cat-src-inst

License
-------

See LICENCE.txt
