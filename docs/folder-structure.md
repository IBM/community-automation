# Folder Structure

[Ansible best practices document](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)

The following is a snippet to help understand the folder structure and how we are using it.  
We have playbooks and roles, and each are at the top level under ansible/.  

You will notice symlinks to roles in each playbook

``` text
└── ansible
    ├── LICENCE.txt
    ├── README.md
    ├── ansible.cfg
    ├── common-service-play
    │   ├── Jenkinsfile
    │   ├── README.md
    │   ├── common-services.yml
    │   ├── ansible.cfg
    │   ├── examples
    │   │   ├── cs_vars.yml
    │   │   └── inventory
    │   └── roles -> ../roles
    ├── recover-expired-certificates-play
    │   ├── Jenkinsfile
    │   ├── readme.md
    │   ├── recover-expired-certificates-play.yml
    │   └── roles -> ../roles
    ├── recover-machine-config-play
    │   ├── Jenkinsfile
    │   ├── readme.md
    │   ├── recover-machine-config-play.yml
    │   └── roles -> ../roles
    ├── request-ocp-aws-play
    │   └── roles -> ../roles
    ├── request-ocp-fyre-play
    │   └── roles -> ../roles
    ├── request-crc-fyre-play
    │   └── roles -> ../roles
    ├── request-ocp-roks-play
    │   └── roles -> ../roles
    └── roles
        ├── common_services
        │   ├── README.md
        │   ├── defaults
        │   │   └── main.yml
        │   ├── tasks
        │   │   └── main.yml
        │   └── templates
        │       ├── cs-group.yaml.j2
        │       ├── cs-request.yaml.j2
        │       ├── cs-sub.yaml.j2
        │       ├── cs-validation.bash.j2
        │       └── opencloud-source.yaml.j2
        ├── ocp_login
        │   └── tasks
        │       ├── main.yml
        │       └── ocp_login.yml
        ├── recover_expired_certificates
        │   ├── defaults
        │   │   └── main.yml
        │   ├── files
        │   ├── meta
        │   │   └── main.yml
        │   ├── tasks
        │   │   ├── main.yml
        │   │   └── recover-expired-certificates.yml
        │   ├── templates
        │   └── vars
        ├── recover_machine_config
        │   ├── defaults
        │   │   └── main.yml
        │   ├── files
        │   ├── meta
        │   │   └── main.yml
        │   ├── readme.md
        │   ├── tasks
        │   │   ├── main.yml
        │   │   └── recover_machine_config.yml
        │   ├── templates
        │   └── vars
        ├── request_ocp_aws
        │   ├── default
        │   ├── readme.md
        │   ├── tasks
        │   └── templates
        ├── request_ocp_fyre
        │   ├── defaults
        │   ├── readme.md
        │   ├── tasks
        │   └── templates
        ├── jmeter
        ├── jmeter_fyrevm
        ├── jmeter_java
        ├── java
        ├── jmeter_prereqs
        └── request_ocp_roks
            ├── defaults
            ├── readme.md
            ├── tasks
            └── templates
```
