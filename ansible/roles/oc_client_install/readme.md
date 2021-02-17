# oc client install

When oc cli is needed you can include this role in your ansible/role/```<rolename>```/meta/main.yml 
example:  

```
---
dependencies:
  - role: oc-cli-install
  - role: ocp_login
```

You will need to pass ```ocp_client_version (eg. 4.3.13, 4.4.0,etc...)``` or set in your defaults/main.yml
