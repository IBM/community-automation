#!/bin/bash

# process OCP clsuter deployment
#
set -o errexit
set -o nounset
set -o pipefail

set -x

CLUSTER_NAME=$1
deploy_log=/tmp/$CLUSTER_NAME.log
retries=120
bootstrap_complete=0
previous_podname=""
provision_podname=""

# process deployment and check for success
for (( i=0; i <= retries; i++ )); do
   # get provising name
   previous_podname=$provision_podname 
   while [ "$provision_podname" == '' ]; do
    echo "Finding provisioning pod name..."
    provision_podname=$(oc --no-headers=true get pods -n "$CLUSTER_NAME" -l hive.openshift.io/job-type=provision,hive.openshift.io/cluster-deployment-name="$CLUSTER_NAME" -o name | cut -d / -f2)
    sleep 10
   done
   # check to see if install failed and has restarted new pod.
   [[ $provision_podname != "$previous_podname" ]] && { previous_podname=$provision_podname; bootstrap_complete=0; } || true  
   oc logs -n "$CLUSTER_NAME" "$provision_podname" -c hive > "$deploy_log"
   echo "Checking install logs for strings...(retry $i)"
   grep "Bootstrap failed to complete" "$deploy_log" && { echo "Bootstrap failed"; exit 1; } || true
   [[ $bootstrap_complete != 1 ]] && { grep -i "Bootstrap status: complete" "$deploy_log" && { echo "bootstrap complete"; bootstrap_complete=1; } } || { grep -i "install completed successfully" "$deploy_log" && exit 0 || continue ; }
   sleep 30
done

