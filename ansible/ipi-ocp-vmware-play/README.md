# Introduction

This playbook will deploy a cluster using the IPI installer on VMWare infrastructure.

## Requirements

- Assumes ansible 2.9 or higher

## Variable files

Sample variable files can be found in examples folder, should be copied to main play folder.

- vsphere-vars.yml - holds vsphere specific variables
- common-vars.yml - holds common variables
- aws-vars.yml - hold AWS Route53 DNS information

## Provision cluster

```bash
# ansible-playbook -i inventory provision-cluster.yml
```

## Delete cluster

```bash
# ansible-playbook -i inventory delete-cluster.yml
```
