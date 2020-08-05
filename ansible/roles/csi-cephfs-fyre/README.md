csi-cephfs: csi cephfs on OCP
=========

This module will install:
- rook-cephfs from repository https://github.com/rook/rook.git onto your fyre inf node.
- Default rook-ceph release is v1.3.8. See release information here https://github.com/rook/rook/releases.
- Creates 3 storageClass
  - rook-cephfs - File store (RWX)
  - rook-ceph-block - Ceph Block storage (RWO)
  - csi-cephfs - For backward compatability to earlier versions of rook-ceph. This is the same storageclass as the rook-cephfs storageclass.
- Sets csi-cephfs as the default storageclass.

Requirements
------------

 - Running fyre OCP+Beta cluster is needed.
 - oc client installed.
 - oc login to OCP cluster performed.
 - git client installed.

How to install oc client
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
- Install csi-cephfs on a fyre cluster before Common Services.

 - name: Install common services
   hosts: bastion
   roles:
   - csi-cephfs-fyre
   - common-services


License
-------

See LICENCE.txt

Author Information
------------------

Walt Krapohl (krapohl@us.ibm.com)
