# createROKSCluster ansible role

> role used to generate a new IBM Cloud ROKS cluster

## Variables

| Name              | Description                      | Required | Type              |
|-------------------|----------------------------------|----------|-------------------|
| resourceGroup     | Name of resource group to use    | No       | string            |
| cloudregion       | IBM Cloud Region                 | No       | default: us-south |
| machineType       | IBM Cloud flavor to use          | Yes      | string            |
| clusterName       | Name of the new cluster          | Yes      | string            |
| dataCenter        | IBM Cloud zone / data center     | Yes      | string            |
| hardware          | Shared or Dedicated hardware option | No    | default: shared   |
| defaultPoolSize   | Number of workers to create      | No       | default: 2        |
| kubeVersion       | 4.3_openshift or IKS options     | No       | default: 4.3_openshift |
| privateVLAN       | Private VLAN ID to use           | Yes      | string            |
| publicVLAN        | Public VLAND ID to use, blank for none | No | string            |

## Output

Registers variable: iccluster

## Example Play

    ---
    - hosts: localhost
      vars:
        ansible_python_interpreter: /usr/bin/python3
        cloudregion: "us-east"
        clusterName: "CLUSTERNAME"
        dataCenter: "wdc04"
        defaultPoolSize: 5
        hardware: shared
        kubeVersion: 4.3_openshift
        machineType: "c3c.32x64"
        privateVLAN: 1234567
        publicVLAN: 2345678
        resourceGroup: "RGNAME"
        workerCount: "5"
      collections:
        - ibmcloud.ibmcollection

      tasks:
        - import_role: 
            name: createROKSCluster
