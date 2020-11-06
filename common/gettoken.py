import requests
from common import readconfig
class getToken:
    def test_get_token(self):
        self.session = requests.session()
        self.data = readconfig.readconfig()
        get_param_dict_token = {
            "username": self.data.get_hosts_zlst('username'),
            "password": self.data.get_hosts_zlst('password'),
            "securityCode": ""
        }
        hosts = 'http://proxy.bl-smart-factory.paas.com'
        response_token = self.session.get(url='%s/gateway/api-ms/authorize/login' % hosts,
                                params=get_param_dict_token)
        actual_result = response_token.json()['access_token']
        return actual_result


