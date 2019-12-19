import execjs,re,requests,json,time

"""

一个账号多次登录会出现验证码  
验证码请自行拓展

58同城和安居客用的登录都是一样的   rsa 密码加密 

"""

class Login_58():

    def __init__(self) -> None:

        self.session = requests.session()
        self.session.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
        }

    #   调用js  密码加密
    def encode_pwd(self, pwd, rsaModulus, rsaExponent):
        ctx = execjs.compile(open('58js.js', 'r').read())
        password = ctx.call('encrypt_password', pwd, rsaModulus, rsaExponent)
        print('密码加密成功', password)
        return password

    #   进行登录操作
    def login(self, username, pwd, token):
        url = 'https://passport.58.com/58/login/pc/dologin'
        data = {
            'username': username,
            'password': pwd,
            'token': token,
            'source': '58-default-pc',
            'path': f'https%3A%2F%2Fsh.58.com%2F%3Fpts%3D{str(int(time.time()*1000))}',
            'domain': '58.com',
            'finger2': 'zh-CN|24|1|6|1920_1080|1920_1040|-480|1|1|1|undefined|1|unknown|Win32|unknown|3|false|false|false|false|false|0_false_false|d41d8cd98f00b204e9800998ecf8427e|f7bc91acfdafdfa98b7636d86db4a2f4',
            'psdk-d': 'jsdk',
            'psdk-v': '1.0.2',
            'fingerprint': 'lDwO9vjOKdkRgmjeJefG3y6V91EAIDDQ',  #  这个参数应该是动态的  目前没有具体研究  后续若是需要  可以研究一下
            'callback': 'SDK_CALLBACK_FUN.successFun',
        }
        self.session.headers['referer'] = 'https://passport.58.com/login/?path=https%3A//sh.58.com/&PGTID=0d100000-0000-28d7-74d1-22ae16c73fa2&ClickID=2'
        res = self.session.post(url=url, data=data, headers=self.session.headers)
        print(res.text)


    #  请求接口获取token
    def gettoken(self):
        url = 'https://passport.58.com/58/login/init?'
        callback = f'JsonpCallBack{str(int(time.time()*1000000))}'
        params = {
            'source': '58-default-pc',
            'path': f'https%3A%2F%2Fsh.58.com%2F%3Fpts%3D{str(int(time.time()*1000))}',
            'psdk-d': 'jsdk',
            'psdk-v': '1.0.2',
            'callback': callback,
        }
        res = self.session.get(url=url, params=params, headers=self.session.headers).text
        token_obj = json.loads(res.replace(callback+'(', '').replace(')', ''))
        msg = token_obj['msg']
        if msg == '成功':
            token = token_obj['data']['token']
            print('获取token成功：',token)
            return token

    #  请求接口  获取rsa密钥
    def get_key(self):
        url = 'https://passport.58.com/58/rsa?'
        callback = f'JsonpCallBack{str(int(time.time()*1000000))}'
        params = {
            'source': '58-default-pc',
            'psdk-d': 'jsdk',
            'psdk-v': '1.0.2',
            'callback': callback,
        }
        res = self.session.get(url=url, params=params, headers=self.session.headers).text
        token_obj = json.loads(res.replace(callback+'(', '').replace(')', ''))
        msg = token_obj['msg']
        if msg == '成功':
            rsaModulus = token_obj['data']['rsaModulus']
            rsaExponent = token_obj['data']['rsaExponent']
            print('获取rsaModulus成功：', rsaModulus)
            print('获取rsaExponent成功：', rsaExponent)
            return rsaModulus,rsaExponent




if __name__ == '__main__':

    username = input('请输入账号：')
    password = input('请输入密码：')

    obj_58 = Login_58()
    rsaModulus, rsaExponent = obj_58.get_key()
    pwd = obj_58.encode_pwd(password, rsaModulus, rsaExponent)
    token = obj_58.gettoken()
    obj_58.login(username, pwd, token)

