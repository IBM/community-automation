# Recover Stalled Maching config rollout
This play will attempt to recover the machine config that is not rolling out.  This often happens after an attempt to upgrade a cluster.

Requirements
------------   
 - Running OCP 4.x cluster

## How to retriever your machine config value
One enhancement would be to figure out how to automatically pick the newest machine config  
See NOTES below if you need to install oc client  
use the following to retrieve the master machine config  
```
oc get mc | grep rendered-master
```
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
copy examples/mc_vars.yml up one folder  
```
cp examples/mc_vars.yml .
```
Edit ```mc_vars.yml```
```
  kubeadmin_user: "kubeadmin"
  kubeadmin_password: <kubeadmin_password>
  ocp_api_url: <api_server>:6443
  arch: "linux"
  ocp_client_version: "4.3.0" # lookup client version here https://mirror.openshift.com/pub/openshift-v4/clients/ocp/
  machine_config: "<machine_config>
```

```
ansible-playbook -vv -i examples/inventory recover-machine-config.yml
```

## NOTES

### How to install oc client

- ocp client versions can be looked up here https://mirror.openshift.com/pub/openshift-v4/clients/ocp/
- Download for linux: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/ocp/<version>/linux/openshift-client-linux.tar.gz`
- Download for Mac: `curl -o oc.tar.gz https://mirror.openshift.com/pub/openshift-v4/clients/ocp/<version>/macosx/openshift-clien-mac.tar.gz`
- Extract: tar xf oc.tar.gz
- Move to /usr/local/bin: cp oc /usr/local/bin
- Example oc login: `oc login https://<api_host_name>:6443 --insecure-skip-tls-verify=true -u kubeadmin -p "<kubeadmin pw>"`
