# Ansible Playbook for registering tWAS Application Server to WebSphere Automation

## Assumptions:

 - WebShpere Automation configured

## Setting up inventory

- From the `wa-automation-register` directory copy the sample inventory file at `examples/inventory` to the  current directory.

```
cp examples/inventory .
```

## Run playbook

Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory parms TBD

```
