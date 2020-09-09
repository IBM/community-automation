# request-ocp-roks-plan

## Usage

1. To ensure the correct version of the ibm.cloudcollection collection is used: `ansible-galaxy collection install -r requirements.yml`
2. Execute the play: `ansible-playbook -i localhost request-roks.yaml`
    * Other options:
        * use -e to set variables from the command line like `-e clusterName=testcluster01`
        * use -C to test the play without creating the cluster
        * use -v for verbose output (-vvv for more, -vvvv to enable connection debugging)

