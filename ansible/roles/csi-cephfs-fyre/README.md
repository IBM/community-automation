csi-cephfs: csi cephfs on OCP
=========

This module will install csi-cephfs on fyre OCP+Beta clusters version 4.4.3 or later.

Requirements
------------

 - Running fyre OCP+Beta cluster is needed.


Example Playbook
----------------

    - name: Install csi-cephfs
      hosts: bastion
      roles:
      - csi-cephfs-fyre

License
-------

See LICENCE.txt

Author Information
------------------

Walt Krapohl (krapohl@us.ibm.com)
