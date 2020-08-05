# Ansible Playbook for installing csi-cephfs onto Fyre OCP+Beta clusters.

## Overview

- Installs rook-cephfs from repository https://github.com/rook/rook.git onto your fyre inf node.
- Default rook-ceph release is v1.3.8 from https://github.com/rook/rook/releases.
- Creates 3 storageClass
  - rook-cephfs - File store (RWX)
  - rook-ceph-block - Ceph Block storage (RWO)
  - csi-cephfs - For backward compatability to earlier versions of rook-ceph. This is the same storageclass as rook-cephfs.
- Sets csi-cephfs as the default storageclass.

## Assumptions:

 - A healthy Fyre OCP+Beta OpenShift 4.4.3 cluster or later in running state.
 - The OCP cluster must have 3 master nodes and at least 3 worker nodes.
 - You must have a fyre root password for your cluster to access the inf node with-in your OCP cluster.

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
ansible-playbook  -i inventory csi-cephfs.yml --extra-vars "rook_cephfs_release=v1.3.8"
```

License
-------

See LICENCE.txt
