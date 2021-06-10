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

ubuntu_release=$(grep VERSION= /etc/os-release | cut -d\" -f2 | cut -d. -f1)

[[ $ubuntu_release == 20 ]] && { \
  sudo apt update -y; \
  sudo apt upgrade -y; \
  sudo add-apt-repository -y ppa:deadsnakes/ppa; \
  sudo apt update -y; \
  sudo apt-get install -y python3.6; \
  sudo -s cd /usr/bin; rm -f python3; ln -s python3.6 python3; \
  sudo apt update -y; \
  sudo apt upgrade -y; \
  sudo apt install -y python3-pip; \
  sudo pip3 install -y ansible==2.10; } || true

# check ubuntu and update/install
[[ $ubuntu_release != 20 ]] && [[ $(cat /etc/os-release  | grep NAME | grep Ubuntu | grep -v PRETTY | cut -d \" -f2) == "Ubuntu" ]] && { \
  sudo apt -y update; \
  sudo apt -y upgrade; \
  sudo apt -y install python3 python3-pip sshpass; \
  sudo rm -f /usr/local/bin/ans*; \
  sudo add-apt-repository -y ppa:ansible/ansible-2.10; \
  sudo apt -y update; \
  sudo pip3 install ansible==2.10; } || true

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
