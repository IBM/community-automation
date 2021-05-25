# OCP login
Used to login to OCP clusters prior to running command line tasks.  This play role will also install a copy of the oc client.

## Expects the following variables

- kubeadmin_user
- kubeadmin_password
- ocp_api_url   (example: "api.my-cluster.purple-chesterfield.com")
- ocp_api_port ( OPTIONAL, defaults to 6443 )
- kubeconfig_location ( OPTIONAL, default $HOME/.kube )
