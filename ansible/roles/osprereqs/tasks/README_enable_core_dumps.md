# Enable Core Dumps Task

## Overview
This task configures Red Hat Enterprise Linux systems to generate full, uncompressed core dump files for debugging purposes.

## What it does

1. **Sets unlimited core dump size** in `/etc/security/limits.conf` for all users
2. **Configures kernel core pattern** to store dumps in `/var/crash` with detailed naming
3. **Creates `/var/crash` directory** with appropriate permissions (1777)
4. **Configures systemd-coredump** (if systemd is present):
   - Disables compression
   - Sets unlimited size limits
   - Configures external storage
5. **Sets ulimit** in `/etc/profile.d/enable_coredumps.sh` for shell sessions

## Core Dump File Naming

Core dumps are stored in `/var/crash/` with the following naming pattern:
```
core.%e.%p.%h.%t
```

Where:
- `%e` = executable filename
- `%p` = process ID
- `%h` = hostname
- `%t` = timestamp (seconds since epoch)

Example: `core.java.12345.myhost.1675789012`

## Usage

Include this task in your Red Hat-specific playbooks:

```yaml
- name: Enable full core dumps
  ansible.builtin.include_tasks: enable_core_dumps.yml
  when: enable_core_dumps | default(false) | bool
```

## Variables

You can control whether core dumps are enabled by setting:
```yaml
enable_core_dumps: true
```

## Requirements

- Red Hat Enterprise Linux 7, 8, 9, or 10
- Root/sudo privileges
- `ansible.posix` collection (for sysctl module)

## Notes

- Core dumps can consume significant disk space
- Monitor `/var/crash` directory size regularly
- systemd-coredump is socket-activated and will automatically pick up configuration changes
- Changes to limits.conf require users to log out and back in to take effect
- Kernel sysctl changes take effect immediately

## Testing

To test if core dumps are working:

```bash
# Check current ulimit
ulimit -c

# Generate a test core dump
sleep 60 &
kill -SEGV $!

# Check for core file
ls -lh /var/crash/
```

## Security Considerations

- Core dumps may contain sensitive information (passwords, keys, etc.)
- Ensure `/var/crash` has appropriate permissions
- Consider implementing log rotation for core dumps
- Review and clean up old core dumps regularly