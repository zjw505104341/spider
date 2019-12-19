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
        'entry': 'weibo',
        'gateway': '1',
        'savestate': '7',
        'qrcode_flag': 'false',
        'useticket': '1',
        'pcid': pcid,
        'door': yan,
        'vsnf': '1',
        'su': user,
        'service': 'miniblog',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'rsakv': '1330428213',
        'sp': password,
        'sr': '1920*1080',
        'encoding': 'UTF-8',
        'prelt': random.randint(100, 500),
        'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }

    headers = {
        'User-Agent': 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
        'Host': 'login.sina.com.cn',
        'Referer': 'https://www.weibo.com/login.php',
    }


    # 使用  requests.session()   保持登陆   保存cookies信息
    s = requests.session()

    #  post请求后有 location.replace 页面跳转   连着跳转2次  获取重要参数  uuiqueid    用户唯一标识符
    res = s.post(url=url, headers=headers, data=data)
    print('post请求成功')

    #  第一次  匹配   进行请求
    pa = r'location\.replace\([\'"](.*?)[\'"]\)'
    url_2 = re.findall(pa, res.content.decode('gbk'))[0]
    res_2 = s.get(url=url_2)
    print('第一次get请求成功')


    #  第二次进行匹配  进行请求
    url_3 = ''.join(re.findall("location.replace\('(.*?)'\);}\);}",res_2.content.decode('gb2312'),re.S))
    res_3 = s.get(url_3)
    print(res_3.text)
    print('第二次get请求成功')


    #  获取到请求后去请求主页  模拟登陆成功  用户的唯一标识uniqueid
    uniqueid = ''.join(re.findall('{"uniqueid":"(\d+)",',res_3.text, re.S))
    url_4 = 'https://weibo.com/u/' + str(uniqueid) + '/home?wvr=5&lf=reg'
    res_4 = s.get(url_4)
    print('登陆成功')
    print(res_4.text)
    print('个人主页请求成功')



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


