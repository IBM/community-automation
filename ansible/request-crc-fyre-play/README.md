# Ansible Playbook for creating an RedHat CodeReadyContainer ( CRC running OCP 4.x ) stack on fyre.

## Assumptions:

 - You have capacity in fyre
 - Fyre is online
 - schader@us.ibm.com maintains an up-to-date crc binary here:
   - crc_download_src: "http://svt-auto01.fyre.ibm.com/opt/crc-linux-amd64.tar.xz"

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
ansible-playbook  -i inventory request-crc-fyre-play.yml 

or


ansible-playbook  -i inventory request-crc-fyre-play.yml -e stackName=mycrcStack01
```

Once the stack is created, crc installed and running, ssh fyre@<stack name>

```
crc status
crc console --credentials
```

One can also vncviewer <stackname>:5901
password is : vncPassw0rd
