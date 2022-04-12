deploy_ova_vmware
=========

Ansible role for uploading a new rhcos vmware ova to a vCenter.

-----------

- Downloads to the local ubuntu system a rhcos ova file.
- Imports the ova file into a vCenter as a VM, for use as a VM template or clone.
- Sets the storage to `thin` when importing the ova.
- Sets the `disk.EnableUUID=TRUE`

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| ova_url                 | yes      |    | url               |           example: (https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/4.4/4.4.3/rhcos-4.4.3-x86_64-vmware.x86_64.ova)            |
| vcenter_uid             | yes      |         |   your admin id             |                          |
| vcenter_ip              | yes      |         |    valid ip address           |                          |
| vcenter_pw              | yes      |         |                |                          |
| vcenter_datacenter      | yes      |         |                |   example: IOCDCPC1                       |
| vcenter_datastore       | yes      |         |                |   example: ICOVCPC-RSX6-102                       |
| vcenter_cluster         | yes      |         |                |   example: ICO01                       |
| vcenter_network_label   | yes      |         |                |   example: VIS241                       |
| vcenter_folder          | yes      |   ova      |                |                          |
| local_target_folder     | yes      |         | a local folder     |                          |
| govc_prq                | yes      |  vmware  |                |                          |
| govc_vers               | yes      |  0.21.0  |                |                          |
| govc_dwld               | yes      |  govc_linux_amd64.gz       |                |                          |

Requirements
------------

run prereq script found in scripts/common folder

- install-prereqs.sh
- sudo apt-get install -y python-pyvmomi

Example Playbook
----------------

    - name: Install ova to vCenter
      hosts: bastion
      roles:
      - deploy_ova_vmware

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Walter Kraphol
