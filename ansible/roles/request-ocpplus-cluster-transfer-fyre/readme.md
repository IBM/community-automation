# Request transfer of Fyre OCP cluster to email
This role transfers a fyre OCP+Beta cluster to a new user by IBM intranet email.

Requirements
------------

 - Running fyre OCP+Beta cluster
 - New owner needs to have a fyre account with allocation for OCP+Beta clusters.
 - Ansible 2.9 or later.

Default parameters set in the defaults/main.yml
------------------

    - transfer_bastion_setup_dir: ~/setup-files/transfer-setup
    - transfer_to_email: <transfer_to_user_email> #IBM Intranet email of person transfering fyre OCP cluster to.
    - cluster_name: <cluster_name> #Name of OCP cluster to transfer
    - cluster_kubeadmin_pw: <cluster_kubeadmin_pw> #kubeadmin password
    - fyre_user: <fyre_username> #Fyre API User name
    - fyre_api_key: <fyre_key> #FYre API key
    - ocp_url: <ocp_login_url>  # OCP login URL like https://console-openshift-console.apps.walturl45p.cp.fyre.ibm.com

Example Playbook
----------------

    - name: Transfer OCP+Beta Cluster
      hosts: bastion
      roles:
      - request-ocpplus-cluster-transfer-fyre
