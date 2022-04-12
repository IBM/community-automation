git_install_fyre
=========

This role will install git onto the inf node of a fyre OCP+ clusters version 4.4.3 or later.

-----------

Requirements
------------

- Running fyre OCP+ cluster is needed.

Role Variables
--------------

None

Dependencies
------------

None

Example Playbook
----------------

    - name: Install git 
      hosts: bastion
      roles:
      - git_install_fyre

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Walt Krapohl (krapohl@us.ibm.com)
