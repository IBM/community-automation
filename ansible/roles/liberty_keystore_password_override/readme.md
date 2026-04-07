# liberty_keystore_password_override

## Description

This role checks for the existence of the `server.env` file in a WebSphere Liberty server directory and ensures that the `keystore_password` key is present. If the file exists but does not contain the `keystore_password` key, the role will add it using the configured password value.

## Requirements

- WebSphere Liberty must be installed
- The Liberty server must be created
- The `wlp_usr_dir` and `wl_server` variables must be defined

## Role Variables

### Required Variables

- `wlp_usr_dir`: The Liberty user directory path (e.g., `/opt/IBM/wlp/usr`)
- `wl_server`: The Liberty server name (e.g., `defaultServer`)

### Optional Variables

- `wlp_keystore_password`: The keystore password to use (default: `changeit`)

## Dependencies

None

## Example Playbook

```yaml
- hosts: liberty_servers
  roles:
    - role: liberty_keystore_password_override
      vars:
        wlp_usr_dir: "/opt/IBM/wlp/usr"
        wl_server: "defaultServer"
        wlp_keystore_password: "mySecurePassword123"
```

## Behavior

1. Checks if the file `{{ wlp_usr_dir }}/servers/{{ wl_server }}/server.env` exists
2. If the file does **not** exist:
   - Creates the file with `keystore_password={{ wlp_keystore_password }}`
   - Displays a creation status message
3. If the file **does** exist:
   - Reads the file contents
   - Checks if `keystore_password=` is present
   - If not present, adds the line `keystore_password={{ wlp_keystore_password }}`
   - Displays a status message indicating whether the password was added or already existed

## Example server.env File

Before (missing keystore_password):
```
JAVA_HOME=/opt/IBM/liberty/java/11.0
WLP_USER_DIR=/opt/IBM/wlp/usr
```

After:
```
JAVA_HOME=/opt/IBM/liberty/java/11.0
WLP_USER_DIR=/opt/IBM/wlp/usr
keystore_password=changeit
```

## License

Apache License 2.0

## Author Information

IBM Community Automation