# Jenkins

## Create your jenkins file

The "Jenkinsfile" should live in your top playbook folder  
Here is sample ( [Jenkinsfile-example](ansible/Jenkinsfile-example) ). You will update the paramList and the stage() sections. The rest is static for now.  
See existing playbooks for more complex examples

``` groovy
#! groovy

// Standard job properties
def jobProps = [
  buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '50')),
  disableResume(),
  durabilityHint("PERFORMANCE_OPTIMIZED"),
  [$class: 'RebuildSettings', autoRebuild: false, rebuildDisabled: false]
]

def paramsList = [
    string(name: 'API_Server_URL', defaultValue: "api.", description: 'clustre api server url'),
    string(name: 'API_Server_Port', defaultValue: "6443", description: 'clustrer api serfver port number'),
    string(name: 'cluster_admin', defaultValue: "kubeadmin", description: 'clustrer admin user'),
    password(name: 'cluster_admin_password', description: 'cluster admin password'),
    string(name: 'ocp_client_version', defaultValue: "4.2.0"),
    string(name: 'machine_config', description: 'machine config found from oc get mc, newest version')
  ]
jobProps.push(parameters(paramsList))

properties(jobProps)

timestamps {
  ansiColor('xterm') {
    node {

      checkout scm

      stage('Recover Machine Config') {
        sh """
          set +x # hide sensitive info being echo'd to log
          cp ./ansible/recover-machine-config-play/examples/mc_vars.yml ./ansible/recover-machine-config-play/;\
          cp ./ansible/recover-machine-config-play/examples/inventory ./ansible/recover-machine-config-play/;\
          ansible-playbook -i ./ansible/recover-machine-config-play/inventory \
          ./ansible/recover-machine-config-play/recover-machine-config-play.yml \
          -e kubeadmin_user=${params.cluster_admin} \
          -e kubeadmin_password=${params.cluster_admin_password} \
          -e ocp_api_url=${API_Server_URL}:${API_Server_Port} \
          -e arch="linux" \
          -e ocp_client_version=${ocp_client_version} \
          -e machine_config=${machine_config} -vv
        """.stripIndent()
      }
   }
  }
}
```

## Setting up your jenkins job

Must be in the community automation blue group (open and issue to request blue group access)

[Community Jenkins Server](https://hyc-ibm-automation-guild-team-jenkins.swg-devops.com/)  
Login to jenkins server  
Navigate to "**Cluster Ops**"  
Select "**New Item**" from left nav.  
Name your job.  
Select "**MultiBranch Pipeline**" from list.  
Enter "**community-pipeline-template**" in the "Copy from" field.  
Select "**OK**"

## Edit job settings

Select "**Single repository & branch**" from "**Add Source**" dropdown.  
Enter your branch name in the "**Name**" field.  Should be "master" most of the time.  
Update Credentials, using github username and token.  Working to get a FUNCTIONAL_ID.  
Under "**Build Configuration**" update "**Script Path**"  
Select "**Save**"
