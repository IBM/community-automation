# Common Scripts

These scripts are intended to be used by a broad group of teams

## clone community repo

```
# git clone git@github.com/IBM/community-automation
```

## using docker/podman

A public docker image has been create with all prereq's for running playbooks.  This option will give you a predefined local docker/podman environment to run all of the availalbe playbook's from.

Make sure docker or podman(RHEL 8) is installed and running on your workstation

**NOTES:**

- You may need to do a **docker logout** before you begin.
- default ssh keys are comming from your ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub

**Tested on MAC (big sur), Ubunutu 16.04,18.04,20.04, and RHEL 7/8**

## MAC, Ubuntu, and RHEL 7 users

### Creates a bash command line to the container ready to run playbooks

```
# docker run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest

EXAMPLE:
# docker run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest
```

### Calling with playbook, assumes all vars are set in vars files, exits the container when complete

```
# docker run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i <YOUR_PLAYBOOK_FOLDER>/inventory  <YOUR_PLAYBOOK_FOLDER>/playbook.yml"

EXAMPLE:
# docker run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i csi-cephfs-fyre-play/inventory  csi-cephfs-fyre-play/csi-cephfs.yml
```

### Using param passing, a mix of vars files, and command line vars, exits the container when complete

```
# docker run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i <YOUR_PLAYBOOK_FOLDER>/inventory  <YOUR_PLAYBOOK_FOLDER>/playbook.yml -e \"var1=value1\" -e \"var2=value2\""

EXAMPLE:
# docker run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i csi-cephfs-fyre-play/inventory  csi-cephfs-fyre-play/csi-cephfs.yml" -e \"rook_cephfs_release=v1.4.7\""
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
# podman run -v /<YOUR_REPO_ABSOLUTE_PATH>:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i <YOUR_PLAYBOOK_FOLDER>/inventory <YOUR_PLAYBOOK_FOLDER>/playbook.yml -e \"var1=value1\" -e \"var2=value2\""

EXAMPLE:
# podman run -v /Users/ashworth/projects/community-automation:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i csi-cephfs-fyre-play/inventory  csi-cephfs-fyre-play/csi-cephfs.yml" -e \"rook_cephfs_release=v1.4.7\""
```

## Personal client VM prereq script

install-prereqs.sh is used to setup an ansible install client VM.  It will ensure the correct version of ansible is installed and it will add python3 and several python3 libraries.  After the script complete you should be able to run most of the existing ansible playbooks (check playbook readme's for parameter details) without any additional updates.  

**Tested on ubuntu 16.04,18.04,20.04 and RHEL 7/8**  
**NOTES:**

- non-root users will need sudo access
- you may need to do a **docker login**, if you see complaints about pull rate limits
- ssh keys that get copied to the container will default to ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub

```
Ubuntu/RHEL7
# cd community-automation
# scripts/common/install-prereqs.sh
```

```
RHEL8
# cd community-automation
# scripts/common/install-prereqs.sh -u YOUR_REDHAT_USERNAME -p YOUR_REDHAT_PASSWOR
```
