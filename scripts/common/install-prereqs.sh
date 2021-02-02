#!/bin/bash

# bash best practices
set -o errexit
set -o nounset
set -o pipefail

ansible_installed=false
docker_install="false"
# check for ansible version
[[ $(which ansible) ]] && [[ $(ansible --version | head -1 | awk '{ print $2 }' | cut -d . -f1-2) == "2.10" ]] && { echo "ansible at correct version"; ansible_installed=true ; } || true

if [ $ansible_installed == false ]; then
# check rhel 8 and update/install
[[ -f /etc/redhat-release ]] && [[ $(grep '8.' /etc/redhat-release) ]] && rhel8_support $@ || true

# check ubuntu and update/install
[[ -f /etc/os-release ]] && [[ $(cat /etc/os-release  | grep NAME | grep Ubuntu | grep -v PRETTY | cut -d \" -f2) == "Ubuntu" ]] && { sudo apt -y update; \
  sudo apt -y upgrade; \
  sudo apt -y remove --purge ansible; \
  sudo apt -y install python3 python3-pip sshpass; \
  sudo add-apt-repository -y add ppa:ansible2.10; \
  sudo apt -y update; \
  sudo pip3 install ansible; } || true

  # clear bash cache
  hash -r
  sync; sync
fi

# run from script location
file_location=$(find . -type f -name install-prereqs.sh | grep .) && cd "$(dirname $file_location)" || { echo "could not find install-prereqs.sh"; exit 1; }

play_dir="../../ansible/prereq-play"
# install ansible modules
ansible-galaxy collection install -r $play_dir/requirements.yml

# update and install python libraries
ansible-playbook -i $play_dir/inventory $play_dir/prereq-play.yml

echo "Install and updates complete."
