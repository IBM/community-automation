oc_client_install
=========

Install openshift oc client

------------

Requirements
------------

None

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| ocp_client_version      | yes       | 4.5.10   | true, false             |                          |
| client_os               | yes      | linux     | linux, mac, windows      |                         |

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - oc_cli_install

Example meta/main.yml  
--------

    dependencies:
      - role: oc-cli-install

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Ray Ashworth (ashwoth@us.ibm.com)
