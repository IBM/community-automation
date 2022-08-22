#!/bin/bash


ansible-playbook  -i inventory  request-edge-ocp-install.yml -e "fyreuser=${MY_FYRE_USER}" -e "fyreapikey=${MY_FYRE_APIKEY}" -e "clusterName=${OCP_STACK_NAME}" -e "ocpVersion=${OCP_VERSION}" -e "ansible_user_dir=/root/" -e "fyre_site=${FYRE_SITE}" -e "fyre_group_id=${FYRE_GROUP_ID}"


