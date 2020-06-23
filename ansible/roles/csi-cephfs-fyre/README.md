csi-cephfs: csi cephfs on OCP
=========

This module will install csi-cephfs on fyre OCP+Beta clusters version 4.4.3 or later.

Requirements
------------

 - Running fyre OCP+Beta cluster is needed.
 - oc client installed.
 - oc login to OCP cluster performed.
 - git client installed.

How to install oc clinet
------------------------
 - Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/linux/oc.tar.gz`
 - Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/oc/latest/macosx/oc.tar.gz`
 - Extract: tar xf oc.tar.gz
 - Move to /usr/local/bin: cp oc /usr/lcoal/bring
 - Example oc login: `oc login -u kubeadmin -p "<kubeadmin pw>" https://api.dev_fyre.cp.fyre.ibm.com:6443 --insecure-skip-tls-verify=true`

 How to install git client
 -------------------------
 - On Redhat: `sudo dnf install git-all -y`
 - On Ubuntu: `sudo apt install git-all`
 - On Mac: `https://git-scm.com/book/en/v2/Getting-Started-Installing-Git`

Example Playbook
----------------

    - name: Install csi-cephfs
      hosts: bastion
      roles:
      - csi-cephfs-fyre

License
-------

See LICENCE.txt

Author Information
------------------

Walt Krapohl (krapohl@us.ibm.com)
