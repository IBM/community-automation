import re

class FilterModule(object):
    def filters(self):
        return {
            'get_twas_server_status': self.get_twas_server_status,
        }

    def get_twas_server_status(self, data):
        m = re.search('"([^"]*)"', data)
        return m.group(1)
