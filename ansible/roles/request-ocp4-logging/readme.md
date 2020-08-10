# Request install of ocp loggingon to a OCP4 cluster
This role will install using the ocp logging operator and operand to install on any OCP cluster.

Requirements
------------

 - Running OCP 4.x cluster
 - Ansible 2.9 or later.
 - oc client installed.
 - oc login to OCP cluster performed.


How to install oc client
------------------------

 - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
 - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
 - Extract: tar xf oc.tar.gz
 - Move to /usr/local/bin: cp oc /usr/lcoal/bring
 - Example oc login: `c login https://api.evident-pika.purple-chesterfield.com:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>`


Default parameters set in the defaults/main.yml
------------------

    - logging_bastion_setup_dir: ~/setup-files/transfer-setup
    - rendered_sc: <storageclass name> #Storageclass to use for ocp logging PVCs. If empty is specified then it will use designated default storageclass.
    - ocp_logging_version: <ocp logging version> #Ocp logging version. Default is 4.2

Example Playbook
----------------

    - name: Install OCP 4.x Logging on OCP Cluster
      hosts: bastion
      roles:
      - request-ocp4-logging
