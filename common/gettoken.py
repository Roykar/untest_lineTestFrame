import requests

class getToken:
    def test_get_token(self):
        self.session = requests.session()
        get_param_dict_token = {
            "username": "ccl001",
            "password": "Nim67D3RL/Wfxp43PCXWY9sLuZ7qoZkzn/Cm1393cDxntQ/BDr0eeHRCUhMF7stelna4wGUkY45b8n/Ro4x2iWyszLYxj87RdNMD6BK5wzZGFCpUanzfOIWTk+vAiiv8uoKbQ+J1FeWQYjkx4YRxhoSnEhhN5NxBr8TVy7awvz8=",
            "securityCode": ""
        }
        hosts = 'http://proxy.bl-smart-factory.paas.com'
        response_token = self.session.get(url='%s/gateway/api-ms/authorize/login' % hosts,
                                params=get_param_dict_token)
        actual_result = response_token.json()['access_token']
        return actual_result


