#!/bin/bash

repo_dir=/workspace/docker-test
play_dir=/tmp/community-automation/ansible/prereq-play

# start docker container and pass environment variables
docker run --name ubuntu_bash -v $repo_dir/community-automation:/tmp/community-automation --rm -i -t -d ubuntu sleep 120m
# update ubuntu
docker exec -it ubuntu_bash apt update
# install pre-reqs
docker exec -it ubuntu_bash apt -y install python3 python3-pip git curl wget sudo jq gpg
docker exec -it ubuntu_bash pip3 install --upgrade pip
docker exec -it ubuntu_bash pip3 install ansible
docker exec -it ubuntu_bash bash -c "ansible-galaxy collection install -r $play_dir/requirements.yml"
docker exec -it ubuntu_bash bash -c "ansible-playbook -i $play_dir/inventory $play_dir/docker-play.yml"

# open docker container to execute plays
docker exec -it ubuntu_bash bash

echo "When you exec from docker conatiner, here is how to stop the container"
echo "docker stop ubuntu_bash"
