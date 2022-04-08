request_ocs
==========

This role installs OCS onto either AWS or VMware Clusters that meet the following requirements.

----------

Requirements
------------

- Running OCP 4.4.15 or greater on AWS or VMware cluster is needed
- Min of 3 worker nodes per cluster.
- Min sum of worker CPU must be 48 CPUs.
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
----------

Default parameters set in the defaults/main.yml

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| ocs_channel             | yes       | stable-4.5   |                |                          |
| ocs_bastion_setup_dir   | yes      |   ~/setup-files/ocs-setup      |                 |                          |
| setdefault              | yes      | false         | true, false                 |                          |

Dependencies
-------

None

Example Playbook
----------------

```yaml
    - name: Install ocs
      hosts: bastion
      roles:
      - request_ocs_common
```

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Walter Kraphol
