csi_cephfs_vmware: csi cephfs  on vmware OCP cluster
=========

This module will install:
- rook-cephfs from repository https://github.com/rook/rook.git onto your vmware cluster.
- Default rook-ceph release is `v1.5.9`. See release information here https://github.com/rook/rook/releases.
- Creates 3 storageClass
  - rook-cephfs - File store (RWX)
  - block-storage - Ceph Block storage (RWO)
  - file-storage - For backward compatability to earlier versions of rook-ceph. This is the same storageclass as the rook-cephfs storageclass.
  - vsphere-block-storage - thin storage.
- Sets file-storage as the default storageclass.

Requirements
------------

 - Running vmware OCP cluster is needed.
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
- Install csi-cephfs on a vmware.

 - name: Install csi-cephfs
   hosts: bastion
   roles:
   - csi_cephfs_fyre


License
-------

See LICENCE.txt

Author Information
------------------

Walt Krapohl (krapohl@us.ibm.com)
