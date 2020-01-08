import requests,execjs,re,base64,hashlib,json


"""
参考博客      https://mp.weixin.qq.com/s/kziqciY7hTSXUBwPJoVNSw
目标网站      http://99718h.com/


首次请求      http://99718h.com/cn/register
二次请求      http://99718h.com/cn/login


zzy123456
123456qq
"""


def index_1(s,headers):
    url = 'http://99718h.com/cn/register'
    res = s.get(url=url, headers=headers)
    cookie = res.headers['Set-Cookie']
    web = cookie.split('; path=/,')[0]
    randomYes = cookie.split('; path=/,')[1]
    data_list = [
        web.replace('web=', '').replace(' ', ''),
        randomYes.replace('randomYes=', '').replace(' ', '')
    ]
    return data_list



def index_2(s,headers, data_list):
    username = input('请输入账号：')
    pwd = input('请输入密码：')
    ctx = execjs.compile(open('login.js', encoding='utf-8').read())
    passwrod = ctx.call('get_pwd', data_list[0], data_list[1], pwd)
    print('加密过后的密码为：', passwrod)

    url = 'http://99718h.com/cn/login'
    data = {
    'username': username,
    'password': passwrod,
    'crypt': '1'
    }
    res = s.post(url=url, data=data, headers=headers)
    html = json.loads(res.text)
    print(html)


if __name__ == '__main__':
    headers = {
        'Referer': 'http://99718h.com/cn/register',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    s = requests.session()
    data_list = index_1(s,headers)
    index_2(s,headers,data_list)

