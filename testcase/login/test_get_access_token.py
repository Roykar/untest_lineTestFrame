import unittest
import requests
from common import readconfig

class testGetAccessToken(unittest.TestCase):
    def setUp(self):                   #初始化
        self.session = requests.session()
        self.data= readconfig.readconfig()
    def tearDown(self):                #测试清理
        self.session.close()

    def test_get_token(self):
        self._testMethodName = 'case01'    #用例名称
        self._testMethodDoc = '中铝视拓-登录'#用例说明
        get_param_dict_token = {
            "username": self.data.get_hosts_zlst('username'),
            "password": self.data.get_hosts_zlst('password'),
            "securityCode": ""
        }
        hosts =self.data.get_hosts_zlst('hosts')
        response_token = self.session.get(url='%s/gateway/api-ms/authorize/login' % hosts,
                                          params=get_param_dict_token)
        actual_result = response_token.json()['resultMsg']
        self.assertEqual(actual_result,'登录成功','登录失败')
        actual_token =response_token.json()['access_token']
        return actual_token
if __name__ == '__main__':
    unittest.main()