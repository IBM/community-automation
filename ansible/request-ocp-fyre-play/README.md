# Ansible Playbook for creating an ocp cluster on fyre.

## Assumptions:

 - You have capacity in fyre
 - Fyre is online

## Setting up inventory

- From the `request-ocp-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `fyreuser` variable in the `inventory` file with the name of your fyre user (see https://fyre.ibm.com/account).
- Modify `fyreapikey` variable in the `inventory` file  with your fyre api key (see https://fyre.ibm.com/account).

```
cp examples/inventory .
```

## Run playbook


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=myClusterName" -e "ocpVersion=desiredVersion"
```