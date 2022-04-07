get_ocp_installer
=========

Download and install the Redhat Openshift installer.

------------

Requirements
------------

None

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| installer_url           | yes      | "https://mirror.openshift.com/pub/openshift-v4/clients/ocp"  |      |         |
| installer_version       | yes      | 4.7.33        |                 |                         |
| installer_file          | yes      |  openshift-install-linux.tar.gz       |                 |                          |

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - get_ocp_installer

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Add author
