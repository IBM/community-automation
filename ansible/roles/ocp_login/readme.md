ocp_login
=========

Login to your ocp cluster

------------

Requirements
------------

- valid credential to cluster

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| kubeadmin_user          | yes       | kubeadmin   | valid admin user     |                        |
| kubeadmin_password      | yes      |         |                 |                          |
| ocp_api_url           | yes      |   |  | example: "api.my-cluster.purple-chesterfield.com") |
| ocp_api_port          | yes   | 6443 |  |  |
| kubeconfig_location   | yes   | $HOME/.kube | valid folder |  |  
| login_retries         | yes   | 10 |  |  |  

Dependencies
------------

- oc_client_install

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - ocp_login

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Ray Ashworth (ashworth@us.ibm.com)
