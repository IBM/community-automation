Ansible Playbook for installing DB2 Community Edition onto OCP clusters.
=========

## Overview
This playbook uses the `db2_fyre` roles to deploy the DB2 Community Edition version `11.5.5.0-cn1` onto an on OCP-Fyre(Private Cloud) cluster.

Assumptions:
------------

 - A healthy OpenShift 4.6.x cluster or later in running state.
 - The OCP cluster must have 3 master nodes and at least 3 worker nodes.
 - A storage class already installed on the cluster.
 - Installed the collections by running the following command--> `ansible-galaxy collection install -r galaxy.yml`
 - Installed the [OpenShift Python Library](https://pypi.org/project/openshift/). You can install it by running this command: `pip3 install openshift`

## Setting up variables & pre-requisites

- From the `db2-fyre-play` directory copy the sample variables file at `db2_vars_example.yml` to the  current directory.
- Modify `kubeadmin_user` variable in the `variables` file with the Kube/OCP admin user of you OCP cluster.
- Modify `kubeadmin_password` variable in the `variables` file with the Kube/OCP admin password of you OCP cluster.
- Modify `ocp_api_url` variable in the `variables` file with the OCP API url of you OCP cluster.
- Modify `db2_namespace` variable in the `variables` file with the namespace where you to install DB2. It can either be a new or existing namespace.
- Modify `storageClassName` variable in the `variables` file with an existing storage class on your OCP cluster. If you don't have a storage class you can use the [csi-cephfs-fyre-play](https://github.com/IBM/community-automation/tree/master/ansible/csi-cephfs-fyre-play) playbook to provision a storage class on your OCP fyre cluster.
- Modify `entitled_key` variable in the `variables` file with the IBM entitled. You can get the IBM entitled key by visiting this link--> https://myibm.ibm.com/products-services/containerlibrary)

## Run playbook


Once you have configured the `db2_vars.yml` file, run the playbook using:

```
ansible-playbook db2-fyre-play.yml --extra-vars  "@./db2_vars.yml"
```

## Post install
You can visit the [DB2 Knowledge Center](https://www.ibm.com/support/knowledgecenter/SSEPGG_11.5.0/com.ibm.db2.luw.welcome.doc/doc/welcome.html) for details on how to use DB2.


License
-------

See [LICENCE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Rahul Tripathi (rahul.tripathi@ibm.com)  