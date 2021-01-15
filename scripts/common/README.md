# Common Scripts

These scripts are intended to be used by a broad group of teams

## prereq script

install-prereqs.sh is used to setup an ansible install client VM.   It will ensure the correct version of ansible is installed and it will add python3 and several python3 libraries.  After the script complete you should be able to run most of the existing ansible playbooks without any additional updates.  

**Testid on ubuntu 16.04 and 18.04**  TODO: add other distro's  
To execute as root, non root users will need sudo access
```
sudo scripts/common/install-prereqs.sh
```
