# Extra Ansible Playbooks for OCP4

This repository consists of additional ansible playbooks for the following:

1. Deploy Common Services

To-do list:

2. Deploy Cloud Paks


## Assumptions:

 - A healthy OpenShift 4 cluster in running state.

## Setting up inventory

Make use of sample file at `examples/inventory`.

```
cp examples/inventory .
```

**IMPORTANT**: Run the playbooks by setting either all.yaml or specific playbook/variables environment file.

## 1. Run all playbooks

### Setting up variables

Make use of the sample file at `examples/all.yaml`. Modify the values as per your cluster.

```
cp examples/all.yaml .
```

#### Run the playbook

Once you have configured the vars & inventory file, run the playbook using:

```
ansible-playbook  -i inventory -e @all.yaml playbooks/main.yml
```

## 2. Run specific playbook

### Setting up variables

### Common Services playbook

Make use of the sample file at `examples/cs_vars.yaml`. Modify the values as per your cluster.

```
cp examples/cs_vars.yaml .
```

#### Use cs_vars.yaml

This section sets the variables for the cs playbook.

```
## ocp-cs vars
cs_install: < Set to true to enable Common Services playbook >
cs_setup_dir:  < Setup directory path >
cs_operator_name: < Name for operator subscription >
cs_project_name: < Namespace for installing Common Services operators >
cs_subscription_channel: < Update channel for operator subscription >
cs_subscription_strategy: < Approval stragergy for operator subscription >
cs_starting_csv: < Cluster Service Version for instaling Common Services >
cs_operand_list: < List of Common Services Operators to install >
storageclass_name: < StorageClass name > 
```

#### Run the playbook

Once you have configured the vars & inventory file, run the playbook using:

```
ansible-playbook  -i inventory -e @cs_vars.yaml playbooks/main.yml
```

License
-------

See LICENCE.txt

