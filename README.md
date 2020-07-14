# CloudPak Community Automation

## Introduction
This repo represents the Community Automation effort where teams can contribute automation to be shared with other teams.  We desided as a guild to use Jenkins and Ansible combination for our implementations.  Jenkins and Ansible details below.

## Play list
| play | Description | status | Comments |
|------|-------------|--------|----------|
|common-service-fyre-play|install csi-cephfs and common services on FYRE| Available | none |
|common-service-play|deploy common-services on any infrastructure|Available|none|
|csi-cephfs-fyre-play|deploy cephfs storage on your fyre cluster|Available | none|
|deploy-ova-vmware-play|deploy a new RHCOS template to VMWare|Available|none|
|request-ocp-fyre-play|deploy an OCP cluster on old fyre and fyre OCP+ beta|Availalbe|none|
|request-ocp-aws-play|deploy an OCP cluster on aws|WIP|none|
|request-ocp-roks-play|deploy an OCP cluster on roks|WIP|none|
|request-ocs-common-play|Install Openshift Container Storage|Available| none|
|recover-machine-config-play|Recover machine-config, not rolling out|WIP| none|

## Supporting Roles
| role | Description | status | Comments |
|------|-------------|--------|----------|
|ocp-login | used when OCP Login is needed for your play | Availalbe | will automatically install oc client |
|oc-client-install|installs oc command| Available | is automatic when using ocp-login role|

## Jenkins
[Community Jenkins Server](https://hyc-ibm-automation-guild-team-jenkins.swg-devops.com/)

## Ansible
[Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/index.html)

## Folder Structure
The folder structure was taken from the [ansible best practices document](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)


The following is a snippet to help understand the folder structure and how we are using it.  
We have plays and roles, and each are at the top level under ansible/.  
Play folders end in -play, while the machine role would contain the playname without "-play"    

There will be roles without a corresponding play folder, these roles would be common function that could be shared across plays

To ensure we can load the roles correctly you will notice a symbolic link to the top roles directory.  This is a work around until ansible collections become available.


```
└── ansible
    ├── LICENCE.txt
    ├── README.md
    ├── ansible.cfg
    ├── common-service-play
    │   ├── Jenkinsfile
    │   ├── README.md
    │   ├── common-services.yml
    │   ├── examples
    │   │   ├── cs_vars.yml
    │   │   └── inventory
    │   └── roles -> ../roles
    ├── recover-expired-certificates-play
    │   ├── Jenkinsfile
    │   ├── readme.md
    │   ├── recover-expired-certificates-play.yml
    │   └── roles -> ../roles
    ├── recover-machine-config-play
    │   ├── Jenkinsfile
    │   ├── readme.md
    │   ├── recover-machine-config-play.yml
    │   └── roles -> ../roles
    ├── request-ocp-aws-play
    │   └── roles -> ../roles
    ├── request-ocp-fyre-play
    │   └── roles -> ../roles
    ├── request-ocp-roks-play
    │   └── roles -> ../roles
    └── roles
        ├── common-services
        │   ├── README.md
        │   ├── defaults
        │   │   └── main.yml
        │   ├── tasks
        │   │   └── main.yml
        │   └── templates
        │       ├── cs-group.yaml.j2
        │       ├── cs-request.yaml.j2
        │       ├── cs-sub.yaml.j2
        │       ├── cs-validation.bash.j2
        │       └── opencloud-source.yaml.j2
        ├── ocp-login
        │   └── tasks
        │       ├── main.yml
        │       └── ocp-login.yml
        ├── recover-epxired-certificates
        │   ├── defaults
        │   │   └── main.yml
        │   ├── files
        │   ├── meta
        │   │   └── main.yml
        │   ├── tasks
        │   │   ├── main.yml
        │   │   └── recover-expired-certificates.yml
        │   ├── templates
        │   └── vars
        ├── recover-machine-config
        │   ├── defaults
        │   │   └── main.yml
        │   ├── files
        │   ├── meta
        │   │   └── main.yml
        │   ├── readme.md
        │   ├── tasks
        │   │   ├── main.yml
        │   │   └── recover-machine-config.yml
        │   ├── templates
        │   └── vars
        ├── request-ocp-aws
        │   ├── default
        │   ├── readme.md
        │   ├── tasks
        │   └── templates
        ├── request-ocp-fyre
        │   ├── defaults
        │   ├── readme.md
        │   ├── tasks
        │   └── templates
        └── request-ocp-roks
            ├── defaults
            ├── readme.md
            ├── tasks
            └── templates
```

# 
## Common Repositories

Terraform Automation (VMWare, AWS, Google, and Azure) 
https://github.ibm.com/ICP-DevOps/tf_openshift_4

Some useful tools (cluster recovery scripts)  
https://github.ibm.com/ICP-DevOps/tf_openshift_4_tools


## ROKS Automation
ROKS info being provided until an ansible solution can be worked out in this community repo  

DTEs ROKS Provisioning Tooling https://github.ibm.com/dte/roksprovisioning - See the README.md and I included an installer script to get started.

The following is used in the above repo for reference:

IBM Cloud Terraform Docker Image: https://hub.docker.com/r/ibmterraform/terraform-provider-ibm-docker/

IBM Cloud Terraform Documentation: https://cloud.ibm.com/docs/terraform?topic=terraform-getting-started
