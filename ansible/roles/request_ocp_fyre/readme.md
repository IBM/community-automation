# Request Fyre OCP 4.x cluster create.

This role will create an OCP cluster in Fyre.
- Expects ansible parm `clusterName=<name>`
- For OCP+Beta 4.x clusters it expects ansible parm `fyre_ocptype=ocpplus`.
  - Expects ansible parm `ocpVersion=<ocpVersion>` must match a version supported in fyre.ibm.com GUI OCP+Beta tab.
  - All OCP+beta clusters are created with an additional /dev/vdb 300G disk.  


Will it is expected to run on a host with the following hostvars set in inventory file:
- fyreuser
- fyreapikey

The role expects to be supplied:
 - clusterName
 - ocpVersion
 - fyre_ocp_inf_group (optional: defaults to 'ocpClusters')
 - fyre_addAnsibleHost (optional: defaults to true)
 - fyre_site (optional: defaults to svl)
 - fyre_group_id (options: default is 0, which will default to account setting )

Ansible controller machine should have an public ssh key available: ~/.ssh/id_rsa.pub

The roles behaves in the following way:
1) Will reuse an existing cluster if name matches (no changes will be reported in this event)
2) Requests and Wait for an OCP cluster to be fully deployed if one does not exist
3) Role will error if cluster fails to create in fyre
4) One of the following will happen
   a) If fyre_addAnsibleHost is true, An ansible host will be added to represent the inf node within the cluster. This node will be part of the supplied group
   b) If fyre_addAnsibleHost is false, The current ansible host will be update with information about the cluster.
5) No checking is performed to ensure that cluster matches ocpVersion

The following is an example of how to run the role.
```
- hosts: fyreApi
  roles:
  - role: request_ocp_fyre
    clusterName: "myfirstcluster"
    ocpVersion: "4.3"
```
