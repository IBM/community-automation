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
| ws_cert                 | yes      |   | | see defaults/main.yml |
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

Steven Schader
