# Request OCS Installs
This role installs OCS onto either AWS or VMware Clusters that meet the following requirements

The role expects to be supplied:
 - clusterName
 - ocpVersion
 - fyre_ocp_inf_group (optional: defaults to 'ocp-clusters')
 - fyre_site (optional: defaults to svl)


Ansible controller machine should have an public ssh key available: ~/.ssh/id_rsa.pub

The roles behaves in the following way:
1) Will reuse an existing cluster if name matches (no changes will be reported in this event)
2) Requests and Wait for an OCP cluster to be fully deployed if one does not exist
3) Role will error if cluster fails to create in fyre
4) An ansible host will be added to represent the inf node within the cluster. This node will be part of the supplied group
5) No checking is performed to ensure that cluster matches ocpVersion

The following is an example of how to run the role.
```
- hosts: fyreApi
  roles:
  - role: request-ocp-fyre
    clusterName: "myfirstcluster"
    ocpVersion: "4.3"
```
