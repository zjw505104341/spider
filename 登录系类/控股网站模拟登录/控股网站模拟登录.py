# -*- coding: utf-8 -*-
# !/usr/bin/python3
# Author: zhou jun wei
# CreatDate: 2020/12/15 11:09

# https://pspcc.bpic.com.cn/app/#/  模拟登录

import random, requests, execjs
from PIL import Image
session = requests.session()  #  保持登录 session  用这个是必须得

js_code = r"""
// 第一步  npm install crypto-js

var JSON_PROTECTION_PREFIX = /^\)\]\}',?\n/;
var key="c2lub3NvZnQuY2hhbm5lbC55ZHBpYw==";
var CryptoJS = require("crypto-js");
var isString=function(value) {return typeof value === 'string';};
var fromJson=function (json) { return isString(json) ? JSON.parse(json) : json;};
function get_pwd(userName, pwd, yzm) {
    temp = {
        "head": {"transCode":"Login","transType":"Req","token":""},
        "userCode": userName,"pwd": pwd,
        "verification": yzm,
        "loginSystemCode":"",
        "isTelemarketing":"0"
    };
    returnObj = obj = JSON.stringify(temp);
    var keyHex = CryptoJS.enc.Utf8.parse(key);
    var vi = CryptoJS.enc.Utf8.parse(key);
     var encrypted = CryptoJS.DES.encrypt(obj, keyHex, {
         mode: CryptoJS.mode.ECB,
         padding: CryptoJS.pad.Pkcs7
     });
     var strEncrypted=encrypted.toString();
     var tmp={
         encryptionData:strEncrypted,
         md5:CryptoJS.MD5(strEncrypted+key).toString()
     };
     returnObj=JSON.stringify(tmp);
     return returnObj
}

function jiemi(data) {
    if (isString(data)) {
         // Strip json vulnerability protection prefix and trim whitespace
         var tempData = data.replace(JSON_PROTECTION_PREFIX, '').trim();
         if (tempData) {
             var keyHex = CryptoJS.enc.Utf8.parse(key);
             var decrypted = CryptoJS.DES.decrypt({
                ciphertext: CryptoJS.enc.Base64.parse(tempData)
             }, keyHex, {
                 mode: CryptoJS.mode.ECB,
                 padding: CryptoJS.pad.Pkcs7
             });
             tempData=decrypted.toString(CryptoJS.enc.Utf8);
             tempData = tempData.replace(JSON_PROTECTION_PREFIX, '').trim();
             data = fromJson(tempData);
         }
     }
    return data;
}

//  这个数据是请求回来得数据
// data = "V7akVmOaI/xKfIIOwVyx80vylQraacMvigOwXNNRVxGcIvJNq9rnjfN4sv4+rqQeWCfPGOIcMrqPZDvUiUItiZPIcoe3+LN5MiBQM0Ckr5Ffsf9B8h2LP3wNXywbWp9qWrkVN9vFVjhBu43QsjBC8DoWWlgTMVinuq0ku++ApsHJzOEw8c9KQq0Fn1NnvkmHjAmAkDBQkvxwbeIBhcFpIzRWGB21SQC8hifB/QKZ23hMQG6HPMdPgYuMQn86bQg8fFKimdnpkO0MYnpyMZGgkFpHf3yk/aRrSjVIvM5yDa8=";
// console.log(jiemi(data));

//  账号   密码  验证码
// console.log(get_pwd('18366669999', '123456', '22222'));
"""

def get_yzm():
    # 验证码url
    yzm_url= "https://pspcs.bpic.com.cn/Channel/kaptcha?{}".format(random.randint(20, 88))
    headers = {
        'Accept': 'image/avif,image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Host': 'pspcs.bpic.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://pspcc.bpic.com.cn/',
        'Sec-Fetch-Dest': 'image',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    response = session.get(yzm_url, headers=headers, verify=False)
    with open('yzm.png', 'wb') as p:
        p.write(response.content)
    Image.open('yzm.png').show()


def post_login():
    user_name = '123456'          #  这是是账号
    pwd = '456789'                #  这个是密码
    code = input("请输入验证码:")  # 这里输入验证码 后期可以接入打码平台

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Host': 'pspcs.bpic.com.cn',
        'Origin': 'https://pspcc.bpic.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://pspcc.bpic.com.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    }
    post_url = 'https://pspcs.bpic.com.cn/Channel/channelTask/channelTaskMain.do'
    cat = execjs.compile(js_code)
    data = cat.call('get_pwd', user_name, pwd, code)
    response = session.post(url=post_url, headers=headers, data=data)
    print(response.headers)
    print(response.cookies)
    response = cat.call('jiemi', response.text)
    print(response)

if __name__ == '__main__':
    get_yzm()
    post_login()


