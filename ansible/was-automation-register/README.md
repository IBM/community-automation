# Ansible Playbook for registering tWAS Application Server to WebSphere Automation

## Assumptions:

 - WebShpere Automation configured

   - [WebSphere Automation pre-reqs](https://www.ibm.com/docs/en/ws-automation?topic=servers-adding-server-track-security-vulnerabilities#cf-t-addserver__prereq_add_server)
 - [tWAS - runs the configuretWasUsageMetering.py script on a dmgr for all application servers in the cell](https://www.ibm.com/docs/en/ws-automation?topic=vulnerabilities-adding-websphere-application-server-server) 
 -  [Liberty](https://www.ibm.com/docs/en/SSH304G/cf-t-add-liberty.html)

## Limitations:

## Setting up inventory

- From the `wa-automation-register` directory copy the sample inventory file at `examples/inventory.yml` to the  current directory.

```
cp examples/inventory.yml .
```

## Run playbook

Once you have configured the `inventory.yml` file run the playbook:
```
ansible-playbook -i inventory.yml was-automation-register.yml 
```
