FROM registry.access.redhat.com/ubi9/podman

RUN set -x && \
    dnf --disableplugin=subscription-manager update -y && \
    dnf --disableplugin=subscription-manager upgrade -y && \
    dnf --disableplugin=subscription-manager install -y python3-pip jq openssh-clients git wget sudo vim && \
    dnf --disableplugin=subscription-manager autoremove

ARG USER=runner
ARG UID=1001
ARG HOME=/home/$USER

RUN set -x && \
    useradd --create-home --uid $UID --gid 0 $USER && \
    echo "runner	ALL=(ALL)	NOPASSWD: ALL" > /etc/sudoers.d/runner

WORKDIR $HOME/ansible

RUN chown -R ${USER}:0 $HOME

USER $USER

ENV PATH $HOME/.local/bin:$PATH

RUN set -x && \
    python3 -m pip install --no-cache-dir --upgrade --user pip && \
    python3 -m pip install --no-cache-dir --upgrade --user ansible && \
    python3 -m pip install --no-cache-dir --upgrade --user kubernetes && \
    python3 -m pip install --no-cache-dir --upgrade --user netaddr && \
    python3 -m pip install --no-cache-dir --upgrade --user dnspython

ENTRYPOINT ["ansible-playbook", "-e", "running_in_container=true"]

COPY --chown=${USER}:0 . .

RUN set -x && \
    ansible-playbook -vvv -i prereq-play/inventory prereq-play/prereq-play.yml playbooks/build-galaxy-collection.yml
