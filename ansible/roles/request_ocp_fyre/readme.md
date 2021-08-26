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

## Custom URLS/Version

This role has support for deploying using some custom urls into Fyre:
e.g. 

```
- role: request_ocp_fyre
  clusterName: "myfirstcluster"
  fyre_ocptype=ocpplus
  ocpVersion=custom
  rhcos_version_path=pre-release/latest
  ocp_version_path=ocp-dev-preview/latest-4.7
```

The additional parms for custom installations basically fill in sub directories of the URLs. Following are the additional parms:
rhcos_version_path 

- In the URLs above this parm would replace a section of the api parms keranel_url, initramfs_url and metal_url URLs as follows:
```
"kernel_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-installer-kernel-x86_64"
"initramfs_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-installer-initramfs.x86_64.img"
"metal_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-metal.x86_64.raw.gz"
```
- ocp_version_path - In the URLs above this parm would replace a section of the api parms install_url and client_url as follows:
```
"install_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/<ocp_version_path>/openshift-install-linux.tar.gz"
"client_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/<ocp_version_path>/openshift-client-linux.tar.gz"
```

Getting the right combination of rhcos_version_path and ocp_version_path can take some work. So have a look on https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/ and https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ and pick the version path you want to try.
