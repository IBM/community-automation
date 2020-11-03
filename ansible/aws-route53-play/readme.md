 
# AWS route53 EXAMPLE play
**NOTE:** At the moment and IPI install on vSphere requires that you install from a VM running inside the same vCenter.

This play will create 2 entries in AWS public Route53 hosted zone to support IPI install on vSphere.

The role from this play will be consumed by a AWS ansible play.  

## Update Ubuntu certs

```
wget --no-check-certificate  https://icovcpc65.rtp.raleigh.ibm.com/certs/download.zip  
copy to /usr/share/ca-certificates/extra  
unzip download.zip  
cd lin directory  
rename files to add .crt  
dpkg-reconfigure ca-certificates  
screen will appear, select the 2 new certs
if on ubuntu 16.xx you may need to copy the certs to a new location
cp /usr/share/ca-certificates/extra/*.* /etc/ssl/certs
```

### Update RHEL certs

```
wget --no-check-certificate  https://icovcpc65.rtp.raleigh.ibm.com/certs/download.zip  
extract zip file  
from lin dir  
cp * /etc/pki/ca-trust/source/anchors/  
update-ca-trust extract  
```

copy inventory and vars file into play parent directory  
```
# cp examples/inventory .
# cp examples/aws-route53-vars.yml .
```

edit **aws-route53-vars.yml** see file for details

add aws route53 ansible module
```
# ansible-galaxy collection install -r requirements.yml
```

## add AWS record
```
# ansible-playbook -i inventory aws-route53-play -e route_task="add" 
```

## delete AWS record
```
# ansible-playbook -i inventory aws-route53-play.yml -e route_task="delete" 
```
