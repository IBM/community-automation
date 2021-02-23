Ansible Playbook for installing NFS automation provisioner onto OCP Private(Fyre) clusters.
=========

## Overview
This playbook uses the `nfs_client_provisioner_fyre` role to deploy the [nfs-subdir-external-provisioner](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner) onto an on OCP-Fyre(Private Cloud) cluster. 

Assumptions:
------------

 - A healthy OpenShift 4.6.x cluster or later in running state.
 - Installed the collections by running the following command--> `ansible-galaxy collection install -r galaxy.yml`
 - Installed the [OpenShift Python Library](https://pypi.org/project/openshift/). You can install it by running this command: `pip3 install openshift`

## Setting up variables & pre-requisites

- From the `nfs-storageclass-openshift-fyre-play` directory copy the sample variables file at `nfs_sc_vars_example.yml` to the current directory.
- Modify `kubeadmin_user` variable in the `variables` file with the Kube/OCP admin user of you OCP cluster.
- Modify `kubeadmin_password` variable in the `variables` file with the Kube/OCP admin password of you OCP cluster.
- Modify `ocp_api_url` variable in the `variables` file with the OCP API url of you OCP cluster.
- Modify `nfs_provisioner_namespace` variable in the `variables` file with the namespace where you to install NFS client provisioner. It can either be a new(preferred) or existing namespace.
- Modify `storageClassName` variable in the `variables` file with a new storage class on your OCP cluster. Please *DO NOT* use an existing storage class name.
- Modify `infra_node_private_ip` variable in the `variables` file with the private IP of your infra(bastion) host.

## Run playbook


Once you have configured the `nfs_sc_vars.yml` file, run the playbook using:

```
ansible-playbook nfs-storageclass-openshift-fyre-play.yml  --extra-vars  "@./nfs_sc_vars.yml"
```

## Post install
You can use the `storageClassName`, provided in the variables file for dynamic pvc/pv provisioning.

License
-------

See [LICENCE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Rahul Tripathi (rahul.tripathi@ibm.com)  