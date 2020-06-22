#!/bin/bash

#oc login -u kubeadmin -p "$(cat /root/auth/kubeadmin-password)" https://api.$(hostname | cut -f1 -d'.' | rev | cut -f1 -d'-' --complement | rev).cp.fyre.ibm.com:6443 --insecure-skip-tls-verify=true

# Install git
sudo dnf install git-all -y
