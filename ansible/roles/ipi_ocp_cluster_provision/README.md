# Provision cluster using IPI installer

This role can be used to provision OCP clusters using the IPI Installer.

## Defaults

```yaml
# Master nodes 
"MASTER_CPUS": "10"
"MASTER_MEMORY": "32768"
"MASTER_DISK_SIZE": "300"
"MASTER_COUNT": 3

# Worker nodes
"WORKER_COUNT": 3
"WORKER_CPUS": "16"
"WORKER_MEMORY": "73728"
"WORKER_DISK_SIZE": "200"
```

## Additional variables

These variables can be

```yaml
BASE_DOMAIN: "<your base domain>"
CLUSTER_NAME: "<cluster name>"
WORKER_VM_SIZE: "<aws VM size>" # (eg. m5.2xlarge )
MASTER_VM_SIZE: "<aws VM size>" # (eg. m5.2xlarge )
```
