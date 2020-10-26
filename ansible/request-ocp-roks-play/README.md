# request-ocp-roks-plan

## Usage

1. To ensure the correct version of the ibm.cloudcollection collection is used run the following command to install: `ansible-galaxy collection install -r requirements.yml`
2. Copy examples/roks-vars.yml up one folder
   `cp examples/roks-vars.yml .`
3. Edit roks-vars.yml as needed (see documentation in the example roks-vars.yml file).
4. Execute the playbook: `ansible-playbook -i localhost request-roks.yml`
    * Other options:
        * use -e to set variables from the command line like `-e clusterName=testcluster01`
        * use -v for verbose output (-vvv for more, -vvvv to enable connection debugging)
