# coding=utf-8
import requests,execjs
from pprint import pprint
url = 'https://passport.fang.com/login.api'
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '316',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'g_sourcepage=txz_dl%5Egg_pc',
    'Host': 'passport.fang.com',
    'Origin': 'https://passport.fang.com',
    'Pragma': 'no-cache',
    'Referer': 'https://passport.fang.com/?backurl=http%3a%2f%2fmy.fang.com%2f',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
pwd = execjs.compile(open('js_1.js', 'r').read()).call('getpwd', '123456')
data = {
    'uid': '13566669999',
    'pwd': pwd,
    'Service': 'soufun-passport-web',
    'AutoLogin': '1',
}
res = requests.post(url=url, headers=headers,data=data)
pprint(res.json())
