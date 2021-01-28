# Common Scripts

These scripts are intended to be used by a broad group of teams

## Presonal client VM prereq script

install-prereqs.sh is used to setup an ansible install client VM.   It will ensure the correct version of ansible is installed and it will add python3 and several python3 libraries.  After the script complete you should be able to run most of the existing ansible playbooks without any additional updates.  

**Tested on ubuntu 16.04,18.04 and 20.04**  
**NOTE:**

- non-root users will need sudo access
- you may need to do a **docker login**, if you see complaints about pull limits

```
# cd community-automation
# scripts/common/install-prereqs.sh

RHEL8
# cd community-automation
# scripts/common/install-prereqs.sh -u YOUR_REDHAT_USERNAME -p YOUR_REDHAT_PASSWORD
```

## community docker script
community-docker.sh will create and run a ubuntu docker container with all prereq's where all playbooks can be run.

**MAC** users need to install docker to run this option

**NOTES:**

- RHEL8 users, non-root users need sudo access
- You may need to do a **docker logout** before you begin.
- default ssh keys are comming from your ~/.ssh/id_rsa and ~/.ssh/id_rsa.pub


**Tested on MAC (big sur), Ubunutu 16.04/18.04, and RHEL 7/8**

```
# cd community-automation
# scripts/common/community-docker.sh

# Options to include your own ssh keys
# scripts/common/community-docker.sh --ssh_priv_key ~/.ssh/my_id_rsa --ssh_pub_key ~/.ssh/my_id_rsa.pub
#   --ssh_priv_key and --ssh_pub_key can be from any location
```



```
# RHEL 8
# cd community-automation
# scripts/common/community-docker.sh -u YOUR_REDHAT_USERNAME -p YOUR_REDHAT_PASSWORD
# options to include your own ssh keys
# scripts/common/community-docker.sh -ssh_priv_key YOUR_PRIVATE_KEY -- ssh_pub_key YOUR_PUBLIC_KEY -u YOUR_REDHAT_USERNAME -p YOUR_REDHAT_PASSWORD
```

## Re-enter docker container

```
NOTE: -w is whatever you used for your working directory
# docker exec -it -w /tmp/community-automation community_auto_bash bash
```

## Stop the docker container

```
# docker stop community_auto_bash
```

## Re-start the docker container

```
# docker start community_auto_bash
NOTE: -w is whatever you used for your working directory
# docker exec -it -w /tmp/community-automation community_auto_bash bash
```

## to remove container

```
# docker rm community_auto_bash
```
