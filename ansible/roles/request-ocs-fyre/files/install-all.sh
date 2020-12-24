#!/bin/bash

./00.label-nodes.sh && \
./01.install-ocs-operator.sh && \
./02.install-local-storage-operator.sh && \
./03.install-local-volumes.sh && \
./04.install-storage-cluster.sh
