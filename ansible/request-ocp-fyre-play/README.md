# Ansible Playbook for creating an ocp cluster on fyre.

## Overview

- Will create an OCP 4.x cluster in fyre.
  - Using `fyre_ocptype=ocpplus` this will create a fyre OCP+beta 4.x cluster.
    - The `ocpVersion=` parm for the cluster must match the versions avaiable in fyre.ibm.com GUI OCP+beta tab.
    - All OCP+beta clusters are created with an additional /dev/vdb 300G disk.  

## Assumptions:

 - You have capacity in fyre
 - Fyre is online

## Setting up inventory

- From the `request-ocp-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `fyreuser` variable in the `inventory` file with the name of your fyre user (see https://fyre.ibm.com/account).
- Modify `fyreapikey` variable in the `inventory` file  with your fyre api key (see https://fyre.ibm.com/account).
- Optionally remove `ansible_python_interpreter: /usr/bin/python3` if you have issues with python discovery
```
cp examples/inventory .
```

## Run playbook

The playbook/role supports provisioning clusters at configurable ocpVersions and works with the OCP and OCP+ apis from fyre team
These are controlled by the ocpVersion and fyre_ocptype variables respectively.

Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=myClusterName" -e "ocpVersion=desiredVersion" -e "fyre_ocptype=ocpplus"
```

This command will create an ocp plus cluster in fyre called myClusterName. If myClusterName already exists it will instead just define it to ansible.
