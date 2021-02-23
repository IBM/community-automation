nfs_client_provisioner_fyre
=========

This role utilizes the Kubernetes SIG's [Kubernetes NFS Subdir External Provisioner](https://github.com/kubernetes-sigs/nfs-subdir-external-provisioner) project to deploy an automatic provisioner for an existing NFS server.


Requirements
------------

* Cluster:
  * OpenShift version ">=4.5.x"
* NFS server: You can read more about configuring [NFS Servers](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/nfs-serverconfig). The OCP Private(Fyre) clusters comes with pre-baked NFS server.
* SCC requirements: The service account for the NFS automatic provisioner does not have the required permissions by default & it needs to be added to the  [hostmount-anyuid](https://www.openshift.com/blog/managing-sccs-in-openshift) SCC. This role automatically adds the SA to the `hostmount-anyuid`, however ensure that the cluster has the `hostmount-anyuid` scc. 


Role Variables
--------------

  * kubeadmin_user
  * kubeadmin_password
  * ocp_api_url "(example: "https://api.my-cluster.purple-chesterfield.com:6443")"
  * nfs_provisioner_namespace "existing or a new project name where the provisioner would be deployed"
  * storageClassName "A new storage class name. Please ensure that the name you provide does not conflict with an existing namespace."
  * infra_node_private_ip This is the privateIP of your bastion host on Fyre Cluster.
  
Dependencies
------------
* Ansible
  * ansible version ">=2.10.x"
  * `community.okd` collection
  * `community.k8s` collection
  * `ocp_request_token` role
  * `ocp_add_users_to_scc` role

Example Playbook
----------------

    - hosts: localhost
      roles:
         - { role: nfs_client_provisioner_fyre }
         
License
-------

See [LICENCE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Rahul Tripathi (rahul.tripathi@ibm.com)  