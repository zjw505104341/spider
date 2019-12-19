import re,time,random,math,json,requests,execjs

"""

    微博加密参数有两个   用户名和密码
    用户名为           base64加密
    密码               RSA加密
    
    
"""


def Get_parameters(su):
    """

    这个方法是初步请求    为获取后面必要参数

    返回  pubkey, times, nonce, rsakv, pcid, servertime   这些必须用到的参数
    """
    try:
        url = f"https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su={su}&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_={str(int(time.time()*1000))}"
        headers = {
            'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
            'Host': 'login.sina.com.cn',
            'Referer': 'https://www.weibo.com/login.php',
        }
        res = requests.get(url=url, headers=headers)

        #   正则匹配把里面的字典取出
        data = ''.join(re.findall('sinaSSOController.preloginCallBack\((.*?)\)', res.text, re.S))
        new_data = json.loads(data)

        times = new_data.get('servertime')
        nonce = new_data.get('nonce')
        pubkey = new_data.get('pubkey')
        rsakv = new_data.get('rsakv')
        pcid = new_data.get('pcid')
        servertime = new_data.get('servertime')

        return pubkey, times, nonce, rsakv, pcid, servertime
    except Exception as err:
        print('访问失败', err)


def get_user_pwd(username, pwd):
    """
    :param pwd:username
    :return:  返回加密的过后的用户名加密码
    """

    # 读取 同级文件夹下execute.js文件  并载入  execjs 库
    js = execjs.compile(open('execute.js', 'r', encoding='utf-8').read())

    #  打印当前执行js的环境
    print('引擎', execjs.get().name)

    # 执行js方法 getusername   传入username   返回 加密过后用户名
    user = js.call('getusername', username)

    # 调用Get_parameters方法  传入参数  加密过后的用户名    让其返回  动态参数  方便后面的调用
    publickey, time, nonce, rsakv, pcid, servertime = Get_parameters(user)

    # 执行js方法 get_up   传入动态参数进行加密操作  获取加密过后的password
    password = js.call('get_up', pwd, publickey, time, nonce)

    # 返回加密过后的username   password   需要请求的动态参数  pcid   servertime   nonce
    return user, password, pcid, servertime, nonce

def getyzm(pcid):
    """

    这个方法的目的是   传入对应的动态参数   返回一张认证过后的验证码  并且下载
    :param pcid:
    :return:
    """
    headers = {
        'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
        'Host': 'login.sina.com.cn',
        'Referer': 'https://www.weibo.com/login.php',
    }
    params = {
        #     r参数   是看js  用py重写的
        'r': math.floor(random.random() * math.pow(10, 8)),
        's': '0',
        'p': pcid           #   pcid是之前动态参数
    }

    url = 'https://login.sina.com.cn/cgi/pin.php'
    res = requests.get(url=url, params=params, headers=headers)
    with open('xinlang.png', 'wb') as p:
        p.write(res.content)

def login(user, password, pcid, servertime, nonce, yan):
    url = f'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)&_={str(int(time.time()*1000))}'

    data = {
        'entry': 'account',
        'gateway': '1',
        'from': 'null',
        'savestate': '30',
        'qrcode_flag': 'true',
        'useticket': '0',
        'pcid': pcid,
        'door': yan,
        'vsnf': '1',
        'su': user,
        'service': 'sso',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'rsakv': '1330428213',
        'sp': password,
        'sr': '1920*1080',
        'encoding': 'UTF-8',
        'prelt': random.randint(100, 500),
        'domain': 'sina.com.cn',
        'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'TEXT'
    }

    headers = {
        'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
        'Host': 'login.sina.com.cn',
        'Referer': 'https://www.weibo.com/login.php',
    }


    #  post请求后有 location.replace 页面跳转   连着跳转2次  获取重要参数  uuiqueid    用户唯一标识符
    res = requests.post(url=url, headers=headers, data=data)
    print(res.content.decode())
    print('post请求成功，登录成功')



if __name__ == '__main__':
    username = input('请输入用户名:')
    pwd = input('请输入密码:')

    #   这是第一次请求  用加密过后的用户名去请求  获取rsa  秘钥  去加密密码
    user, password, pcid, servertime, nonce = get_user_pwd(username, pwd)
    print('用户名加密后为：',user)
    print('密码加密后为：', password)
    print('请求验证码需要的pcid为：', pcid)
    print('服务器返回的servertime为：', servertime)
    print('服务器返回的nonce：', nonce)

    #  传入 pcid  获取认证过后的验证码
    getyzm(pcid)
    yan = input('请输入验证码：')


    # 进行登陆操作
    login(user, password, pcid, servertime, nonce, yan)


