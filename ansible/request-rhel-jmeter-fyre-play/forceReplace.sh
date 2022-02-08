#!/bin/bash
ansible-playbook -i somehost.fqdn, jmeter-play.yml \
-e jmeterUser=nest \
-e noLog=false \
-e javaArchive='https://github.com/ibmruntimes/semeru17-binaries/releases/download/jdk-17.0.2+8_openj9-0.30.0/ibm-semeru-open-jdk_x64_linux_17.0.2_8_openj9-0.30.0.tar.gz' \
-e jmeterArchive='http://somehost.fqdn/binaries/jmeter/apache-jmeter-5.4.3.zip' \
-e jmeterManagerPluginUrl='https://jmeter-plugins.org/get/' \
-e forceReplace=true  \
