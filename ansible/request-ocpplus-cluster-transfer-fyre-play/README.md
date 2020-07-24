# Ansible Playbook for transfering a fyre OCP+Beta cluster to another user

## Overview

- Transfers a fyre OCP+Beta cluster to a user using their IBM intranet email.
   - Transfers OCP+Beta cluster using API
   - Sends an email to the new user with
     - ocp_web_console_url
     - kubeadmin Password
     - API curl command to accept the cluster transfer


## Requirements

  - Running fyre OCP+Beta cluster.
  - Ansible 2.9 or later installed.


## Setting up inventory

Make use of sample file at `examples/inventory` (no changes needed).

```
cp examples/inventory .
```

## Run playbook

#### Setting up variables for playbook

Make use of the sample file at `examples/ocp_transfer_vars.yml`. Modify the values as per your cluster. See comments in file.

```
cp examples/ocp_transfer_vars.yml .
```

Once you have configured the vars file, run the playbook using:

```
ansible-playbook  -i inventory -e @ocp_transfer_vars.yml request-ocpplus-transfer.yml
```

License
-------

See LICENCE.txt
