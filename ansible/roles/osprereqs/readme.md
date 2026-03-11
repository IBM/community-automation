OS Prerequisites Role
=====================

This role configures operating system prerequisites for various platforms including Red Hat Enterprise Linux, Ubuntu, SLES, and AIX.

Requirements
------------

- Ansible 2.9 or higher
- `ansible.posix` collection (for sysctl module in core dump configuration)
- Root/sudo privileges on target systems

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| twas855x                | no       | false   | true, false               | Install 32-bit packages for tWAS 8.5.5.x |
| enable_core_dumps       | no       | false   | true, false               | Enable full core dump generation         |

## Core Dump Configuration

When `enable_core_dumps` is set to `true`, the role will:
- Configure unlimited core dump size in `/etc/security/limits.conf`
- Set kernel core pattern to `/var/crash/core.%e.%p.%h.%t`
- Create `/var/crash` directory with proper permissions
- Configure systemd-coredump (if present) for uncompressed, unlimited dumps
- Set ulimit in `/etc/profile.d/enable_coredumps.sh`

See [tasks/README_enable_core_dumps.md](tasks/README_enable_core_dumps.md) for detailed documentation.

Dependencies
------------

None

Example Playbook
----------------

Basic usage:
```yaml
- hosts: all
  roles:
    - role: osprereqs
```

With core dumps enabled:
```yaml
- hosts: debug_servers
  vars:
    enable_core_dumps: true
  roles:
    - role: osprereqs
```

Include core dump task directly:
```yaml
- hosts: all
  tasks:
    - name: Enable core dumps
      ansible.builtin.include_role:
        name: osprereqs
        tasks_from: enable_core_dumps
      when: enable_core_dumps | default(false) | bool
```

See [examples/enable_core_dumps_example.yml](examples/enable_core_dumps_example.yml) for more examples.

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Add author
