# remove-ocp-roks-play

> Playbook to remove an IBM Cloud ROKS cluster

## Requirements

1. Depends on the role "remove-ocp-roks" included in this repo.
2. The "ibm.cloudcollection". Version 1.28.0 is currently known to work. To install: `ansible-galaxy collection install ibm.cloudcollection`. You can also use the "requirements.yml" file located in 'ansible/request-ocp-roks-play'. 
3. IBM-Cloud terraform-provider-ibm v1.28.0
4. Terraform v0.12.20

## Usage

1. To ensure the correct version of the ibm.cloudcollection collection is used run the following command to install: `ansible-galaxy collection install -r requirements.yml`
2. Copy examples/roks-vars.yml up one folder
   `cp examples/roks-vars.yml .`
3. Edit roks-vars.yml as needed (see documentation in the example roks-vars.yml file).
4. Execute the playbook: `ansible-playbook -i localhost remove-roks.yml`
    * Other options:
        * use -e to set variables from the command line like `-e clusterName=testcluster01`
        * use -v for verbose output (-vvv for more, -vvvv to enable connection debugging)

## Variables used in this Playbook and Role

| Name              | Description                            | Required | Type                   |
|-------------------|----------------------------------------|----------|------------------------|
| ansible_python_interpreter | Set to /user/bin/python3      | Yes      | string                 |
| apikey            | IBM IAM API Key with create rights     | Yes      | string                 |
| clusterName       | Name of the new cluster                | Yes      | string                 |
| dataCenter        | IBM Cloud zone / data center           | Yes      | string                 |
| hardware          | Shared or Dedicated hardware option    | No       | default: shared        |
| resourceGroup     | Name of resource group to use          | No       | string                 |

### Additional Variable Information

* dataCenter: This maps to the IBM Cloud Zone or datacenter to deploy to. Find options through the command line `ibmcloud cs zone ls --provider classic`
* apikey: IBM Cloud IAM API key is required to provision. See the following documentation: [API Key Information](https://cloud.ibm.com/docs/openshift?topic=openshift-users#api_key)

