# Ansible Playbook for creating an ocp cluster on fyre.

## Overview
- All possible params can be found in [role defaults](../roles/request_ocp_fyre/defaults/main.yml)
- Will create an OCP 4.x cluster in fyre.
  - The `clusterName=` parm, name you want to give your cluster. Must be unique in fyre.
  - The `ssh_public_key_file=` parm, reference to your public ssh key use to access the INF server.
  - Using `fyre_ocptype=ocpplus` this will create a fyre `OCP+` 4.x cluster.
    - The `ocpVersion=` parm
      -  Set to the current versions available in the fyre.ibm.com GUI `OCP+` tab.
      -  Set to `custom` if you want to install a nightly or a patch level of a GA'd version. See the following  `Custom installations additional information` section on detail for doing `custom` installs.
    - All `OCP+` clusters are created with an additional /dev/vdb 300G disk on the worker nodes.
  - Using `fyre_ocptype=quickburn` this will create a fyre `OCP+` 4.x  cluster against the QuickBurn quota.
    - The `clusterName=` parm, name you want to give your cluster. Must be unique in fyre.
    - The `ocpVersion=` parm
      -  Set to the current versions available in the fyre.ibm.com GUI `QuickBurn` tab.    
    - The `quickburn_ttl=` time-to-live parm set to the number of hours you want the cluster to live. Default is `12` hours if not specified. Max value allowed is `36`.
    - The `quickburn_size=` cluster size parm set to either medium or large. For both `medium or large` the master nodes have cpu 8 and ram of 16G. Default is `medium` if not specified.
      - `medium` - workers are cpu 8 and ram 16G.
      - `large` - workers are cpu 16 and ram 32G.
    - All QuickBurn clusters are created with an additional /dev/vdb 200G disk on the worker nodes.
## Custom installations additional information
- Using the `custom` installation gives you a wide variety of installation options, so much so, that it can be very easy to not set correct values when using it. So to start we are going to give you some templates for installation that we think will be most useful and then follow with more detail for those that need something more.
 - Ansible call to install the stable patch level of OCP 4.7.0-rc.2 nightly
    - `ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=your47rc2clustername" -e "fyre_ocptype=ocpplus" -e "ocpVersion=custom" -e "rhcos_version_path=pre-release/latest" -e "ocp_version_path=ocp/4.7.0-rc.2"`
 - Ansible call to install the stable patch level of OCP 4.7 nightly
    - `ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=your47nightlyclustername" -e "fyre_ocptype=ocpplus" -e "ocpVersion=custom" -e "rhcos_version_path=pre-release/latest" -e "ocp_version_path=ocp-dev-preview/latest-4.7"`
  - Ansible call to install the stable patch level of OCP 4.6
    - `ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=your46clustername" -e "fyre_ocptype=ocpplus" -e "ocpVersion=custom" -e "rhcos_version_path=4.6/latest" -e "ocp_version_path=ocp/stable-4.6"`
  - Ansible call to install the stable patch level of OCP 4.5
    - `ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=your45clustername" -e "fyre_ocptype=ocpplus" -e "ocpVersion=custom" -e "rhcos_version_path=4.5/latest" -e "ocp_version_path=ocp/stable-4.5"`
- So for installations that the previous ansible call templates do not satisfy here are some additional points to understand.
  - The `custom` installation uses under the covers a fairly complicated API call that involves 5 URLs to get the information it needs to do a correct installation. Following are examples of the api_parm:URLs it uses for the latest nightly 4.7 installation.
    - "kernel_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/pre-release/latest/rhcos-installer-kernel-x86_64"
    - "initramfs_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/pre-release/latest/rhcos-installer-initramfs.x86_64.img"
    - "metal_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/pre-release/latest/rhcos-metal.x86_64.raw.gz"
    - "install_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp-dev-preview/latest-4.7/openshift-install-linux.tar.gz"
    - "client_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp-dev-preview/latest-4.7/openshift-client-linux.tar.gz"
  - The additional parms for `custom` installations basically fill in sub directories of the URLs. Following are the additional parms:
    - `rhcos_version_path` - In the URLs above this parm would replace a section of the api parms  keranel_url, initramfs_url and metal_url URLs as follows:
      - "kernel_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-installer-kernel-x86_64"
      - "initramfs_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-installer-initramfs.x86_64.img"
      - "metal_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/<rhcos_version_path>/rhcos-metal.x86_64.raw.gz"
    - `ocp_version_path`  - In the URLs above this parm would replace a section of the api parms install_url and client_url as follows:
      - "install_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/<ocp_version_path>/openshift-install-linux.tar.gz"
      - "client_url":"https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/<ocp_version_path>/openshift-client-linux.tar.gz"
  - Getting the right combination of `rhcos_version_path` and `ocp_version_path` can take some work. It is recommended to leave `rhcos_version_path` as one of the following versions and just do adjustments to the 'ocp_version_path'.
    - For OCP 4.7 nightly installations use `rhcos_version_path=pre-release/latest`   
    - For OCP 4.6 installations use `rhcos_version_path=4.6/latest`   
    - For OCP 4.5 installations use `rhcos_version_path=4.5/latest`

## Assumptions:

 - You have capacity in fyre
 - Fyre is online

## Setting up inventory

- From the `request-ocp-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `fyreuser` variable in the `inventory` file with the name of your fyre user (see https://fyre.ibm.com/account).
- Modify `fyreapikey` variable in the `inventory` file  with your fyre api key (see https://fyre.ibm.com/account).
- Optionally remove `ansible_python_interpreter: /usr/bin/python3` if you have issues with python discovery
```
cp examples/inventory .
```

## Run playbook

The playbook/role supports provisioning clusters at configurable ocpVersions and works with the OCP and OCP+ apis from fyre team
These are controlled by the ocpVersion and fyre_ocptype variables respectively.

Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=myClusterName" -e "ocpVersion=desiredVersion" -e "fyre_ocptype=ocpplus"
```

With ocp_var.yml file. Copy examples/ocp_vars_example.yml to current as ocp_vars.yml and run the playbook using:

```
ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=myClusterName" -e "ocpVersion=desiredVersion" -e "fyre_ocptype=ocpplus" -e  @ocp_vars.yml
```

## Run playbook for Quickburn

```
ansible-playbook  -i inventory request-ocp-fyre-play.yml -e "clusterName=myClusterName" -e "ocpVersion=desiredVersion" -e "fyre_ocptype=quickburn" -e "quickburn_size=medium/large" -e quickburn_ttl=hoursToLive"
```

This command will create an ocp plus cluster in fyre called myClusterName. If myClusterName already exists it will instead just define it to ansible.
