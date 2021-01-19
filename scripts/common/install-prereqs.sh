#!/bin/bash

# bash best practices
set -o errexit
set -o nounset
set -o pipefail

[[ $(ansible --version | head -1 | awk '{ print $2 }' | cut -d . -f1-2) == 2.10 ]] && { echo "ansible at correct version"; exit 0; } || true

[[ $(cat /etc/redhat-release | grep '8.') ]] && rhel8_support $@ || true

[[ $(cat /etc/os-release  | grep NAME | grep Ubuntu | grep -v PRETTY | cut -d \" -f2) == "Ubuntu" ]]  && { sudo apt -y update; \
sudo apt -y upgrade; \
sudo apt -y remove --purge ansible; \
sudo apt -y install python3 python3-pip; \
sudo add-apt-repository -y add ppa:ansible2.10; \
sudo apt -y update; \
sudo pip3 -y install ansible; } || true

# check for python3 version 3.6.9
[[ $(python3 --version | awk '{ print $2 }') == "3.6.9" ]] && { echo "correct version of python installed"; exit 0; }|| true

# run from script location
file_location=$(find . -type f -name install-prereqs.sh | grep .) && cd "$(dirname $file_location)" || { echo "could not find install-prereqs.sh"; exit 1; }

play_dir="../../ansible/prereq-play"
# install ansible modules
ansible-galaxy collection install -r $play_dir/requirements.yml

# update and install python libraries
ansible-playbook -i $play_dir/inventory $play_dir/prereq-play.yml

echo "Install and updates complete."
