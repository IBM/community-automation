# Ansible Playbook for creating an RedHat CodeReadyContainer ( CRC running OCP 4.x ) stack on fyre.

## Assumptions:

 - You have capacity in fyre
 - Fyre is online
 - schader@us.ibm.com maintains an up-to-date crc binary here:
   - crc_download_src: "http://svt-auto01.fyre.ibm.com/opt/crc-linux-amd64.tar.xz"  
   NOTE: A temporary downgraded version has been placed here "http://9.46.68.100/crc-linux-amd64.tar.xz". It is currently the default install image.  The latest version is having issues completing the install.

## Setting up inventory

- From the `request-crc-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `fyreuser` variable in the `inventory` file with the name of your fyre user (see https://fyre.ibm.com/account).
- Modify `fyreapikey` variable in the `inventory` file  with your fyre api key (see https://fyre.ibm.com/account).

```
cp examples/inventory .
```

## Run playbook

The playbook/role supports a single Intel Fyre vm with 6cpu/32gb RHEL 8.x.  The stack name is randomly chosen unless overridden

e.g. -e stackName=mycrcStack01


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory request-crc-fyre-play.yml --vault-password-file roles/crc_start/files/crc_pull_pass

or


ansible-playbook  -i inventory request-crc-fyre-play.yml -e stackName=mycrcStack01 --vault-password-file roles/crc_start/files/crc_pull_pass
```

To disable vnc server install ( takes around 8 minutes ) add
``` 
-e vnc=False
```

## Access the command line

Once the stack is created, crc installed and running, ssh kevin@stackname_FQDN

```
crc status
crc console --credentials
```

## Access the web gui ( vnc is required )

One can also vncviewer stackname_FQDN:5901
password is : vncPassw0rd

Open a command term, and run

```
crc console --credentials
crc console
```
