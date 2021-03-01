# Community automation collection

## How to use collections

Create or update your `requirements.yml` file found in your play folder. 

Add the `community-automation.git` as shown below:

```
---
collections:
  - name: community.kubernetes
    version: 1.1.1
  - name: community.okd
    version: 1.1.0
  - name: https://github.com/IBM/community-automation.git
    type: git
```

Install this by invoking the following command:
```
ansible-galaxy install -r requirements.yml
```

Check if this was installed using the following command:
```
ansible-galaxy collection list
```

## Using in your playbook

### roles example
```
---
- name: Prepare cluster for Demo Deployment
  hosts: localhost
  gather_facts: no
  tasks:
  roles:
    - ibm_community_automation.ibm_community_automation.ocp_request_token
```

### include_role example
```
---
- name: Prepare cluster for Demo Deployment
  hosts: localhost
  gather_facts: no
  tasks:
    - include_role:
        name: ibm_community_automation.ibm_community_automation.ocp_request_token
```
