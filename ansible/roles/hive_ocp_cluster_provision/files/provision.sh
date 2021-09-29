#!/bin/bash

# process OCP clsuter deployment
#
set -o errexit
set -o nounset
set -o pipefail

CLUSTER_NAME=$1
deploy_log=/tmp/$CLUSTER_NAME.log
provision_podname=""

# get provising name
provision_podname=$(oc --no-headers=true get pods -n "$CLUSTER_NAME" -l hive.openshift.io/job-type=provision,hive.openshift.io/cluster-deployment-name="$CLUSTER_NAME" -o name | tail -1 | cut -d / -f2) || true

# get deploy log
oc logs -n "$CLUSTER_NAME" "$provision_podname" -c hive > "$deploy_log" || true

# check content of deploy log
grep -i "Bootstrap failed to complete" "$deploy_log" && { echo "Bootstrap failed"; exit 1; } || true
grep -i "bootstrap status: complete" "$deploy_log" && echo "Bootstrap Complete" || true
grep -i "install completed successfully" "$deploy_log" && { echo "Bootstrap complete"; exit 0; }  || true

