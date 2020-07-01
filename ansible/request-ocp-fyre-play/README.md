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

The playbook/role supports provisioning clusters at configurable ocpVersions and works with the OCP and OCP+ apis from fyre team
These are controlled by the ocpVersion and fyre_ocptype variables respectively.

e.g. ocpVersion=4.3.19
fyre_ocptype=ocp or fyre_ocptype=ocpplus



Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=myClusterName" -e "ocpVersion=desiredVersion" -e="fyre_ocptype=ocpplus"
```

This command will create an ocp plus cluster in fyre called myClusterName. If myClusterName already exists it will instead just define it to ansible.