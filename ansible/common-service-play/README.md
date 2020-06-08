# Ansible Playbook for Common Services Installation

## Assumptions:

 - A healthy OpenShift 4 cluster in running state.

## Setting up inventory

Make use of sample file at `examples/inventory`.

```
cp examples/inventory .
```

## Run playbook

#### Setting up variables for playbook

Make use of the sample file at `examples/cs_vars.yml`. Modify the values as per your cluster. For more information refer to examples.

```
cp examples/cs_vars.yml .
```

Once you have configured the vars & inventory file, run the playbook using:

```
ansible-playbook  -i inventory -e @cs_vars.yml common-services.yml
```

License
-------

See LICENCE.txt

