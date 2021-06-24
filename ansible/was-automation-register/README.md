# Ansible Playbook for registering tWAS Application Server to WebSphere Automation

## Assumptions:

 - WebShpere Automation configured
 - [runs this script on a dmgr for all application servers in the cell](https://www.ibm.com/docs/en/ws-automation?topic=vulnerabilities-adding-websphere-application-server-server) 

## Setting up inventory

- From the `wa-automation-register` directory copy the sample inventory file at `examples/inventory` to the  current directory.

```
cp examples/inventory .
```

## Run playbook

Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory -e wsadmin_username=yourAdminUser -e wsadmin_password=yourAdminPassword -e wa_target_path='/opt/WAS/profiles/dmgr' -e wa_url='https://cpd-websphere-automation.apps.yourCluster.cp.fyre.ibm.com/websphereauto/meteringapi' -e api_key='yourApiKey' -e sslRef='CellDefaultSSLSettings'

```
