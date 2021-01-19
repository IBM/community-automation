#!/bin/bash

# bash best practices
set -o errexit
set -o nounset
set -o pipefail

function usage () {
  echo "When using RHEL 8, you must provide redhat credentials"
  echo "--redhat_username YOUR_REDHAT_USERNAME"
  echo "--redhat_password YOUR_REDHAT_PASSWORD"
}

function rhel8_support () {
  local num_of_params=4

  [[ $# -lt $num_of_params ]] && { usage ; exit 1; } || true

  # Set the parameters
  while test $# -gt 0; do
     [[ $1 =~ ^-u|--redhat_username$ ]] && { redhat_username="$2" ; shift 2; continue; };
     [[ $1 =~ ^-p|--redhat_password$ ]] && { redhat_password="$2" ; shift 2; continue; };
     echo "Parameter not recognized: $1, ignored"
     shift
  done

  sudo subscription-manager register --username "$redhat_username" --password "$redhat_password"
  sudo subscription-manager attach --auto
  sudo yum module install -y container-tools
  sudo yum install -y podman-docker
  sudo podman login registry.redhat.io --username "$redhat_username" --password "$redhat_password"
  echo "[INFO] redhat 8 support complete."
}

[[ $(cat /etc/redhat-release | grep '8.') ]] && rhel8_support $@ || true

repo_dir="$(pwd)"
play_dir=/tmp/community-automation/ansible/prereq-play
container_name="community_auto_bash"
# start docker container and pass environment variables
docker run --name "$container_name" -v "$repo_dir":/tmp/community-automation --rm -i -t -d ubuntu:latest sleep 120m

# install pre-reqs
docker exec -it "$container_name" bash -c "apt -y update; apt -y install python3 python3-pip git curl wget sudo jq gpg; pip3 install --upgrade pip; pip3 install ansible"
docker exec -it "$container_name" bash -c "ansible-galaxy collection install -r $play_dir/requirements.yml"
docker exec -it "$container_name" bash -c "ansible-playbook -i $play_dir/inventory $play_dir/docker-play.yml"

# open docker container to execute plays
docker exec -it "$container_name" bash

echo "When you exit from docker conatiner $container_name, here is how to stop the container"
echo "docker stop $container_name"
