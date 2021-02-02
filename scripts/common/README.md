# Common Scripts

These scripts are intended to be used by a broad group of teams

## clone community repo

```
# git clone git@github.com/IBM/community-automation
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
# scripts/common/install-prereqs.sh -u YOUR_REDHAT_USERNAME -p YOUR_REDHAT_PASSWORD
```

## using docker/podman

**MAC/RHEL7** users need to install docker to run this option

**NOTES:**

- On RHEL8 use podman
- You may need to do a **docker logout** before you begin.
- default ssh keys are comming from your ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub

**Tested on MAC (big sur), Ubunutu 16.04,18.04,20.04, and RHEL 7/8**

```

# RHEL 7: sudo systemctl start docker; sudo yum install -y docker
# docker run -v /PATH_TO_REPOSITORY:/community-automation -i -t quay.io/rayashworth/community-ansible:latest

NOTE: RHEL 8
# podman run -v /PATH_TO_REPOSITORY:/community-automation -i -t quay.io/rayashworth/community-ansible:latest

# if you setup the parameters for a play ahead of time, you can directly call the playbook

# docker run -v /PATH_TO_REPOSITORY:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i YOUR_PLAYBOOK/inventory YOUR_PLAYBOOK/YOUR_PLAYZBOOK.yml"

SAMPLE with parameter passing
# docker run -v /PATH_TO_REPOSITORY:/community-automation -v ~/.ssh:/root/.ssh -i -t quay.io/rayashworth/community-ansible:latest -c "ansible-playbook -i ocp-pool-claim-play/inventory ocp-pool-claim-play/ocp-pool-claim-play.yml -e \"admin_task=claim\""

NOTE: RHEL 8

# podman run -v /PATH_TO_REPOSITORY:/community-automation -v ~/.ssh:/root/.ssh -i -t community-ansible:latest -c "ansible-playbook -i YOUR_PLAY/inventory  YOUR_PLAY/YOUR_PLAYBOOK.yml"
```
