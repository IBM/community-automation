clone_repo
============

This role can be used to include other repos that could be used for post install steps

------------

Requirements
------------

N/A

Role Variables
--------------

| Variable                | Required | Default | Choices                   | Comments                                 |
|-------------------------|----------|---------|---------------------------|------------------------------------------|
| local_repo_location     | yes      | /tmp    | valid path                |                                          |
| repo_url                | yes      |         | valid repo                | repo_url="https://github.com/IBM/community-automation"|
| repo_name               | yes      |         | valid repo name           |     |
| repo_branch             | yes      | master  | valid branch name         |     |
| temp_branch             | yes      |         | string                    | used to operate in a branch other then master |
| git_user_email          | yes      | | |  |
| git_user_name           | yes      | | |  |

Dependencies
------------

N/A

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - clone_repo

License
-------

See [LICENSE](https://github.com/IBM/community-automation/blob/master/LICENSE)

Author Information
------------------

Add author
