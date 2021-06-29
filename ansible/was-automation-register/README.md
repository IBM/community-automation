# Ansible Playbook for registering tWAS Application Server to WebSphere Automation

## Assumptions:

 - WebShpere Automation configured

 - [tWAS - runs the configuretWasUsageMetering.py script on a dmgr for all application servers in the cell](https://www.ibm.com/docs/en/ws-automation?topic=vulnerabilities-adding-websphere-application-server-server) 
 -  Liberty - WA Cert embedded in was_automation_register/tasks/defaults/main.yml

## Limitations:

## Setting up inventory

- From the `wa-automation-register` directory copy the appropriate sample inventory file at `examples/` to the  current directory.

```
cp examples/inventory .

or

cp examples/inventory_twas .

or

cp examples/inventory_liberty .
```

## Run playbook

- startServers='true|false'
- inventory file can be a comma delimitted list of hostnames. eg: -i myhost1,myhost2,  ( note the trailing comma )

Once you have configured the `inventory` file or list of hosts, run the playbook using for tWAS:
```
ansible-playbook  -i inventory -e wsadmin_username=yourAdminUser -e wsadmin_password=yourAdminPassword -e wa_target_path='/opt/WAS/profiles/dmgr' -e wa_url='https://cpd-websphere-automation.apps.yourCluster.cp.fyre.ibm.com/websphereauto/meteringapi' -e api_key='yourApiKey' -e sslRef='CellDefaultSSLSettings' -e startServers='true' -e waProductType='tWAS'
```

Once you have configured the `inventory` file, run the playbook using for Liberty:
```
ansible-playbook  -i inventory -e wa_target_path='/opt/liberty/wlp' -e wa_url='https://cpd-websphere-automation.apps.yourCluster.cp.fyre.ibm.com/websphereauto/meteringapi' -e api_key='yourApiKey' -e startServers='true' -e waProductType='Liberty'
```
