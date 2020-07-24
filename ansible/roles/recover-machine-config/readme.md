# Revover Stalled Maching config rollout
This role installs OCS onto either AWS or VMware Clusters that meet the following requirements.

Requirements
------------   
 - Running OCP 4.x cluster

## How to retriever your machine config value
One enhancement would be to figure out how to automatically pick the newest machine config  
See NOTES below if you need to install oc client  
use ```oc get mc | grep rendered-master``` to retrieve the the newest machine config  
Example output: In this example you would pick the line that has 25d  
```
root@Rayvm:~# oc get mc | grep rendered-master
rendered-master-4bff23481df7ffec2aac45086963cb1b            8af4f709c4ba9c0afff3408ecc99c8fce61dd314   2.2.0             26d
rendered-master-9a7898d7927764206e4153259c675091            b6c95fea3987483780994c8a5809a6afd15a633d   2.2.0             25d
```

## Jenkins Job
You can run this play via our community jenkins server  
https://hyc-ibm-automation-guild-team-jenkins.swg-devops.com/job/cluster-ops/job/machin-config-recovery/job/master/build?delay=0sec

## Using Command line

### Variables
Edit ```examples/vars.yml``` 
```
  kubeadmin_user: "kubeadmin"
  kubeadmin_password: <kubeadmin_password>
  ocp_api_url: <api_server>:6443
  arch: "linux"
  ocp_client_version: "4.3.0"
  machine_config: "<machine_config>
```

```
ansible-playbook -vv -i examples/inventory -e @examples/vars.yml recover-machine-config.yml
```

## NOTES

### How to install oc client

- ocp client versions can be looked up here https://mirror.openshift.com/pub/openshift-v4/clients/ocp/
- Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/ocp/<version>/linux/openshift-client-linux.tar.gz`
- Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/ocp/<version>/macosx/openshift-clien-mac.tar.gz`
- Extract: tar xf oc.tar.gz
- Move to /usr/local/bin: cp oc /usr/local/bin
- Example oc login: `oc login https://<api_host_name>:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`
