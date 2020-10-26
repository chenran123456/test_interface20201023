import requests,json
from common.my_log import MyLog

logger=MyLog('登录模块')

class  Httprequest:
    #初始化url和param，url:访问地址  param:请求参数
    def __init__(self,url,param):
        self.url=url
        self.param=param
    def http_request(self,method,headers=None,cookies=None):
        if method.upper()=='GET':
            try:
                res=requests.get(self.url,self.param,headers=headers,cookies=cookies)
            except Exception as e:
                logger.error("执行get请求报错，错误是：{0}".format(e))
        elif method.upper()=='POST':
            try:
                res=requests.post(self.url,self.param,headers=headers,cookies=cookies)
            except Exception as e:
                logger.error("执行post请求报错，错误是：{0}".format(e))
        else:
            print("你的请求方式不对！")
        return res

if __name__ == '__main__':
   url="http://api.keyou.site:8000/user/chenran/count/"
   param=" "
   #param={"username":"chenran123", "password":"cr921212"}
   #token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6ImNoZW5yYW4iLCJleHAiOjE2MDA5MTA3NjEsImVtYWlsIjoiY3IxMDQ5MTYyMjg2QDE2My5jb20ifQ.Htpfw60gVioi7kyh9Vd4MLVDl_rlgCZJrliM4Ar1ZAg"
   #headers={'Authorization':"JWT"+token}
   res=Httprequest(url,param).http_request("get")
   print(res.json())
   print(res.status_code)
