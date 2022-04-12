request_ocpplus_cluster_transfer_fyre
========

This role transfers a fyre OCP+ cluster to a new user by IBM intranet email

----------

Requirements
------------

- Running fyre OCP+ cluster
- New owner needs to have a fyre account with allocation for OCP+ clusters.
- Ansible 2.9 or later.

Role Variables
------------------

Default parameters set in the defaults/main.yml

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| transfer_bastion_setup_dir  | yes       |  ~/setup-files/transfer-setup  |      |                          |
| transfer_to_email       | yes      |         | IBM email                |                          |
| cluster_name            | yes  |     | string    |   |  
| fyre_user              | yes |  | fyre user | |
| fyre_api_key           | yes |  | fyre api key  | |

Dependencies
------------

None

Example Playbook
----------------

```yaml
    - name: Transfer OCP+Beta Cluster
      hosts: bastion
      roles:
      - request_ocpplus_cluster_transfer_fyre
```

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Add author
