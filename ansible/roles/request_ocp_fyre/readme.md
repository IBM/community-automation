request_ocp_fyre
============

Create and ocp cluster on fyre infrastructure

-----------

- Expects ansible parm `clusterName=<name>`
- For OCP+ 4.x clusters it expects ansible parm `fyre_ocptype=ocpplus`.
  - Expects ansible parm `ocpVersion=<ocpVersion>` must match a version supported in fyre.ibm.com GUI OCP+Beta tab.
  - All OCP+ clusters are created with an additional /dev/vdb 300G disk.  

Set in inventory file:

- fyreuser
- fyreapikey

Role Variables
----------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| clusterName             | yes      |    | string               |                          |
| ocpVersion              | yes      |         |                 | 4.6.52                         |
| fyre_ocp_inf_group      | yes      | ocpClusters  |                 |                         |
| fyre_addAnsiblehost        | yes      | true  |  true, false                 |                         |
| fyre_site              | yes | svl | rtp, svl | |
| fyre_group_id          | yes | 0 | specify a different group number | 0 will used default account settings |

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

```yaml
- hosts: fyreApi
  roles:
  - role: request_ocp_fyre
    clusterName: "myfirstcluster"
    ocpVersion: "4.3"
```

Custom URLS/Version
-----------

This role has support for deploying using some custom urls into Fyre:
e.g.

```yaml
- role: request_ocp_fyre
  clusterName: "myfirstcluster"
  fyre_ocptype=ocpplus
  ocpVersion=custom
  rhcos_version_path=pre-release/latest
  ocp_version_path=ocp-dev-preview/latest-4.7
```

The additional params for custom installations basically fill in sub directories of the URLs. Following are the additional params:

```yaml
"kernel_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-installer-kernel-x86_64"
"initramfs_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-installer-initramfs.x86_64.img"
"metal_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-metal.x86_64.raw.gz"

"install_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/<ocp_version_path>/openshift-install-linux.tar.gz"
"client_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/<ocp_version_path>/openshift-client-linux.tar.gz"
```

Getting the right combination of rhcos_version_path and ocp_version_path can take some work. So have a look on https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/ and https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ and pick the version path you want to try.

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Walter Kraphol
Ray Ashworth (ashworth@us.ibm.com)
