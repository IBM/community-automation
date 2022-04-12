python_install_fyre
=========

This module will install git onto the inf node of a fyre OCP clusters version 4.4.3 or later.

------------

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

    - name: Install csi-cephfs
      hosts: bastion
      roles:
      - python_install_fyre
      - git_install_fyre
      - csi_cephfs_fyre

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Jesse Peek (peek@ibm.com)
