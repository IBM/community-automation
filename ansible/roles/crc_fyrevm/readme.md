# Request a RedHat CodeReadyContainer Fyre
This role create a single 6cpu/32gb  stack in Fyre.
Will it is expected to run on a host with the following hostvars:
- fyreuser
- fyreapikey

The role expects to be supplied: 
 - stackName
 - fyre_site (optional: defaults to rtp)


fyreApi machine should have an public ssh key available: ~/.ssh/id_rsa.pub

The roles behaves in the following way:
1) Requests and Wait for an RedHat 8.x Intel Fyre vm ( Amd will not work ) stack to be fully deployed 
2) Role will error if stack fails to create in fyre
3) Installs and enables VNC.  Using vnc to log in via the OpenShift gui.

The following is an example of how to run the role.
```
- hosts: fyreApi
  roles: 
  - role: request-crc-fyre
    stackName: myCrcvm
```

