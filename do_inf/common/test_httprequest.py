import unittest
import json
import uuid
import os
from common.http_request import Httprequest
from ddt import ddt,data
from common.do_excel import DoExcel
from conf import read_path
from common.my_log import MyLog
from common.get_token import Gettoken

logger=MyLog('登录模块')
path=os.path.join(read_path.test_data_path)
test_data=DoExcel(path,'test_data').do_excel()
TOKEN=Gettoken().get_token()

@ddt
class TestHttpRequest(unittest.TestCase):

    @data(*test_data)
    def test_case(self,item):
        global TOKEN
        headers={'Authorization':"JWT"+TOKEN}
        res=Httprequest(item['url'],eval(item['param'])).http_request(item['method'],headers=headers)
        logger.info("第{0}条用例执行的结果的是：{1}".format(item['case_id'],res.status_code))

if __name__ == '__main__':
    unittest.main()
