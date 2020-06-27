deploy-ova-vmware: deploy an ova file to a vCenter
=========

Ansible role for uploading a new rhcos vmware ova to a vCenter.

Description
-----------

 - Downloads to the local ubuntu system a rhcos ova file.
 - Imports the ova file into a vCenter as a VM, for use as a VM template or clone.
 - Sets the storage to `thin` when importing the ova.
 - Sets the `disk.EnableUUID=TRUE`

Requirements:
------------

 - Need to be on an ubuntu system, with ansible 2.9.9 or later and pyvmomi installed.
   - sudo apt-get update -y
   - sudo apt-get install ansible
   - sudo apt-get install -y python-pyvmomi

Example Playbook
----------------

   - name: Install ova to vCenter
     hosts: bastion
     roles:
     - deploy-ova-vmware

License
-------

See LICENCE.txt
