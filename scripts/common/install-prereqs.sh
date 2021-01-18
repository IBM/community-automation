#!/bin/bash

# install ansible 2.9+

[[ $(ansible --version | head -1 | awk '{ print $2 }' | cut -d . -f1-2) == 2.10 ]] && { echo "ansible at correct version"; exit 0; } || true

sudo apt -y update
sudo apt -y upgrade
sudo apt -y remove --purge ansible
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt -y update
sudo apt -y install ansible

# run from script location
file_location=$(find . -type f -name install-prereqs.sh | grep .) && cd "$(dirname $file_location)" || { echo "could not find install-prereqs.sh"; exit 1; }

play_dir="../../ansible/prereq-play"
# install ansible modules
ansible-galaxy collection install -r $play_dir/requirements.yml

# update and install python libraries
ansible-playbook -i $play_dir/inventory $play_dir/prereq-play.yml

echo "Install and updates complete."
