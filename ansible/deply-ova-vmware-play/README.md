# Ansible Playbook for uploading a new rhcos vmware ova to a vCenter.

## Description
 - Downloads to the local ubuntu system a rhcos ova file.
 - Imports the ova file into a vCenter as a VM, for use as a VM template or clone.
 - Sets the storage to `thin` when importing the ova.
 - Sets the disk.EnableUUID=TRUE on the VM

## Assumptions:
 - Need to be on an ubuntu system, with ansible 2.9.9 or later and pyvmomi installed.
   - sudo apt-get update -y
   - sudo apt-get install ansible
   - sudo apt-get install -y python-pyvmomi

## Copy deploy_vmware_vars.yml from examples and configure with your values

```
cp examples/deploy_vmware_vars.yml .
```

## Copy inventory file from examples (no changes needed)

```
cp examples/inventory .
```

## Run playbook


Once you have configured the `deploy_vmware_vars.yml` file, run the playbook using:

```
ansible-playbook  -i inventory -e @deploy_vmware_vars.yml deploy-ova-vmware.yml
```
For debug run with -vvv
```
ansible-playbook  -vvv -i inventory -e @deploy_vmware_vars.yml deploy-ova-vmware.yml
```

License
-------

See LICENCE.txt
