# AWS IPI install playbook

This playbook will install an OCP cluster using RH IPI installer on AWS cloud infrastructure.

## Variables

### Master nodes

The following are preset in the role defaults, but can be overwritten in aws-vars.yml or common-vars.yml

```yaml
"MASTER_CPUS": "10"
"MASTER_MEMORY": "32768"
"MASTER_DISK_SIZE": "300"
"MASTER_COUNT": 3
```

### Worker nodes

```yaml
"WORKER_COUNT": 3
"WORKER_CPUS": "16"
"WORKER_MEMORY": "73728"
"WORKER_DISK_SIZE": "200"
```

## Variable files

Variable files should be copied from examples folder and edited. See files for details

- common-vars.yml
- aws-vars.yml

## Inventory file

Copy inventory file from examples folder

- inventory

## Provision a cluster

```bash
# ansible-playbook -i inventory provision_cluster.yml
```

## Delete a cluster

```bash
# ansible-playbook -i inventory delete_cluster.yml
```
