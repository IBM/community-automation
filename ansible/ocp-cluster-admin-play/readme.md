# Cluster administration play

## Admin Tasks
- Stop and AWS Cluster
- Start an AWS Cluster

## prereq's
- an available AWS cluster
- cluster tag
- owner tag
- AWS credentials

## usage
```
cp examples/inventory .
cp examples/admin-vars.yml .
```

edit and update admin-vars.yml
```
# ansible-playbook -i inventory ocp-cluster-admin-play.yml
```
