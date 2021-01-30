# Common Scripts

These scripts are intended to be used by a broad group of teams

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
# scripts/common/install-prereqs.sh -u YOUR_REDHAT_USERNAME -p YOUR_REDHAT_PASSWORD
```

## using docker/podman

**MAC** users need to install docker to run this option

**NOTES:**

- On RHEL8 use podman
- You may need to do a **docker logout** before you begin.
- default ssh keys are comming from your ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub

**Tested on MAC (big sur), Ubunutu 16.04,18.04,20.04, and RHEL 7/8**

```
# docker run -v $repo_dir:community-automation -i -t quay.io/rayashworth/community-ansible:latest

NOTE: RHEL 8
# podman run -v $repo_dir:community-automation -i -t quay.io/rayashworth/community-ansible:latest

# if you setup the parameters for a play ahead of time, you can directly call the playbook

# docker run -v $repo_dir:/community-automation -v ~/.ssh:/root/.ssh -i -t community-ansible:latest ansible-playbook -i ansible/YOURE-PLAY/inventory  ansible/YOUR_PLAY/playbook.yml

NOTE: RHEL 8

# podman run -v $repo_dir:/community-automation -v ~/.ssh:/root/.ssh -i -t community-ansible:latest ansible-playbook ansible/YOUR_PLAY/inventory  ansible/YOUR_PLAY/playbook.yml
```
