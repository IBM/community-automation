#!/bin/bash

set -x

## Possible variables ##
##   fyre_platform: x
##   fyre_cpu: 2
##   fyre_memory: 2
##   fyre_os: 'Ubuntu 20.04'
##   fyre_site: "{{ site }}"

ansible-playbook  -i inventory  request-edge-fyre-play.yml -e "fyreuser=${MY_FYRE_USER}" -e "fyreapikey=${MY_FYRE_APIKEY}" -e "site=rtp" -e "stackName=${FYRE_STACK_NAME}"  -e 'fyre_os="Ubuntu 20.04"'

