# Installing ansible

Installation details can be found here https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-ansible-on-macos

Your ansible version should be at 2.9.x when complete.

**NOTE:** When configuring your inventory file you may need to add a reference to python.  [sample inventory](recover-machine-config-play/examples/inventory)

## Ubuntu

```bash
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

## RHEL

https://access.redhat.com/articles/3174981

```bash
sudo subscription-manager register
sudo subscription-manager  attach --pool=8a85f99b6e12cc13016e3c2546361fa5
RHEL 8
sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
or
RHEL 7
sudo subscription-manager repos --enable rhel-7-server-ansible-2.9-rpms
sudo yum install ansible
```

## MAC

Apple removed sshpass from MAC, so you will need to install sshpass.  
Redhat recommends using the pip install method https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#from-pip  however brew will work as well.  Just be sure you end up with version 2.9.x  

### Install sshpass 

```bash
brew install http://git.io/sshpass.rb
```

**NOTE:** If installing `sshpass` with `brew` is not possible on your system, consult this useful article on [installing sshpass](https://thornelabs.net/posts/ansible-os-x-mavericks-you-must-install-the-sshpass-program.html)

### Ansible Install  

```bash
brew install ansible
```
