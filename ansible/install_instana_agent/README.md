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

- Does not support Windoze

## Setting up inventory

- From the `install_instana_agent` directory copy the sample inventory file at `examples/inventory` to the  current directory.

```
cp examples/inventory .
```

## Run playbook

Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook -i inventory install_instana_agent.yml -e instana_host_port=my-instana.com:myport -e agent_key=yourAgentKey -e custom_agent_url=http://yourcustompackagehost.com/opt/custompackage/instana

```
