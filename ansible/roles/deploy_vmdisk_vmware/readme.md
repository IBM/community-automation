deploy_vmdisk_vmware: deploy an second drive onto every worker in the vmware cluster.
=========

Ansible role for deploy second disk (sdb) drive on to vmware worker nodes.

Requirements:
------------

 - Need to be on an linux box or docker image that has run `community-automation/scripts/common/install-prereqs.sh`.

Example Playbook
----------------

    - name: Install second disk drive on worker nodes.
      hosts: bastion
      roles:
      - deploy_vmdisk_vmware

License
-------

See LICENCE.txt
