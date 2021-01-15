# Ansible Playbook for configuring target operation systems with pre-reqs for a product

## Assumptions:

- Fyre systems do not have unzip. This is the basic install of that package
- Check the roles/osprereqs/tasks/*.yml to review the actual list of packages

## Setting up inventory

- From the `osprereq-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `hosts` to match your target hosts

```
cp examples/inventory .
```

## Run playbook

The playbook/role supports  RedHat8 / SLES / Ubuntu x64 or ppc64le


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory osprereqs-play.yml

```
