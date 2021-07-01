# Ansible Playbook for configuring VNC Server

## Limitations:

- Currently support for:
  - RHEL8
  - UB20.04 ( future )


## Setting up inventory

- From the `vnc-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.

```
cp examples/inventory .
```
- Change the ansible_user in the inventory to match the target user you wish to run vnc server

## Run playbook


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory vnc-play


## Access vnc 

One can also vncviewer stackname_FQDN:5901
password is : vncPassw0rd
