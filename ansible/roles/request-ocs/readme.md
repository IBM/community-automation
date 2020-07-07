# Request OCS Installs
This role installs OCS onto either AWS or VMware Clusters that meet the following requirements.

Credits
-------
 - Thanks to the CP4I team for providing the base ocs_install.sh (with slite modifications) script used by this role.

Requirements
------------

 - Running AWS or VMware cluster is needed.
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

    - ocs_channel: stable-4.4 # Channel to pull ocs from, it should match the OCP version.
    - ocs_bastion_setup_dir: ~/setup-files/ocs-setup # Working dir for running the ocs_install.sh
    - setdefault: false  # Make the ocs cephfs storageclass the default or not.


Example Playbook
----------------

    - name: Install ocs
      hosts: bastion
      roles:
      - request-ocs-common
