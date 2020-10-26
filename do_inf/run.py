import unittest
import HTMLTestRunnerNew
from common.test_httprequest import TestHttpRequest
from conf import read_path
import os
import time
from common.send_email import sendEmail

suite=unittest.TestSuite()
loader=unittest.TestLoader()
#加载测试用例
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

#执行测试用例
# runner=unittest.TextTestRunner()
# runner.run(suite)

#将测试的结果写入到指定的文件中去
# with open('test.txt','w+') as file:
#     runner=unittest.TextTestRunner(file,'test',2)
#     runner.run(suite)

now=time.strftime('%Y-%m-%d_%H_%M_%S')
path=os.path.join(read_path.report_path,'test_api'+now+'.html')

#生成测试报告
with open(path,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,title='cr-test',description='登录模块',tester='chenran')
    runner.run(suite)

email_to='1049162286@qq.com'
sendEmail().send_email(email_to,path)