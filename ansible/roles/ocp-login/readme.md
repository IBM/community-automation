# OCP login
Used to login to OCP clusters prior to running command line tasks.  This play role will also install a copy of the oc client.

## Expects the following

- kubeadmin user
- kubeadmin password
- ocp api URL with port number  (example: "api.my-cluster.purple-chesterfield.com:6443")

## Variables used for tagging

- cluster_tags
- AWS_REGION
- cloud
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
