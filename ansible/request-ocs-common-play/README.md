# Ansible Playbook for installing Openshift Container Storage on AWS, VMware and Fyre OCP+Beta Clusters

## Overvieww

- Installs `Openshift Contianer Storage 4.4` onto a AWS, VMware and Fyre OCP+Beta Baremetal clusters.
  - Min required CPUs across all workers must be 48.
  - Min require 
    - Use this command to figure this out if you don't know ``
  - Creates file storage (rwo/rwx)  storageclass called `csi-cephfs` as the default storageclass.
  - Creates block storageclass (rwo/rwx) `rook-ceph-block`
- Installs `common-services` 3.4.1 GA by default.

## Assumptions:

 - A healthy Fyre OCP+Beta OpenShift 4.4.6 or later cluster in running state.
 - oc login has been completed to fyre cluster.
 - Running on Ubuntu or Mac.


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

Make use of the sample file at `examples/cs_vars_fyre.yml`. Modify the values as per your cluster. For more information refer to examples.

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
