# Docker Image Option

A public docker image has been create with all prereq's for running playbooks.

Make sure docker or podman(RHEL 8) is installed and running on your workstation

**NOTES:**

- You may need to do a **docker logout** before you begin.
- default ssh keys are coming from your ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub

**Tested on MAC (big sur), Ubunutu 16.04,18.04,20.04, and RHEL 7/8**

## MAC, Ubuntu, and RHEL 7 users

### Creates a bash command line to the container ready to run playbooks
```
# docker run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest

EXAMPLE:
# docker run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest
```

### Calling a playbook, assumes all vars are set in vars files, exits the container when complete

```
# docker run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i <YOUR_PLAYBOOK_FOLDER>/inventory  <YOUR_PLAYBOOK_FOLDER>/playbook.yml"

EXAMPLE:
# docker run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i csi-cephfs-fyre-play/inventory  csi-cephfs-fyre-play/csi-cephfs.yml"
```

### Using param passing, a mix of vars files, and command line vars, exits the container when complete

```
# docker run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i <YOUR_PLAYBOOK_FOLDER>/inventory  <YOUR_PLAYBOOK_FOLDER>/playbook.yml -e \"var1=value1\" -e \"var2=value1\""

EXAMPLE:
# docker run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i csi-cephfs-fyre-play/inventory  csi-cephfs-fyre-play/csi-cephfs.yml" -e "var1=value1"
```

## RHEL 8

### Creates a bash command line to the container ready to run playbooks

```
# podman run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest

EXAMPLE:
# podman run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest
```

### Calling with playbook, assumes all vars are set in vars files, exits the container when complete

```
# podman run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i <YOUR_PLAYBOOK_FOLDER>/inventory  <YOUR_PLAYBOOK_FOLDER>/playbook.yml"

EXAMPLE:
# podman run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i csi-cephfs-fyre-play/inventory  csi-cephfs-fyre-play/csi-cephfs.yml" 
```

### Using param passing, a mix of vars files, and command line vars, exits the container when complete

```
# podman run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i <YOUR_PLAYBOOK_FOLDER>/inventory  <YOUR_PLAYBOOK_FOLDER>/playbook.yml -e \"var1=value1\" -e \"var2=value2\"

EXAMPLE:
# podman run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i csi-cephfs-fyre-play/inventory  csi-cephfs-fyre-play/csi-cephfs.yml" -e \"rook_cephfs_release=v1.4.7\""
```

### Personal install client (VM)

**NOTE:** This only need to be run once.

From the repo home folder "community-automation", run the following command which will setup your person installer client with all of hte necessary prereqs to run playbooks. [README](https://github.com/IBM/community-automation/tree/master/scripts/common)  

```
# cd community-automation
# scripts/common/install-prereqs.sh

# RHEL 8
# cd community-automation
# scripts/common/install-prereqs.sh -u YOUR_RH_USERNAME -p YOUR_RH_PASSWORD
```
