ocp_add_users_to_scc
=========

This role can be used to patch existing SCC with the user/service account required to give permissions to various OCP objects.

---------

Read more about [SCC Doc](https://www.openshift.com/blog/understanding-service-accounts-sccs)

Requirements
--------------

None

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| scc_to_be_modified     | yes       |    |  scc to update              |      "hostmount-anyuid"                     |
| user_string_for_scc     | yes      |    |  string                | 'system:serviceaccount:{{ nfs_provisioner_namespace }}:nfs-client-provisioner'                         |

Dependencies
------------

* Ansible
  * ansible version ">=2.10.x"
  * `community.k8s` collection
  * `ocp_request_token` role
  * [OpenShift Python Library](https://pypi.org/project/openshift/). You can install it by running this command: `pip3 install openshift`

Example Playbook
----------------

    - hosts: localhost
      roles:
         - role: ocp_add_users_to_scc 

License
-------

See [LICENCE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Rahul Tripathi (rahul.tripathi@ibm.com)  
