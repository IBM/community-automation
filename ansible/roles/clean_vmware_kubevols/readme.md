clean_vmware_kubevols
=========

After vmware cluster is uninstalled call this role to cleam up any orphaned kubevol files.

------------

Requirements
------------

- Need to be on an linux box or docker image that has run `community-automation/scripts/common/install-prereqs.sh`.

Example Playbook
----------------

    - name: clean orphaned kubvols on  vCenter
      hosts: bastion
      roles:
      - clean_vmware_kubevols

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)
