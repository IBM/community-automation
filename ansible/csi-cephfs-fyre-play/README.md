# Ansible Playbook for installing csi-cephfs onto Fyre OCP+Beta clusters.

## Overview

- Installs rook-cephfs from repository https://github.com/rook/rook.git onto your fyre inf node.
- Default rook-ceph release is `v1.5.9`.  See release information here https://github.com/rook/rook/releases. The use of `master` is also supported.
- Creates 3 storageClass
  - rook-cephfs - File store (RWX)
  - rook-ceph-block - Ceph Block storage (RWO)
  - csi-cephfs - For backward compatability to earlier versions of rook-ceph. This is the same storageclass as rook-cephfs.
- Sets csi-cephfs as the default storageclass.

## Assumptions:

 - A healthy Fyre OCP+Beta OpenShift 4.4.3 cluster or later in running state.
 - The OCP cluster must have 3 master nodes and at least 3 worker nodes.
 - You must have a fyre root password for your cluster to access the inf node with-in your OCP cluster.
 - Each worker needs to have additional disks configure (/dev/vdb). The additional disk is what rook-ceph uses to allocate storage against.
   - `GUI CLUSTERS:` By default using the OCP+ GUI (fyre.ibm.com) to create your cluster you will get a 200G /dev/vdb additional disk on each worker.
   - `API CLUSTERS:`If using the OCP+ API to create your cluster be sure to have additional disks specified for your workers.
     - "additional_disk": [ "200" ]


## Setting up inventory

- From the `csi-cephfs-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `fyre.inf.node.9dot.ip` variable in the `inventory` file with the 9dot ip of the inf node in your fyre OCP+Beta cluster.
- Modify `fyre.root.pw` variable in the `inventory` file  with your fyre root password.

```
cp examples/inventory .
```

## Run playbook


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory csi-cephfs.yml
```
or to pass a new rook-ceph release

```
ansible-playbook  -i inventory csi-cephfs.yml --extra-vars "rook_cephfs_release=v1.5.9"
```
or to get the master release

```
ansible-playbook  -i inventory csi-cephfs.yml --extra-vars "rook_cephfs_release=master"
```
or set new default storageclass to something other than csi-cephfs

```
ansible-playbook  -i inventory csi-cephfs.yml --extra-vars "default_sc=rook-cephfs"
```

or pass Docker registry authentication. Note that the `registry` variable must be specified in order for the playbook to setup the 
ImagePullSecret.
```
ansible-playbook  -i inventory csi-cephfs.yml --extra-vars "registry=docker.io registry_user=MYUSER registry_pwd=MYPASSWORD"
```
Additionally if you have special characters in your variables (as is common with passwords) consider using a JSON or YAML file and 
referencing it as below
```
ansible-playbook  -i inventory csi-cephfs.yml --extra-vars "@registry.json"
```
`registry.json`:
```
{
  "registry": "docker.io",
  "registry_user": "MYUSER",
  "registry_pwd": "MYPASSWORD"
}
```

License
-------

See LICENCE.txt
