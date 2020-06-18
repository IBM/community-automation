# Ansible Playbook for installing csi-cephfs onto Fyre OCP+Beta clusters.

## Assumptions:

 - A healthy Fyre OCP+Beta OpenShift 4.4.3 cluster or later in running state.
 - The OCP cluster must have 3 master nodes and at least 3 worker nodes.
 - You must have a fyre root password for your cluster to access the inf node with-in your OCP cluster.

## Setting up inventory

- From the `csi-cephfs-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `fyre.inf.node.9dot.ip` variable in the `inventory` file with the 9dot ip of the inf node in your fyre OCP+Beta cluster.
-Modify `fyre.root.pw` variable in the `inventory` file  with your fyre root password.

```
cp examples/inventory .
```

## Run playbook


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory csi-cephfs.yml
```

License
-------

See LICENCE.txt
