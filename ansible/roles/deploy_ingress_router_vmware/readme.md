deploy_ingress_rounter_vmware: deploy an ingress router to every worker in the cluster. Only needed for vmware clusters where the worker nodes have public 9 dot IPs.
=========

Ansible role for enabling the ingress router on all cluster worker nodes.

Requirements:
------------

 - Need to be on an linux box or docker image that has run `community-automation/scripts/common/install-prereqs.sh`.

Example Playbook
----------------

    - name: Install ova to vCenter
      hosts: bastion
      roles:
      - deploy_ingress_router_vmware

License
-------

See LICENCE.txt
