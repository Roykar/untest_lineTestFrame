import unittest
import requests
import datetime
from common import readconfig,gettoken


class testCreateTask(unittest.TestCase):
    def setUp(self):
        self.sesstion = requests.session()
        self.data = readconfig.readconfig()
        self.token= gettoken.getToken()

    def tearDown(self):
        self.sesstion.close()


    def test_create_task(self):
        self._testMethodName = 'case02'
        self._testMethodDoc = '创建测量任务'


        header={"Content-Type": "application/json",
                 "token":self.token.test_get_token()
        }
        # 获取当前时间然后转换为str
        curr_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
        get_param_create={"JHRW_DJCCLJH_FC":"2c94951963910cfa016396eee8740243",
                              "JHRW_DJCCLJH_BC_ID":"6050F70ECF1A41C6974729DF3B3AD8DF",
                              "JHRW_DJCCLJH_BM":"2c94e68271c4b86f0171c8a09e4f00a3",
                              "JHRW_DJCCLJH_BM_NAME":"",
                              "JHRW_DJCCLJH_CLXMIDJH":"1D93845396E2234dfsfsdC872DE414",
                              "JHRW_DJCCLJH_CLDXFWID":"1099",
                              "JHRW_DJCCLJH_CLRY":"2c94e68271c4b86f0171c8a5686100c4",
                              "JHRW_DJCCLJH_CJSJ":time_str,
                              "JHRW_DJCCLJH_BZ":"新增槽测量任务说明",
                              "JHRW_DJCCLJH_CLRY_NAME":"槽测量员1",
                              "JHRW_DJCCLJH_CLFS":"1",
                              "JHRW_DJCCLJH_BC":"白班"}
        hosts = self.data.get_hosts_zlst('hosts')
        response = self.sesstion.post( url='%s/gateway/api-product-control/slot-task/createTempTask' % hosts,
                                       json=get_param_create,
                                       headers=header)
        result =response.json()['message']
        self.assertEqual(result,'新增成功','新增任务失败')
if __name__ == '__main__':
    unittest.main()