# Ansible Playbook for creating an RedHat Jmeter host on Fyre

## Assumptions:

 - You have capacity in fyre
 - Fyre is online

## Setting up inventory

- From the `request-rhel-jmeter-fyre-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `fyreuser` variable in the `inventory` file with the name of your fyre user (see https://fyre.ibm.com/account).
- Modify `fyreapikey` variable in the `inventory` file  with your fyre api key (see https://fyre.ibm.com/account).

```
cp examples/inventory .
```

## Run playbook

The playbook/role supports a single Intel Fyre vm with 2cpu/2gb RHEL 8.x.  The stack name is randomly chosen unless overridden

e.g. -e stackName=jmeterstress01

Do not use jmeter for the username as the lineinfile logic will fail to add jmeter to the path


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory request-rhel-jmeter-fyre-play.yml 

or

ansible-playbook  -i inventory request-crc-fyre-play.yml -e stackName=jmeterStack -e jmeterUser=nest -e noLog=false -e javaArchive='https://github.com/AdoptOpenJDK/openjdk14-binaries/releases/download/jdk-14.0.2+12_openj9-0.21.0/OpenJDK14U-jdk_x64_linux_openj9_14.0.2_12_openj9-0.21.0.tar.gz'  -e jmeterArchive='http://www.gtlib.gatech.edu/pub/apache/jmeter/binaries/apache-jmeter-5.3.tgz'
```

To disable vnc server install ( takes around 8 minutes ) add
``` 
-e vnc=False
```

## Access the command line

Once the stack is created, ssh root@stackname_FQDN and set the password for < jmeterUser >
Once the < jmeterUser > password is set, ssh < jmeterUser >@stackname_FQDN

```
jmeter -v
```

## Access vnc 

One can also vncviewer stackname_FQDN:5901
password is : vncPassw0rd

The default terminal does not login, thus the jmeter nor java commands are in the PATH.  Edit the terminal Preferences->Command and check 'Run command as login shell' and restart the terminal.
