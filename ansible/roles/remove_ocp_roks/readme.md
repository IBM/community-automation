remove_ocp_roks
==============

role used to delete an IBM Cloud ROKS cluster

-----------

Requirements
-----------

1. The "ibm.cloudcollection". Version 1.8.2 is currently known to work. Newer versions are known to cause issues with the embedded roles. To install: `ansible-galaxy collection install ibm.cloudcollection`. You can also use the "requirements.yml" file located in 'ansible/request-ocp-roks-play'. 
2. IBM-Cloud terraform-provider-ibm v1.9.0
3. Terraform v0.12.20

Role Variables
-------------

| Name              | Description                            | Required | Type                   |
|-------------------|----------------------------------------|----------|------------------------|
| clusterName       | Name of the new cluster                | Yes      | string                 |
| dataCenter        | IBM Cloud zone / data center           | Yes      | string                 |
| apikey            | IBM IAM API Key with create rights     | Yes      | string                 |
| resourceGroup     | Name of resource group to use          | No       | string                 |
| hardware          | Shared or Dedicated hardware option    | No       | default: shared        |

Additional Variable Information
----------

* dataCenter: This maps to the IBM Cloud Zone or datacenter to deploy to. Find options through the command line `ibmcloud cs zone ls --provider classic`
* apikey: IBM Cloud IAM API key is required to provision. See the following documentation: [API Key Information](https://cloud.ibm.com/docs/openshift?topic=openshift-users#api_key)
* dataCenter: This is the 5 character zone id for IBM Cloud (i.e. dal10). To see zones available use the IBM Cloud CLI `ibmcloud cs zones --provider classic`

Example Play
----------

    ---
    - hosts: localhost
      vars:
        ansible_python_interpreter: /usr/bin/python3
        clusterName: newclustername # Provide a unique cluster name
        dataCenter: wdc04 # Provide the data center (zone) to deploy to
        hardware: shared # shared for virtual workers
        resourceGroup: default # Provide the Resouce Group name where the cluster is deployed -- default is "default" resource group
        apikey: 1234567890123456 # Set the api key here to use for IBM Cloud authentication
      collections:
        - ibm.cloudcollection

      tasks:
      - name: delete roks cluster
        import_role: 
          name: remove_ocp_roks

Removing a cluster through an Ansible Container
-----------

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

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Add author
