# Ansible Playbook for installing IBM Installation Manager

## Limitations:

- Support for user install 

## Setting up inventory

- From the `ibm_installation_manager_play` directory copy the sample inventory file at `examples/inventory` to the  current directory.

```
cp examples/inventory .
```
- Change the ansible_user in the inventory to match the target user you wish to install IBM Installation Manager

## Run playbook


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory ibm_installation_manager_play.yml

