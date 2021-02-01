# Claiming a cluster from a cluster pool
This playbook assumes you have installed "Hive" on an OCP cluster or you are using the shared "Hive" instance.  
Contact Ray Ashworth or Walt Krapohl for shared "Hive" details

This playbook is used to claim a cluster from a cluster pool.

It is assumed that you will create a post install role for your team that may not be the same as other teams roles.

## prereq's

```
- Access to a "Hive" instance 
- Predefined Cluster Pool
```

## edit variable files

from the ocp-pool-claim-play folder
```
# cp examples/inventory .
# cp examples/pool-vars.yml .
# cp examples/YOUR_ROLE_VARS_FILE_vars.yml custom-vars.yml
```

edit custom-vars.yml  
edit pool-vars.yml

## Running the play

### using without command line parameters, assumes all vars are filled in

```
# ansible-playbook -i inventory ocp-pool-claim-play.yml
```

### using with command line parameters

```
# ansible-playbook -i inventory ocp-pool-claim-play.yml -e "claim_name=YOUR_CLAIM_NAME" -e "admin_task=claim"
```

## release a claimed cluster

```
# ansible-playbook -i inventory ocp-pool-claim-play.yml -e "claim_name=YOUR_CLAIM_NAME" -e "admin_task=release"
```