#!/bin/bash

ansible-playbook  -i inventory  request-edge-fyre-play.yml -e "fyreuser=${MY_FYRE_USER}" -e "fyreapikey=${MY_FYRE_APIKEY}" -e "stackName=${FYRE_STACK_NAME}"

