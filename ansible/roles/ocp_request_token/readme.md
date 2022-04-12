ocp_request_token
=========

This role fetches the OCP token which can be used to consume the Kubernetes/OCP API's

----------

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| kubeadmin_user          | yes       | kubeadmin   |               |                         |
| kubeadmin_password      | yes      |         |                 |                          |
| ocp_api_url             | yes      |         |  api URL               | example: "https://api.my-cluster.purple-chesterfield.com:6443"                         |

Dependencies
------------

* Ansible
  * ansible version ">=2.10.x"
  * `community.okd` collection
  * [OpenShift Python Library](https://pypi.org/project/openshift/). You can install it by running this command: `pip3 install openshift`

Example Playbook
----------------

    - hosts: localhost
      roles:
         - role: ocp_request_token

License
-------

See [LICENCE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Rahul Tripathi (rahul.tripathi@ibm.com)
