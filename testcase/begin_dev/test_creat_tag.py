# #project:untest_lineTestFrame
# #author:Roykar
# #date:2020/11/4,23:07
#
# import unittest
# import requests
# from common import readconfig
#
# class creat_tag(unittest.TestCase):
#     def setUp(self):                   #初始化
#         self.session = requests.session()
#         self.data= readconfig.readconfig()
#     def tearDown(self):                #测试清理
#         self.session.close()
#
#     def test_creat_tag(self):
#         self._testMethodName = 'case02'    #用例名称
#         self._testMethodDoc = '用户管理-创建标签'#用例说明
#         get_param_dict_token = {
#             "grant_type": "client_credential",
#             "appid": self.data.get_host_wx('appid'),
#             "secret": self.data.get_host_wx('secret')
#         }
#         hosts = self.data.get_host_wx('host')
#         response_token = self.session.get(url='%s/cgi-bin/token' % hosts,
#                                 params=get_param_dict_token)
#         actual_result = response_token.status_code
#         self.assertEqual(actual_result,200,'case01 验证get_acess_token接口是否调用成功')
#         actual_token =response_token.json()['access_token']
#
#         print(actual_token)
# if __name__ == '__main__':
#     unittest.main()
