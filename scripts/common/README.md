# Common Scripts

These scripts are intended to be used by a broad group of teams

## clone community repo

```
# git clone git@github.com/IBM/community-automation
```

## using docker/podman

A public docker image has been create with all prereq's for running playbooks.

Make sure docker or podman(RHEL 8) is installed and running on your workstation

**NOTES:**

- You may need to do a **docker logout** before you begin.
- default ssh keys are comming from your ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub

**Tested on MAC (big sur), Ubunutu 16.04,18.04,20.04, and RHEL 7/8**

## MAC, Ubuntu, and RHEL 7 users

```
# docker run -v /YOUR_REPO_PATH:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest
```

### calling with playbook, assumes all vars are set in vars files

```
# docker run -v /YOUR_REPO_PATH:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i YOUR-PLAY/inventory  YOUR_PLAYBOOK/playbook.yml"
```

### using param passing, a mix of vars files, and command line vars

```
# docker run -v /YOUR_REPO_PATH:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i YOUR-PLAY/inventory  YOUR_PLAYBOOK/playbook.yml -e \"var1=value1\" -e \"var2=value2\""
```

## RHEL 8

```
# podman run -v /YOUR_REPO_PATH:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest
```

### calling with playbook, assumes all vars are set in vars files

```
# podman run -v /YOUR_REPO_PATH:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i YOUR-PLAY/inventory  YOUR_PLAYBOOK/playbook.yml"
```

### using param passing, a mix of vars files, and command line vars

```
# podman run -v /YOUR_REPO_PATH:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i YOUR-PLAY/inventory  YOUR_PLAYBOOK/playbook.yml -e \"var1=value1\" -e \"var2=value2\
```

## Personal client VM prereq script

install-prereqs.sh is used to setup an ansible install client VM.   It will ensure the correct version of ansible is installed and it will add python3 and several python3 libraries.  After the script complete you should be able to run most of the existing ansible playbooks without any additional updates.  

**Tested on ubuntu 16.04,18.04,20.04 and RHEL 7/8**  
**NOTES:**

- non-root users will need sudo access
- you may need to do a **docker login**, if you see complaints about pull limits
- ssh keys that get copied to the container will default to ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub

```
# cd community-automation
# scripts/common/install-prereqs.sh

RHEL8
# cd community-automation
# scripts/common/install-prereqs.sh -u YOUR_REDHAT_USERNAME -p YOUR_REDHAT_PASSWOR