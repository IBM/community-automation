# Ansible Playbook for configuring AutoWAS Server

## Limitations:

- Current support for:
  - RHEL8
  - UB20.04 ( future )


## Setting up inventory

- From the `setup-autowas-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.

```
cp examples/inventory .
```
- Change the ansible_user in the inventory to match the target user you wish to run AutoWAS server
- Change the autowas_dir to a writable dir ( the play will create if it does not exist )
- Change the GSA credentials in the inventory 

## Run playbook


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory setup-autowas-play
```
