# Ansible Playbook for installing Instana agents 

## Assumptions:

- Instana hosting server

- Instana support for ppc64le / aix / s390x is a tar.gz.  This playbook presumes that a custom package has been created where inside the package is an OS supported jvm in : ./instana-agent/jvm/ or a working jvm in the path on the target host

-- custom package naming compatible with the ansible arch naming:

```

instana-agent-x86_64.tar.gz
instana-agent-ppc64le.tar.gz
instana-agent-s390x.tar.gz
instana-agent-chrp.tar.gz

```


## Restrictions:


## Setting up inventory

- UNIX: From the `install_instana_agent` directory copy the sample inventory file at `examples/inventory.unix.yml` to the  current directory.
- Windows: From the `install_instana_agent` directory copy the sample inventory file at `examples/inventory.windows.yml` to the  current directory.

```
cp examples/inventory.unix.yml ./inventory
```

or

```
cp examples/inventory.windows.yml ./inventory
```

## Run playbook

Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook -i inventory install_instana_agent.yml 

```

## Change / update the Instana agent zone

Set the instana_zone in the inventory, run the playbook using:

```
ansible-playbook -i inventory instana_agent_zone.yml

```
## Change the Instana agent Instana server backend

```
cp examples/inventory.switch.yml ./inventory
```

Set the Instana server info in the inventory, run the playbook using:

```
ansible-playbook -i inventory instana_agent_switch.yml

```
