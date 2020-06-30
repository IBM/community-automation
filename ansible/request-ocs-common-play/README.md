# Ansible Playbook for installing Openshift Container Storage on AWS, VMware and Fyre OCP+Beta Clusters

## Overvieww

- Installs `Openshift Contianer Storage 4.4` onto a AWS and VMware.

## Requirements

  - oc login has been completed to AWS or VMware cluster.
  - Running on Ubuntu or Mac.
    - jq is install on the host box.
  - OCP cluster version matches OCS version.
  - Min required CPUs across all OCP cluster workers must be 48.
  - Min mem required 64GB per worker
  - Min cluster storage availability of 6.5 TB on VMware thin and AWS gp2 storage.

## How to install oc client

  - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
  - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
  - Extract: tar xf oc.tar.gz
  - Move to /usr/local/bin: cp oc /usr/local/bin
  - Example oc login: `oc login https://api.evident-pika.purple-chesterfield.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`


## Setting up inventory

Make use of sample file at `examples/inventory` (no changes needed).

```
cp examples/inventory .
```

## Run playbook

#### Setting up variables for playbook

Make use of the sample file at `examples/ocs_vars.yml`. Modify the values as per your cluster.

```
cp examples/ocs_vars.yml .
```

Once you have configured the vars file, run the playbook using:

```
ansible-playbook  -i inventory -e @ocs_vars.yml request-ocs-common.yml
```

License
-------

See LICENCE.txt
