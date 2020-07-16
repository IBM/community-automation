# Ansible Playbook for Installing the Common Services Catalog Source

## Overview

- This is for those that have a OCP 4.4.x or later cluster that may want to choose the Common Services Operands they wish to install and from which Catalog Source.
- It allows you to specify whether you want the IBM common services CatalogSource `latest` or `dev-latest`.
  - `latest` gives you the most recently released to quay.io IBM common services operator stable-v1 channel.
  - `dev-latest` gives you the most recent not released IBM common services operator beta and dev channels.

## Assumptions:

 - A healthy OCP 4.4.x or later cluster.
 - oc login has been completed to OCP cluster.
 - Running on linux.
 - There is no IBM common services CatalogSource pod already Running
   - Run `oc -n openshift-marketplace get pod | grep opencloud-operators`
   - There should be no pod returned from this command.

## How to install oc client

  - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
  - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
  - Extract: tar xf oc.tar.gz
  - Move to /usr/local/bin: cp oc /usr/lcoal/bring
  - Example oc login: `oc login https://api.dev_fyre.cp.fyre.ibm.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`


## Setting up inventory

Make use of sample file at `examples/inventory` (with no changes).

```
cp examples/inventory .
```

## Run playbook

#### Setting up variables for playbook

Make use of the sample file at `examples/cs_vars_fyre.yml`. Modify the values as per your cluster. For more information refer to comments in the file.

```
cp examples/cs_vars_fyre.yml .
```

Once you have configured the vars & inventory file, run the playbook using:

```
ansible-playbook  -i inventory -e @cs_cat_src_vars.yml common-services-cat-src.yml
```

License
-------

See LICENCE.txt
