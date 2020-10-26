from common.http_request import Httprequest

class Gettoken:
    def Count(self):
        url="http://api.keyou.site:8000/user/chenran/count"
        param=''
        res=Httprequest(url,param).http_request("get")
        #print(res.json())
        return res.json()

    def get_token(self):
        a=Gettoken().Count()
        #count=0,表示该账户没有注册
        if a["count"]==0:
            url="http://api.keyou.site:8000/user/register/"
            param={"username":"chenran", "password":"cr921212","email":"1049162286@qq.com","password_confirm":"cr921212"}
            res=Httprequest(url,param).http_request("post")
            token_register=res.json()["token"]
            return token_register
        else: #调用登录的接口，获取token
            url="http://api.keyou.site:8000/user/login/"
            param={"username":"chenran", "password":"cr921212"}
            res=Httprequest(url,param).http_request("post")
            token_login=res.json()["token"]
            return token_login
if __name__ == '__main__':
    token=Gettoken().get_token()
    print(token)


