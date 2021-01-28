#!/bin/bash

# bash best practices
set -o errexit
set -o nounset
set -o pipefail

function usage () {
    echo "Usage: ./community-docker.sh <params>"
    echo "  Where <params> are:"
    echo "    --ssh_priv_key"
    echo "    --ssh_pub_key"
    echo "    --help"
}

# Set the parameters
saved_params="$@"
ssh_priv_key="$HOME/.ssh/id_rsa"
ssh_pub_key="$HOME/.ssh/id_rsa.pub"
while test $# -gt 0; do
  [[ $1 =~ ^-sp|--ssh_priv_key$ ]] && { ssh_priv_key="$2" ; shift 2; continue; };
  [[ $1 =~ ^-su|--ssh_pub_key$ ]] && { ssh_pub_key="$2" ; shift 2; continue; };
  [[ $1 =~ ^-h|--help$ ]] && { usage; shift 1; continur; };
  echo "Parameter not recognized: $1, ignored"
  shift
done

set -- $saved_params
source scripts/common/rhel8-functions.sh

# check for RHEL8
[[ -f /etc/redhat-release ]] && [[ $(grep '8.' /etc/redhat-release) ]] && rhel8_support $@ || true

# check ubuntu and update/install
[[ -f /etc/os-release ]] && [[ $(cat /etc/os-release | grep NAME | grep Ubuntu | grep -v PRETTY | cut -d \" -f2) == "Ubuntu" ]] && apt install -y docker.io || true

repo_dir="$(pwd)"
play_dir=/tmp/community-automation/ansible/prereq-play
container_name="community_auto_bash"
container_home_dir="/tmp/community-automation"

cp "$ssh_priv_key" "$(pwd)/id_rsa"
cp "$ssh_pub_key" "$(pwd)/id_rsa.pub"

# start docker container and pass environment variables
docker run --name "$container_name" -v "$repo_dir":"$container_home_dir" -i -t -d ubuntu:latest 

# install pre-reqs
docker exec -it "$container_name" bash -c "apt -y update; apt -y install python3 python3-pip git curl wget sudo jq gpg vim sshpass; pip3 install --upgrade pip; pip3 install ansible"
docker exec -it "$container_name" bash -c "mkdir -p -m600 ~/.ssh; cp id_rsa* ~/.ssh" 
docker exec -it "$container_name" bash -c "ansible-galaxy collection install -r $play_dir/requirements.yml"
docker exec -it "$container_name" bash -c "ansible-playbook -i $play_dir/inventory $play_dir/prereq-play.yml"

echo "########################################################################################"
echo "When you exit from docker conatiner $container_name, here is how to stop the container"
echo " for RHEL host, cd to /tmp/community-automation after container starts"
echo "docker stop $container_name"

echo "To restart your docker container"
echo "docker start $container_name"
echo "docker exec -it $container_name bash"
echo "########################################################################################"

# open docker container to execute plays.  -w does not work on RHEL
[[ ! -f /etc/redhat-release ]] && docker exec -it -w "$container_home_dir" "$container_name" bash || docker exec -it "$container_name" bash
