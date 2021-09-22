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
previous_podname=""
provision_podname=""

# process deployment and check for success
for (( i=0; i <= retries; i++ )); do
   # get provising name
    echo "Finding provisioning pod name..."
    previous_podname=$provision_podname
    provision_podname=$(oc --no-headers=true get pods -n "$CLUSTER_NAME" -l hive.openshift.io/job-type=provision,hive.openshift.io/cluster-deployment-name="$CLUSTER_NAME" -o name | tail -1 | cut -d / -f2)
    [[ $provision_podname == '' ]] && { sleep 10; continue; } || true
   # check to see if install failed and has restarted new pod.
   [[ $provision_podname != "$previous_podname" ]] && { previous_podname=$provision_podname; bootstrap_complete=0; } || true  
   oc logs -n "$CLUSTER_NAME" "$provision_podname" -c hive > "$deploy_log" || true
   echo "Checking install logs for strings...(retry $i)"
   grep "Bootstrap failed to complete" "$deploy_log" && { echo "Bootstrap failed"; exit 1; } || true
   [[ $bootstrap_complete != 1 ]] && { grep -i "Bootstrap status: complete" "$deploy_log" && { echo "bootstrap complete"; bootstrap_complete=1; } } || { grep -i "install completed successfully" "$deploy_log" && exit 0 || sleep 30; }
done

