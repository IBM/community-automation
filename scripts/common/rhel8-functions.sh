# RHEL 8 functions

function usage_rhel8 () {
  echo "When using RHEL 8, you must provide redhat credentials"
  echo "--redhat_username YOUR_REDHAT_USERNAME"
  echo "--redhat_password YOUR_REDHAT_PASSWORD"
}

function rhel8_support () {
  local num_of_params=4

  [[ $# -lt $num_of_params ]] && { usage_rhel8 ; exit 1; } || true

  # Set the parameters
  while test $# -gt 0; do
     [[ $1 =~ ^-u|--redhat_username$ ]] && { redhat_username="$2" ; shift 2; continue; };
     [[ $1 =~ ^-p|--redhat_password$ ]] && { redhat_password="$2" ; shift 2; continue; };
     echo "Parameter not recognized: $1, ignored"
     shift
  done

  sudo subscription-manager register --username "$redhat_username" --password "$redhat_password"
  sudo subscription-manager attach --auto
  sudo subscription-manager repos --enable ansible-2.9-for-rhel-8-x86_64-rpms
  sudo yum install -y python3 ansible
  if [ $docker_install == "true" ]; then
    sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
    sudo dnf install --nobest --allowerasing docker-ce
    sudo systemctl start docker
    #sudo yum module install -y container-tools
    #sudo yum install -y podman-docker
    #sudo podman login registry.redhat.io --username "$redhat_username" --password "$redhat_password"
  fi
  echo "[INFO] redhat 8 support complete."
}