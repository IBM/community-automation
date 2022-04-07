git_install_fyre: git inf node of gyre on OCP cluster
=========

This module will install git onto the inf node of a fyre OCP+Beta clusters version 4.4.3 or later.

Requirements
------------

 - Running fyre OCP+Beta cluster is needed.


Example Playbook
----------------

    - name: Install csi-cephfs
      hosts: bastion
      roles:
      - git_install_fyre
      - csi_cephfs_fyre

License
-------

See LICENCE.txt

Author Information
------------------

Walt Krapohl (krapohl@us.ibm.com)
