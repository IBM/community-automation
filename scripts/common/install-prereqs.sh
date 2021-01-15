#!/bin/bash

# install ansible 2.9+
apt -y update
apt -y upgrade
apt-get -y remove --purge ansible
apt-add-repository -y ppa:ansible/ansible
apt -y update
apt -y install ansible

# install ansible modules
ansible-galaxy collection install -r ../../../ansible/prereq-play/requirements.yml

# update and install python libraries
ansible-playbook -i inventory ../../../ansible/prereq-play/prereq-play.yml

echo "Install and updates complete."
