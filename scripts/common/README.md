# Common Scripts

These scripts are intended to be used by a broad group of teams

## Presonal client VM prereq script

install-prereqs.sh is used to setup an ansible install client VM.   It will ensure the correct version of ansible is installed and it will add python3 and several python3 libraries.  After the script complete you should be able to run most of the existing ansible playbooks without any additional updates.  

**Tested on ubuntu 16.04 and 18.04**  
**NOTE:** non-root users will need sudo access

```
# scripts/common/install-prereqs.sh
```

## community docker script
community-docker.sh will create and run a ubuntu docker container with all prereq's where all playbooks can be run.

**Tested on MAC (big sur), Ubunutu 16.04/18.04, and RHEL 7/8**

```
# scripts/common/community-docker.sh
```

**NOTE:** RHEL8 users, requires sudo

```
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