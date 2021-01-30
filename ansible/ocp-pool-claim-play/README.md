# Claiming a cluster from a cluster pool
This play assumes you have installed "Hive" on an OCP cluster or you are using the shared "Hive" instance.  
Contact Ray Ashworth or Walt Krapohl for shared "Hive" details

This play is an example of claiming a cluster and running post installation steps.

## prereq's

```
- Access to a "Hive" instance 
- Predefined Cluster Pool
```

## edit variable files

from the ocp-pool-claim-play folder
```
# cp examples/* .
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