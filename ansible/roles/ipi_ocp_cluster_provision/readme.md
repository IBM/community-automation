ipi_ocp_cluster_provision
=========

Provision OCP cluster using IPI installer

------------

Only implemented for AWS at this time

Requirements
------------

- Access to a cloud platform

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| MASTER_CPUS             | yes      | 10      | | |
| MASTER_MEMORY           | yes      | 32768   | | |  
| MASTER_DISK_SIZE        | yes     | 300     | | |
| MASTER_COUNT            | yes     | 3       | | |
| WORKER_COUNT            | yes     | 3        | | |
| WORKER_CPUS             | yes     | 16      |  | |
| WORKER_MEMORY           | yes      | 73728  | | |
| WORKER_DISK_SIZE        | yes      | 200 | | |
| WORKER_VM_SIZE          | yes      | m5.2xlarge | |  AWS size of worker VM instances |
| MASTER_VM_SIZE          | yes      | m5.2xlarge | |  AWS of master VM instances |
| BASE_DOMAIN             | yes      |  |  | purple-chesterfield.com |
| CLUSTER_NAME            | yes      |  | string value |   |
| cloud                   | yes      | AWS | AWS, google, azure, vsphere | AWS is only implementation at this time  |
| logfile                 | yes      | /tmp/deploy.log | |   |

Dependencies
------------

get_ocp_installer automatically included via meta

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - ipi_ocp_cluster_provision

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Ray Ashworth (ashworth@us.ibm.com)
