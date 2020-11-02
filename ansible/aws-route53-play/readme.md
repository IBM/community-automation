 
# AWS route53 EXAMPLE play

The role from this play will be comsumed by a AWS ansible play.  

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
