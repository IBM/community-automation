# Ansible Playbook for configuring target Fyre hosts for tWAS operations

## Assumptions:


## Setting up inventory

- From the `fix-fyre-hosts-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `hosts` to match your target hosts

```
cp examples/inventory .
```

## Run playbook

The playbook/role supports Fyre hosts


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory fix-fyre-hosts-play.yml

```
