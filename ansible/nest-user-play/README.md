# Ansible Playbook for creating a user for tWAS/Liberty NEST testing

## Assumptions:

- external default file: /etc/ansible/nestvars.yml
```
---

nest_username: nest
nest_groupname: nest
user_username: nest
user_password: yourFavoritePassword
```
Can override this file with `-e external_password_file=somefile`

## Setting up inventory

- From the `osprereq-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `hosts` to match your target hosts

```
cp examples/inventory .
```

## Run playbook

The playbook/role supports linux hosts


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory nest-user-play.yml

```
