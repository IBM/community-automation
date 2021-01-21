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


**Tested on MAC (big sur), Ubunutu 16.04/18.04, and RHEL 7/8**

```
# cd community-automation
# scripts/common/community-docker.sh
```

```
# RHEL 8
# cd community-automation
# scripts/common/community-docker.sh -u YOUR_REDHAT_USERNAME -p YOUR_REDHAT_PASSWORD
```

## Re-enter docker container

```
# docker exec -it community_auto_bash bash
```

## Stop the docker container

```
# docker stop community_auto_bash
```

## Re-start the docker container

```
# docker start community_auto_bash
# docker exec -it community_auto_bash bash
```
