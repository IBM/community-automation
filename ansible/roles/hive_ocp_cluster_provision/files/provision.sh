#!/bin/bash

# process OCP clsuter deployment
#
set -o errexit
set -o nounset
set -o pipefail

CLUSTER_NAME=$1
deploy_log=/tmp/$CLUSTER_NAME.log
retries=120
bootstrap_complete=0

# process deployment and check for success
for (( i=0; i <= retries; i++ )); do
   # get provising name
   provision_podname=$(oc --no-headers=true get pods -n "$CLUSTER_NAME" -l hive.openshift.io/job-type=provision,hive.openshift.io/cluster-deployment-name="$CLUSTER_NAME" -o name | cut -d / -f2)
   oc logs -n "$CLUSTER_NAME" "$provision_podname" -c hive > "$deploy_log"
   grep "Bootstrap failed to complete" "$deploy_log" && { echo "Bootstrap failed"; exit 1; } || true
   [[ $bootstrap_complete != 1 ]] && { grep -i "Bootstrap status: complete" "$deploy_log" && { echo "bootstrap complete"; bootstrap_complete=1; } } || { grep -i "install completed successfully" "$deploy_log" && exit 0 || continue ; }
   sleep 30
done
