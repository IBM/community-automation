request_ocp4_logging
============

This role will install OCP logging operator and operand

----------

Requirements
------------

- Running OCP 4.x cluster
- Ansible 2.9 or later.
- oc client installed.
- oc login to OCP cluster performed.

How to install oc client
------------------------

- Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
- Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
- Extract: tar xf oc.tar.gz
- Move to /usr/local/bin: cp oc /usr/lcoal/bring
- Example oc login: `c login https://api.evident-pika.purple-chesterfield.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>`

Role Variables
------------------

Default parameters set in the defaults/main.yml

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| logging_bastion_setup_dir   | yes       | ~/setup-files/transfer-setup   | valid folder      |                          |
| rendered_sc             | yes      |  default sc    | storageClass name          |                          |
| ocp_logging_version     | yes  | 4.2  |   |   |

Dependencies
---------

None

Example Playbook
----------------

```yaml
    - name: Install OCP 4.x Logging on OCP Cluster
      hosts: bastion
      roles:
      - request_ocp4_logging
```

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Walter Kraphol
