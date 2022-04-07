db2_fyre
=========

This role install DB2 CE

------------

[IBM Operator Catalog](https://www.ibm.com/support/knowledgecenter/SSTTDS_11.0.0/com.ibm.ace.icp.doc/certc_install_enablingoperatorcatalog.html)

Install [DB2 CE](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.welcome.doc/doc/welcome.html) version `11.5.5.0-cn1` on OCP clusters.

Requirements
------------

* Cluster:
  * OpenShift version ">=4.5.x"
* Storage
  * Any storage class. You can use the [csi-cephfs-fyre-play](https://github.com/IBM/community-automation/tree/master/ansible/csi-cephfs-fyre-play) playbook to provision a storage class on your OCP Fyre cluster.
* Resources:
  * Minimum 1.7 vCPU
  * Minimum 2 Gi

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| kubeadmin_user          | yes      | kubeadmin   | valid admin user              | example variable                 |
| kubeadmin_password      | yes      |         |                 |                          |
| ocp_api_url             | yes      |         | example: "https://api.my-cluster.purple-chesterfield.com:6443" |                    |
| db2_namespace           | yes      |         |                 |                          |
| storageClassName        | yes      |         |                |                          |
| entitled_key            | yes      |         | valid IBM entitlement key               |     [Entitlement](https://myibm.ibm.com/products-services/containerlibrary)   |

Dependencies
------------

* Ansible
  * ansible version ">=2.10.x"
  * `community.okd` collection
  * `community.general` collection
  * `ocp_request_token` role ( a dependency in meta folder)

Example Playbook
----------------

    - hosts: localhost
      roles:
         - db2_fyre

License
-------

See [LICENCE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Rahul Tripathi (rahul.tripathi@ibm.com)
