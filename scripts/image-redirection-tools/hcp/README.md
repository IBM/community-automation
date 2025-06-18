# Overview

On [OpenShift Hosted Control Planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/hosted_control_planes/hosted-control-planes-overview), there is no first class support for image registry redirection, which is on OpenShift deployments provided via [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/images/image-configuration#images-configuration-blocked-payload) or [`ImageDigestMirrorSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.14/html/config_apis/imagedigestmirrorset-config-openshift-io-v1)

There if RFE to provide support for image registry redirection https://issues.redhat.com/browse/XCMSTRAT-994 , yet this document provides stop-gap solution on Hosted Control Planes, before the first class support is provided.

The procedure consists of two steps:
- creating an image pull secret for the registry mirror to use
- create a (privileged) `DaemonSet` which updates the worker node's container runtime configuration file, `/var/lib/kubelet/config.json`

## Step 1 - create a secret for the additional config.json.

The config.json can be created by `podman login --authfile`:

```sh
podman login -u [user]] -p [password] --authfile=/path/to/your/additional/config.json  [registry]
```

Create the image pull secret `docker-auth-secret` in `kube-system` namespace:

```sh
oc create secret generic docker-auth-secret \
--namespace kube-system \
--from-file=.dockerconfigjson=/path/to/your/additional/config.json \
--type=kubernetes.io/dockerconfigjson --dry-run=client -o yaml | oc apply -f 
```

## Step 2 - create a DaemonSet updating container runtime configuration

The DeamonSet init container updates the container runtime configuration on each of the worker node and then sleeps indefinitely.

```sh
oc apply -f update-docker-config-ds.yaml
```
