#project:untest_lineTestFrame
#author:Roykar
#date:2020/11/2,22:45

import requests
import unittest
from common import readconfig

class TestGetAcessToken(unittest.TestCase):
    def setUp(self):                   #初始化
        self.session = requests.session()
        self.data= readconfig.readconfig()
    def tearDown(self):                #测试清理
        self.session.close()

    def test_get_acesstoken(self):
        self._testMethodName = 'case01'    #用例名称
        self._testMethodDoc = '获取微信公众号token'#用例说明
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": self.data.get_host_wx('appid'),
            "secret": self.data.get_host_wx('secret')
        }
        hosts = self.data.get_host_wx('host')
        response = self.session.get(url='%s/cgi-bin/token' % hosts,
                                params=get_param_dict)
        actual_result = response.status_code
        self.assertEqual(actual_result,200,'case01 验证get_acess_token接口是否调用成功')


if __name__ == '__main__':
        unittest.main()
