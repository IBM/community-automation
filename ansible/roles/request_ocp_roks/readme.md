# createROKSCluster ansible role

> role used to generate a new IBM Cloud ROKS cluster

## Requirements 

1. The "ibm.cloudcollection". Version 1.28.0 is currently known to work. To install: `ansible-galaxy collection install ibm.cloudcollection`. You can also use the "requirements.yml" file located in 'ansible/request-ocp-roks-play'. 
2. IBM-Cloud terraform-provider-ibm v1.9.0
3. Terraform v0.12.20

## Variables

| Name              | Description                            | Required | Type                   |
|-------------------|----------------------------------------|----------|------------------------|
| clusterName       | Name of the new cluster                | Yes      | string                 |
| dataCenter        | IBM Cloud zone / data center           | Yes      | string                 |
| machineType       | IBM Cloud flavor to use                | Yes      | string                 |
| privateVLAN       | Private VLAN ID to use                 | Yes      | string                 |
| apikey            | IBM IAM API Key with create rights     | Yes      | string                 |
| resourceGroup     | Name of resource group to use          | No       | string                 |
| cloudregion       | IBM Cloud Region                       | No       | default: us-south      |
| hardware          | Shared or Dedicated hardware option    | No       | default: shared        |
| defaultPoolSize   | Number of workers to create            | No       | default: 2             |
| kubeVersion       | 4.3_openshift or IKS options           | No       | default: 4.3_openshift |
| publicVLAN        | Public VLAND ID to use, blank for none | No       | string                 |
| entitlement       | Set to 'cloud_pak' to use entitlement  | No       | string                 |
| icaccount         | IBM Cloud Account GUID                 | No       | string                 |

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

## Example Play

    ---
    - hosts: localhost
      vars:
        ansible_python_interpreter: /usr/bin/python3
        cloudregion: us-south # Provide the resource i.e. us-south to use
        clusterName: newclustername # Provide a unique cluster name
        dataCenter: wdc04 # Provide the data center (zone) to deploy to
        defaultPoolSize: 2 # Set the size of the default worker pool
        hardware: shared # shared for virtual workers
        kubeVersion: 4.4_openshift # kube version to use 
        machineType: b2c.4x16 # machine flavor to use
        privateVLAN: 1234567 # Private VLAN to use, must be available
        publicVLAN: 2345678 # Public VLAN to use, optional
        resourceGroup: default # Provide the Resouce Group name where the cluster is deployed -- default is "default" resource group
        icaccount: 1234567890123456 # Target the account to use
        entitlement: cloud_pak # Set entitlement to "cloud_pak" when deploying a cloud pak to the cluster otherwise you will be charged for OCP licenses
        apikey: 1234567890123456 # Set the api key here to use for IBM Cloud authentication
      collections:
        - ibm.cloudcollection

      tasks:
      - name: create roks cluster
        import_role: 
          name: request_ocp_roks

## Deploying a cluster through an Ansible Container

*Container Dockerfile that would include all tools necessary for running in a Docker container:*

```
FROM centos:7
# set up os and install ansible
RUN yum install -y epel-release && yum update -y && yum install git openssh-clients.x86_64 ansible.noarch -y
# below .keys - generate SSH Keys for client and server as these will be used to execute ansible
ADD .keys/client/id_rsa /root/.ssh/id_rsa
ADD .keys/client/id_rsa.pub /root/.ssh/id_rsa.pub
COPY .keys/server/ /root/.ssh/
# allows localhost ssh connectivity
RUN cat /root/.ssh/ssh_host_ecdsa_key.pub > /root/.ssh/known_hosts && cat /root/.ssh/ssh_host_ed25519_key.pub >> /root/.ssh/known_hosts && cat /root/.ssh/ssh_host_rsa_key.pub >> /root/.ssh/known_hosts && mkdir -p /runner
# below assumes you have terraform binary locally and install it
ADD terraform /usr/local/bin
# add kubernetes and ibmcloud modules to ansible
RUN chmod +x /usr/local/bin && ansible-galaxy collection install community.kubernetes && ansible-galaxy collection install ibmcloud.ibmcollection && yum install python3.x86_64 -y && pip3 install openshift

WORKDIR /runner
ENTRYPOINT [ "/usr/bin/ansible-playbook" ]
```

*Running in a container*

* Map the location of your playbook files and roles to the /runner directory
* Provide variables either as "extra vars" or in a file
* "apikey" must be included as one of the variables.

`docker run -it --rm -v <playbook directory>:/runner <image name> -i localhost -e "<variable name>=<value> <variable name>=<value> ..." <playbook name>`

