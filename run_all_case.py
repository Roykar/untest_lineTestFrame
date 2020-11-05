#project:untest_lineTestFrame
#author:Roykar
#date:2020/11/2,22:38

import unittest
import os
from common import HTMLTestReportCN

case_path= os.path.join(os.path.dirname(__file__),'testcase/')                #测试用例存放路径
discover = unittest.defaultTestLoader.discover(start_dir=case_path,           #能执行的测试用例的存放路径
                                               pattern='test_*.py',           #执行以"test_"开头的py文件
                                               top_level_dir=case_path)

all_case_suite = unittest.TestSuite()        #创建测试用例套件对象
all_case_suite.addTest(discover)             #将所有符合条件的用例加入测试套件

report_path = os.path.join(os.path.dirname(__file__), 'Reports/')  #测试报告存放路径
print(report_path)
report_dir = HTMLTestReportCN.ReportDirectory(report_path)  # 创建一个测试报告路径对象
report_dir.create_dir('API_TEST')  # 调用创建目录的方法
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')  # 获取测试报告的路径
report_html_file = open(report_html_path, 'wb')
html_runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_file,
                                              title='微信公众平台测试报告',
                                              description='接口测试矿建实战使用',
                                              tester='Roykar')
html_runner.run(all_case_suite)
