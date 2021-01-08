# Tagging clusters

Details about tagging can be found at the followign playbook link  
https://playbook.cloudpaklab.ibm.com/public-cloud-management/

Create the following file in your play
```
---
    collections:
      - name: community.general
        source: https://galaxy.ansible.com
      - name: community.aws
        source: https://galaxy.ansible.com
```

Run the collection install command
```
# ansible-galaxy collection install -r requirements.yml
```

```
# pip3 install --upgrade six
# pip3 install boto
# pip3 install boto3
# pip3 install botocore
```