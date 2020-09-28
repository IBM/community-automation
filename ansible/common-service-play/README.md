# Ansible Playbook for Common Services Installation

## Assumptions:

 - A healthy OpenShift 4 cluster in running state.
 - oc login has been completed to the Openshift cluster.
 - Running on Ubuntu or Mac.


 ## How to install oc client

   - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
   - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
   - Extract: tar xf oc.tar.gz
   - Move to /usr/local/bin: cp oc /usr/lcoal/bring
   - Example oc login: `oc login https://api.your-cluster.purple-chesterfield.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`

## Setting up inventory

Make use of sample file at `examples/inventory`.

```
cp examples/inventory .
```

## Run playbook

#### Setting up variables for playbook

Make use of the sample file at `examples/cs_vars.yml`. Defaults to using the Common Services stable-v1 channel. Modify the values as per your cluster needs. For more information refer to examples.

```
cp examples/cs_vars.yml .
```

Once you have configured (For general use no modifications are needed) the vars & inventory file, run the playbook using:

```
ansible-playbook  -i inventory -e @cs_vars.yml common-services.yml
```

License
-------

See LICENCE.txt
