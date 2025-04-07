import re

class FilterModule(object):
    def filters(self):
        return {
            'get_twas_server_names': self.get_twas_server_name,
        }

    def get_twas_server_name(self, data):
        m = re.search('"([^"]*)"', data)
        return m.group(1)
