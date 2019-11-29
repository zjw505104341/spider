import execjs,requests,re,hashlib
#     http://interlib.sdust.edu.cn/opac/reader/login

def getpassword(password):
    ctx = execjs.compile(open('dushu.js', 'r').read())
    pwd = ctx.call('md5', password)
    print('加密密码成功')
    return pwd

def index_1():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    url = 'http://interlib.sdust.edu.cn/opac/reader/login'
    res = requests.get(url=url, headers=headers)
    cookies = requests.utils.dict_from_cookiejar(res.cookies)
    print('第一次请求  获取 cookie成功')
    return cookies

def login():
    username = '1501030101'
    user_password = '1501030101'
    cookie_1 = index_1()
    jsessionid = cookie_1['JSESSIONID']

    url = 'http://interlib.sdust.edu.cn/opac/reader/doLogin;jsessionid='+ jsessionid
    # rdPasswd = hashlib.md5(user_password.encode()).hexdigest()
    rdPasswd = getpassword(user_password)
    data = {
        "rdid": username,
        "rdPasswd": str(rdPasswd),
        "returnUrl": "",
        "password": "",
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    }
    res = requests.post(url=url, data=data, headers=headers, allow_redirects=False)
    cookie = requests.utils.dict_from_cookiejar(res.cookies)
    print('模拟登录成功')
    print(cookie)
    return cookie


if __name__ == '__main__':
    login()