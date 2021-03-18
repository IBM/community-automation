# Ansible Playbook for creating an RedHat DB2 CE v11.5.x host on Fyre

## Assumptions:

 - You have capacity in fyre
 - Fyre is online

## Setting up inventory

- From the `request-rhel-db2-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `fyreuser` variable in the `inventory` file with the name of your fyre user (see https://fyre.ibm.com/account).
- Modify `fyreapikey` variable in the `inventory` file  with your fyre api key (see https://fyre.ibm.com/account).

```
cp examples/inventory .
```

## Run playbook

The playbook/role supports a single Intel Fyre vm with 2cpu/4gb RHEL 8.x.  The stack name is randomly chosen unless overridden

e.g. -e stackName=test-db2


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory request-rhel-db2-fyre-play.yml 

or

ansible-playbook  -i inventory request-crc-fyre-play.yml -e stackName=jmeterStack -e jmeterUser=nest -e noLog=false -e db2Archive='linkTodb2Archive.tgz'  -e db2responseFile='linkTodb2Responsefile'
```

To disable vnc server install ( takes around 8 minutes ) add
``` 
-e vnc=False
```

## Access the command line

Once the stack is created, ssh root@stackname_FQDN and set the password for db2inst1

## Access vnc 

One can also vncviewer stackname_FQDN:5901
password is : vncPassw0rd
