#!/usr/bin/python3
# Retrieves the latest releases from GitHub and compares the release time with the local file time
# If the latest release is newer, the local directories are emptied 
# Files are downloaded from GitHub if they match the format in os_dict
#
# @Authors: Jonathan.Maciel@ibm.com schader@us.ibm.com
# This was copied from IBM WebSphere SVT NEST processing
# It would be great if this logic could be pure ansible
#
# currently it is used for IBM WebSphere Liberty Operating System Certification setup 
# which runs in a container, thus /home/nest/jdk/XX is a known directory to the setup logic
#

import requests
import json
import os 
import datetime
import time

url_dict = {'https://api.github.com/repos/ibmruntimes/semeru8-binaries/releases/latest': '/home/nest/jdk/IBMjdk8.OpenJ9/',    
            'https://api.github.com/repos/ibmruntimes/semeru11-binaries/releases/latest': '/home/nest/jdk/IBMjdk11.OpenJ9/',
            'https://api.github.com/repos/ibmruntimes/semeru17-binaries/releases/latest': '/home/nest/jdk/IBMjdk17.OpenJ9/',
            'https://api.github.com/repos/ibmruntimes/semeru18-binaries/releases/latest': '/home/nest/jdk/IBMjdk18.OpenJ9/'}

os_dict = {'x64_windows': 'zip',
           'ppc64le': 'gz',
           'ppc64_aix': 'gz',
           'x64_linux': 'gz',
           's390x_linux': 'gz'}

def check_data(url, dir):
    session = requests.Session()
    r = session.get(url)
    print('-- url: %s r.status_code %s' % (url,r.status_code,))
    data = json.loads(r.content)
    if r.status_code == 200:
        
        published_time = time.mktime(datetime.datetime.strptime(data['published_at'], '%Y-%m-%dT%H:%M:%SZ').timetuple())
        print('-- checking remote file time: %s' % (published_time,))
        print('-- checking local file time: %s' % (dir,))
        old_file_time = os.stat(dir).st_mtime

        if published_time > old_file_time or len(os.listdir(dir)) == 0:
            # remove all files in directory
            for file in os.scandir(dir):
                print('-- Removing local file: %s' % (file,))
                os.remove(file.path)
                
            assets = data['assets']
            for asset in assets:
                for key in os_dict:
                    prefixes = ['ibm-semeru-open-jdk_' + key, 'ibm-semeru-certified-jdk_' + key]
                    # match with front and back of file name
                    for prefix in prefixes:
                        if prefix == asset['name'][0:len(prefix)] and os_dict[key] == asset['name'][-len(os_dict[key]):]:
                            r = session.get(asset['url'], headers={'User-Agent': 'request', 'Accept':'application/octet-stream'})
                            with open(dir + asset['name'], 'wb') as f:
                                f.write(r.content)
                                f.close()
        else:
            print('no new updates yet')
    else:
        print('--  session error: %s' % (data,))
        exit(r.status_code)

if __name__ == "__main__":
    for key in url_dict:
        check_data(key, url_dict[key])
