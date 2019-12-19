import execjs,re,requests,json,time



class Login_anjuke():

    def __init__(self) -> None:

        self.session = requests.session()
        self.session.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
        }

    #   调用js  密码加密
    def encode_pwd(self, pwd, rsaModulus, rsaExponent):
        ctx = execjs.compile(open('anjuke.js', 'r').read())
        password = ctx.call('encrypt_password', pwd, rsaModulus, rsaExponent)
        print('密码加密成功', password)
        return password

    #   进行登录操作
    def login(self, username, pwd, token):
        url = 'https://cloud-passport.anjuke.com/ajk/login/pc/dologin'
        data = {
            'username': username,
            'password': pwd,
            'token': token,
            'source': 'ajk-anjuke-pc',
            'path': 'https%3A%2F%2Fshanghai.anjuke.com%2F%3Fpi%3DPZ-baidu-pc-all-biaoti',
            'domain': 'anjuke.com',
            'finger2': 'zh-CN|24|1|6|1920_1080|1920_1040|-480|1|1|1|undefined|1|unknown|Win32|unknown|3|false|false|false|false|false|0_false_false|d41d8cd98f00b204e9800998ecf8427e|f7bc91acfdafdfa98b7636d86db4a2f4',
            'psdk-d': 'jsdk',
            'psdk-v': '1.0.1',
            'callback': 'SDK_CALLBACK_FUN.successFun',
        }
        self.session.headers['referer'] = 'https://login.anjuke.com/login/iframeform?style=1&forms=11&third_parts=111&other_parts=111&history=aHR0cHM6Ly9zaGFuZ2hhaS5hbmp1a2UuY29tLz9waT1QWi1iYWlkdS1wYy1hbGwtYmlhb3Rp&check_bind_phone=1&t=1576732286880'
        res = self.session.post(url=url, data=data, headers=self.session.headers)
        print(res.text)


    #  请求接口获取token
    def gettoken(self):
        url = 'https://cloud-passport.anjuke.com/ajk/mobile/init?'
        callback = f'JsonpCallBack{str(int(time.time()*1000000))}'
        params = {
            'source': 'ajk-anjuke-pc',
            'path': 'https%3A%2F%2Flogin.anjuke.com%2Flogin%2Fiframeform%2F',
            'psdk-d': 'jsdk',
            'psdk-v': '1.0.1',
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
        url = 'https://cloud-passport.anjuke.com/ajk/rsa?'
        callback = f'JsonpCallBack{str(int(time.time()*1000000))}'
        params = {
            'source': 'ajk-anjuke-pc',
            'psdk-d': 'jsdk',
            'psdk-v': '1.0.1',
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

    obj_anjuke = Login_anjuke()
    rsaModulus, rsaExponent = obj_anjuke.get_key()
    pwd = obj_anjuke.encode_pwd(password, rsaModulus, rsaExponent)
    token = obj_anjuke.gettoken()
    obj_anjuke.login(username, pwd, token)



