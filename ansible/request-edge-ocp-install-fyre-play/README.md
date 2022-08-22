# Ansible Playbook for creating an ocp with common-services cluster on fyre.

## Overview
- Will create an OCP+beta cluster in fyre. See OCP+Beta cluster additional information.
- Will install `csi-cephfs` onto the OCP+Beta cluster.
  - Installs rook-cephfs from repository https://github.com/rook/rook.git onto your fyre inf node.
    - Will use the /dev/vdb drive on every worker node for csi-cephfs.
    - Uses the default rook-ceph release v1.3.8. See release information here https://github.com/rook/rook/releases.
    - Creates 3 storageClass
      - `rook-cephfs` - File store (RWX)
      - `rook-ceph-block` - Ceph Block storage (RWO)
      - `csi-cephfs` - For backward compatability to earlier versions of rook-ceph. This is the same storageclass as rook-cephfs.
    - Sets csi-cephfs as the default storageclass.
- Will install the current stable-v1 Common Services onto the OCP-Beta cluster.

## OCP+Beta cluster additional information
- The `ocpVersion=` parm
  -  Set to the current versions available in the fyre.ibm.com GUI OCP+Beta tab.
  -  Set to `custom` if you want to install a nightly or a patch level of a GA'd version. See following section on detail for doing `custom` installs.
- All OCP+beta clusters are created with an additional /dev/vdb 300G disk.  
## Custom installations additional information
- Using the `custom` installation gives you a wide variety of installation options, so much so, that it can be very easy to not set correct values when using it. So to start we are going to give you some templates for installation that we think will be most useful and then follow with more detail for those that need something more.
  - Ansible call to install the latest OCP 4.6 nightly
    - `ansible-playbook  -i inventory request-ocp-cs-install.yml -e "clusterName=your46clustername" -e "ocpVersion=custom" -e "rhcos_version_path=pre-release/latest" -e "ocp_version_path=ocp-dev-preview/latest-4.6"`
  - Ansible call to install the stable patch level of OCP 4.5
    - `ansible-playbook  -i inventory request-ocp-cs-install.yml -e "clusterName=your45clustername" -e "ocpVersion=custom" -e "rhcos_version_path=4.5/latest" -e "ocp_version_path=ocp/stable-4.5"`
  - Ansible call to install the stable patch level of OCP 4.4
    - `ansible-playbook  -i inventory request-ocp-cs-install.yml -e "clusterName=your44clustername" -e "ocpVersion=custom" -e "rhcos_version_path=4.4/latest" -e "ocp_version_path=ocp/stable-4.4"`
- So for installations that the previous ansible call templates do not satisfy here are some additional points to understand.
  - The `custom` installation uses under the covers a fairly complicated API call that involves 5 URLs to get the information it needs to do a correct installation. Following are examples of the api_parm:URLs it uses for the latest nightly 4.6 installation.
    - "kernel_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/pre-release/latest/rhcos-installer-kernel-x86_64"
    - "initramfs_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/pre-release/latest/rhcos-installer-initramfs.x86_64.img"
    - "metal_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/pre-release/latest/rhcos-metal.x86_64.raw.gz"
    - "install_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp-dev-preview/latest-4.6/openshift-install-linux.tar.gz"
    - "client_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp-dev-preview/latest-4.6/openshift-client-linux.tar.gz"
  - The additional parms for `custom` installations basically fill in sub directories of the URLs. Following are the additional parms:
    - `rhcos_version_path` - In the URLs above this parm would replace a section of the api parms  keranel_url, initramfs_url and metal_url URLs as follows:
      - "kernel_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-installer-kernel-x86_64"
      - "initramfs_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-installer-initramfs.x86_64.img"
      - "metal_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-metal.x86_64.raw.gz"
    - `ocp_version_path`  - In the URLs above this parm would replace a section of the api parms install_url and client_url as follows:
      - "install_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/<ocp_version_path>/openshift-install-linux.tar.gz"
      - "client_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/<ocp_version_path>/openshift-client-linux.tar.gz"
  - Getting the right combination of `rhcos_version_path` and `ocp_version_path` can take some work. It is recommended to leave `rhcos_version_path` as one of the following versions and just do adjustments to the 'ocp_version_path'.
    - For OCP 4.6 installations use `rhcos_version_path=pre-release/latest`
    - For OCP 4.5 installations use `rhcos_version_path=4.5/latest`   
    - For OCP 4.4 installations use `rhcos_version_path=4.4/latest`

## Assumptions:

 - You have capacity in fyre
 - Fyre is online

## Setting up vars file and inventory
- From the `request-ocp-cs-install-fyre-play` directory copy the sample inventory file at `examples/cs_vars_fyre.yml` to the  current directory.
- From the `request-ocp-cs-install-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
  - Modify `fyreuser` variable in the `inventory` file with the name of your fyre user (see https://fyre.ibm.com/account).
  - Modify `fyreapikey` variable in the `inventory` file  with your fyre api key (see https://fyre.ibm.com/account).
  - Optionally remove `ansible_python_interpreter: /usr/bin/python3` if you have issues with python discovery
```
cp examples/cs_vars_fyre.yml .
cp examples/inventory .
```

## Run playbook

The playbook/role supports provisioning clusters with OCP+ apis from fyre team.
These are controlled by the ocpVersion and fyre_ocptype variables respectively.

Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory request-ocp-cs-install.yml -e "clusterName=myClusterName" -e "ocpVersion=desiredVersion"
```

This command will create an ocp plus cluster in fyre called myClusterName. If myClusterName already exists it will instead just define it to ansible.
