import requests,execjs,re,json,base64
from pprint import pprint


class login:
    def __init__(self) -> None:
        self.ctx = execjs.compile(open('login.js', 'r', encoding='UTF-8').read())
        self.url_1 = 'https://passport.migu.cn/password/publickey'
        self.url_2 = 'https://passport.migu.cn/authn'
        self.url_3 = 'https://passport.migu.cn/captcha/graph/risk?imgcodeType=1&showType=1&sourceid=203021'
        self.headers = {
            'Host': 'passport.migu.cn',
            'Origin': 'https://passport.migu.cn',
            'Referer': 'https://passport.migu.cn/login?sourceid=203021&apptype=2&forceAuthn=true&isPassive=false&authType=&display=&nodeId=70027513&relayState=login&weibo=1&callbackURL=http%3A%2F%2Fwww.miguvideo.com%2Fmgs%2Fwebsite%2Fprd%2Findex.html%3FisIframe%3Dweb',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        }


    def index_1(self, s):
        res = s.post(url=self.url_1, headers=self.headers)
        html = res.text
        json_html = json.loads(html)
        print(json_html)
        if json_html['status'] == 2000:
            result = json_html['result']
            return result

    def index_2(self, result, s, img_str, passwrod, username):

        modulus = result['modulus']
        publicExponent = result['publicExponent']
        pwd = self.ctx.call('get_pwd', modulus, publicExponent, passwrod)
        obj_json = self.ctx.call('get_l', modulus, publicExponent)
        details = obj_json['details']
        result = obj_json['result']

        data = {
            'sourceID': '203021',
            'appType': '2',
            'relayState': 'login',
            'loginID': username,
            'enpassword': pwd,
            'captcha': img_str,
            'imgcodeType': '1',
            'fingerPrint': result,
            'fingerPrintDetail': details,
            'isAsync': 'true'
        }

        res = s.post(url=self.url_2, headers=self.headers, data=data)
        html = json.loads(res.text)
        if html['status'] == 2000:
            print('登录成功', html['result']['token'])
        else:
            print('登录失败')



    def index_3(self, s):
        res = s.get(url=self.url_3, headers=self.headers)
        html = json.loads(res.text)
        if html['status'] == 2000:
            img = html['result']['captchaurl']
            with open('yzm.jpg', 'wb')as p:
                p.write(base64.b64decode(img.replace('data:image/jpeg;base64,', '')))


if __name__ == '__main__':
    s = requests.session()

    login_obj = login()
    result = login_obj.index_1(s)
    login_obj.index_3(s)
    img_str = input('请输入验证码：')
    passwrod = input('请输入密码：')
    username = input('请输入账号：')
    login_obj.index_2(result, s, img_str, passwrod, username)







