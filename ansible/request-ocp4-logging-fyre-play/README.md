# Ansible Playbook for installing ocp logging on OCP 4.x clusters

## Overview

- Will install csi-csephfs (v1.3.8) onto an OCP+Beta 4.x cluster and will set the csi-cephfs storageclass as the default.
- Will install OCP logging onto the same fyre OCP+Beta 4.x cluster , and use the csi-cephfs storageclass for elasticsearch PVC creation.

## Requirements

  - A running fyre OCP+Beta cluster (16CPU/32GMem) with 3 workers that have an additional disk on each worker of at least 300G for elasticsearch PVC creation. (You must use the request-ocp-fyre-play or the OCP+Beta API https://w3.ibm.com/w3publisher/fyre/ocp/ocp-apis to create clusters with additional disks to meet this requirement ). See API example file examples/examplefyreAPIjson.
  - Ansible 2.9 or later installed with python3.
  - oc client installed.
  - oc login to OCP cluster performed.


## How to install oc client

  - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
  - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
  - Extract: tar xf oc.tar.gz
  - Move to /usr/local/bin: cp oc /usr/local/bin
  - Example oc login: `oc login https://api.walt454fmt3.cp.fyre.ibm.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`


### Setting up inventory

Make use of sample file at `examples/inventory` (no changes needed).

```
cp examples/inventory .
```

## Run playbook

#### Setting up variables for playbook

Make use of the sample file at `examples/ocp_logging_fyre_vars.yml`. Modify the values as per your cluster. See comments in file.

```
cp examples/ocp_logging_fyre_vars.yml .
```

Once you have configured the vars file, run the playbook using:

```
ansible-playbook  -i inventory -e @ocp_logging_fyre_vars.yml request-ocp4-logging-fyre.yml
```

License
-------

See LICENCE.txt
