# Ansible Playbook for installing ocp logging on OCP 4.x clusters

## Overview

- Install OCP logging onto an OCP 4.x clusters.

## Requirements

  - Running fyre OCP+Beta cluster.
  - Ansible 2.9 or later installed.
  - oc client installed.
  - oc login to OCP cluster performed.

## How to install oc client

  - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
  - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
  - Extract: tar xf oc.tar.gz
  - Move to /usr/local/bin: cp oc /usr/local/bin
  - Example oc login: `oc login https://api.evident-pika.purple-chesterfield.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`


### Setting up inventory

Make use of sample file at `examples/inventory` (no changes needed).

```
cp examples/inventory .
```

## Run playbook

#### Setting up variables for playbook

Make use of the sample file at `examples/ocp_logging_vars.yml`. Modify the values as per your cluster. See comments in file.

```
cp examples/ocp_transfer_vars.yml .
```

Once you have configured the vars file, run the playbook using:

```
ansible-playbook  -i inventory -e @ocp_logging_vars.yml request-ocp4-logging.yml
```

License
-------

See LICENCE.txt
