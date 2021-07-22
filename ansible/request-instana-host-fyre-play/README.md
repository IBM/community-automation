# Ansible Playbook for creating an Ubuntu 18.04 Instana hosted instance host on Fyre

## Assumptions:

 - You have capacity in fyre
 - Fyre is online

## Setting up inventory

- From the `request-instana-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `fyreuser` variable in the `inventory` file with the name of your fyre user (see https://fyre.ibm.com/account).
- Modify `fyreapikey` variable in the `inventory` file  with your fyre api key (see https://fyre.ibm.com/account).

```
cp examples/inventory .
```

## Run playbook

The playbook/role supports a single Intel Fyre vm with 16cpu/64gb Ubuntu 18.04.  The stack name is randomly chosen unless overridden

e.g. -e stackName=test-instana


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory request-instana-fyre-play.yml 

or

ansible-playbook  -i inventory request-instana-fyre-play.yml -e stackName=instana -e noLog=false 
```

## Access the command line

Once the stack is created, ssh root@stackname_FQDN 

There is an additional disk 1024GB 
