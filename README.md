# Red Hat Openshift Container Platform (OCP) Community Automation

## Introduction

This repo represents the Red Hat Openshift Container Platform (OCP) Community Automation effort where teams can contribute ansible automation to be shared with other teams.  It was decided early on in the project to use Jenkins and Ansible combination for our implementations.  Jenkins and Ansible details below.  The repo is also setup for use as an ansible collection to be included in playbooks being created outside of this repo.  

This community is meant to be a place where developers can contribute to a library of ansible playbooks and/or roles related to Red Hat Openshift Container Platform (OCP), from installing OCP to post install activities.  It is the intent that these playbooks and roles can be reused by any team that is looking to automate their CI/CD pipeline.

## How to run playbooks

- clone this community-automation repository
- Run options
  - Docker image
  - importing the ansible collection  
  - Personal workspace (requires prereq [scripts](docs/scripts.md) found in scripts folder)

## Documentation

  - [prereq scripts](docs/scripts.md)
  - [Ansible Documentation](https://docs.ansible.com/ansible/latest/user_guide/index.html)
  - [Ansible-collection](docs/collection.md)
  - [Docker-Image](docs/docker-image.md)  
  - [Folder Structure](docs/folder-structure.md)  
  - [playbooks](docs/playbooks.md)
  - [roles](docs/roles.md)
  - [jenkinsfile](docs/jenkinsfile.md)
  - [non ansible scripts](scripts/README.md)
