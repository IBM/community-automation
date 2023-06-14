# Ansible Playbook for configuring target operation systems with pre-reqs for a product

## Assumptions:

- Fyre systems do not have unzip. This is the basic install of that package
- Check the roles/osprereqs/tasks/*.yml to review the actual list of packages
- Ansible host has python `passlib`

- external default file: /etc/ansible/nestvars.yml
```
---

user_username: nest
user_password: yourFavoritePassword
```
Can override this file with `-e external_password_file=somefile`

- external file containing .ssh/id_rsa.pub keys

Default is blank, thus no keys are added to the target host

Can override this file with `-e authorized_keys_url=http://yourkeyhost/yourkeyfile`

## Setting up inventory

- From the `setup-new-fyre-host-play` directory copy the sample inventory file at `examples/inventory` to the  current directory.
- Modify `hosts` to match your target hosts

```
cp examples/inventory .
```

## Run playbook

The playbook/role supports  RedHat8 / SLES / Ubuntu x64 or ppc64le


Once you have configured the `inventory` file, run the playbook using:

```
ansible-playbook  -i inventory setup-new-fyre-host-play.yml

```

