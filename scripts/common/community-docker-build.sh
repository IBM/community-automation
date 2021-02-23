#!/bin/bash

# currently being maintained by Ray Ashworth

# bash best practices
set -o errexit
set -o nounset
set -o pipefail

git clone ../../. community-automation
docker build . -t quay.io/rayashworth/community-ansible:latest
docker login quay.io -u $quay_user -p $quay_password
docker push quay.io/rayashworth/community-ansible:latest
