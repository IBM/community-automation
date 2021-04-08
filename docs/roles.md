# Roles

| role | Description | status | Comments |
|------|-------------|--------|----------|
|ocp_login | used when OCP Login is needed for your play | Available | will automatically install oc client |
|oc_client_install|installs oc command| Available | is automatic when using ocp_login role|
|ocp_request_token | used to fetch OCP token | Available | will fetch OCP token  |
|ocp_cluster_tag|tags your cluster| Available | working on AWS only at this time|
|ocp_add_users_to_scc | used to patch existing SCC with the user/service account | Available |
|aws_route53|sets up api.\* and apps.\* for vsphere ipi installer| Available |
|deploy_ova_vmware| deploy redhat coreos image to vmware|Available|
