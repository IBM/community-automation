was_automatoin_register
=========

A brief description of the role goes here.

------------

Requirements
------------

None

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| api_key                 | yes       | thisIsAlwaysOverridden   |                |                          |
| wa_url                  | yes      |  thisIsAlwaysOverridden   |               |                          |
| ws_cert                 | yes      |   | | see defaults/main.yml |
| wa_keystore_pass        | yes     | thisIsAlwaysOverridden  | | see defaults/main.yml |
| wa_target_host          | yes     | thisIsAlwaysOverridden   | |  |
| wa_target_scope        | yes      | thisIsAlwaysOverridden  | |  |
| wa_target_path          | yes      | thisIsAlwaysOverridden  | | |
| wsadmin_username        | yes    | thisIsAlwaysOverridden  | |  |
| wsadmin_password        | yes    | thisIsAlwaysOverridden  |  |   |  
| waProductType          | yes     | thisIsAlwaysOverridden     |  |   |  
| startServers           | yes | false   |  |   |  

Dependencies
------------

None

Example Playbook
----------------

```yaml
    - hosts: all
      roles:
         - was_automation_register
```

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Steven Schrader
