# Ansible Playbook for Fyre OCP+Beta Cluster Common Services Installation

## Assumptions:

 - A healthy Fyre OCP+Beta OpenShift 4.4.6 or later cluster in running state.
 - oc login has been completed to fyre cluster.


## How to install oc client

  - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
  - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
  - Extract: tar xf oc.tar.gz
  - Move to /usr/local/bin: cp oc /usr/lcoal/bring
  - Example oc login: `oc login https://api.dev_fyre.cp.fyre.ibm.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`


## Setting up inventory

Make use of sample file at `examples/inventory`.

```
cp examples/inventory .
```

## Run playbook

#### Setting up variables for playbook

Make use of the sample file at `examples/cs_vars.yml`. Modify the values as per your cluster. For more information refer to examples.

```
cp examples/cs_vars_fyre.yml .
```

Once you have configured the vars & inventory file, run the playbook using:

```
ansible-playbook  -i inventory -e @cs_vars_fyre.yml common-services-fyre.yml
```

License
-------

See LICENCE.txt
