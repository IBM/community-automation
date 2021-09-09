# request-ocp-roks-play

> Playbooks to create or remove an IBM Cloud ROKS cluster

## Requirements

1. Depends on the roles "request-ocp-roks" and "remove-ocp-roks" included in this repo.
2. The "ibm.cloudcollection". Version 1.28.0 is currently known to work. To install: `ansible-galaxy collection install ibm.cloudcollection`. You can also use the "requirements.yml" file located in 'ansible/request-ocp-roks-play'. 
3. IBM-Cloud terraform-provider-ibm v1.28.0
4. Terraform v0.12.20

## Usage

### Create ROKS Cluster
1. To ensure the correct version of the ibm.cloudcollection collection is used run the following command to install: `ansible-galaxy collection install -r requirements.yml`
2. Copy examples/roks-vars.yml up one folder
   `cp examples/request-roks-vars.yml .`
3. Edit roks-vars.yml as needed (see documentation in the example roks-vars.yml file).
4. Execute the playbook: `ansible-playbook -i localhost request-roks.yml`
    * Other options:
        * use -e to set variables from the command line like `-e clusterName=testcluster01`
        * use -v for verbose output (-vvv for more, -vvvv to enable connection debugging)

### Delete ROKS Cluster
1. To ensure the correct version of the ibm.cloudcollection collection is used run the following command to install: `ansible-galaxy collection install -r requirements.yml`
2. Copy examples/roks-vars.yml up one folder
   `cp examples/remove-roks-vars.yml .`
3. Edit roks-vars.yml as needed (see documentation in the example roks-vars.yml file).
4. Execute the playbook: `ansible-playbook -i localhost remove-roks.yml`
    * Other options:
        * use -e to set variables from the command line like `-e clusterName=testcluster01`
        * use -v for verbose output (-vvv for more, -vvvv to enable connection debugging)

## Variables used in these Playbooks and Roles

| Name              | Description                            | Required | Type                   |
|-------------------|----------------------------------------|----------|------------------------|
| ansible_python_interpreter | Set to /user/bin/python3      | Yes      | string                 |
| apikey            | IBM IAM API Key with create rights     | Yes      | string                 |
| cloudregion       | IBM Cloud Region                       | No       | default: us-south      |
| clusterName       | Name of the new cluster                | Yes      | string                 |
| dataCenter        | IBM Cloud zone / data center           | Yes      | string                 |
| defaultPoolSize   | Number of workers to create            | No       | default: 2             |
| entitlement       | Set to 'cloud_pak' to use entitlement  | No       | string                 |
| hardware          | Shared or Dedicated hardware option    | No       | default: shared        |
| icaccount         | IBM Cloud Account GUID                 | No       | string                 |
| kubeVersion       | 4.5_openshift or IKS options           | No       | default: 4.5_openshift |
| machineType       | IBM Cloud flavor to use                | Yes      | string                 |
| privateVLAN       | Private VLAN ID to use                 | Yes      | string                 |
| publicVLAN        | Public VLAND ID to use, blank for none | No       | string                 |
| resourceGroup     | Name of resource group to use          | No       | string                 |

### Additional Variable Information

* dataCenter: This maps to the IBM Cloud Zone or datacenter to deploy to. Find options through the command line `ibmcloud cs zone ls --provider classic`
* machineType: IBM Cloud specifies template machine specs supported in a cluster. Find options through the command line `ibmcloud cs flavors --provider classic --zone dal10`
* cloudregion: IBM Cloud region for the data center. Find options through the command line: `ibmcloud regions`
* kubeVersion: IBM Cloud specific version for Kubernetes or OpenShift clusters. Find options through the command line `ibmcloud cs versions`.
* privateVLAN: A private VLAN is required and must exist. VLAN options can be viewed in the UI or CLI. CLI: `ibmlcoud cs vlans --zone <zone name>`.
* publicVLAN: A public VLAN is required for inbound Internet access to the cluster. The VLAN must exist.
* apikey: IBM Cloud IAM API key is required to provision. See the following documentation: [API Key Information](https://cloud.ibm.com/docs/openshift?topic=openshift-users#api_key)
* icaccount: Add IBM Cloud Account GUID when API Key provided is used by multiple accounts.
* dataCenter: This is the 5 character zone id for IBM Cloud (i.e. dal10). To see zones available use the IBM Cloud CLI `ibmcloud cs zones --provider classic`

