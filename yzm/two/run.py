# !/usr/bin/python3
# -*-coding:utf-8-*-
# Author: zhou jun wei
# CreatDate: 2020/6/30 11:07

import requests
from PIL import Image
from img import get_gap

#  http://bulletin.cebpubservice.com/     目标网站

url_1 = 'http://47.95.70.97:8950/captcha/captcha/captchaImage'
url_2 = 'http://47.95.70.97:8950/captcha/captcha/checkCaptcha'

s = requests.session()

headers = {
    'Host': '47.95.70.97:8950',
    'Origin': 'http://bulletin.cebpubservice.com',
    'Pragma': 'no-cache',
    'Referer': 'http://bulletin.cebpubservice.com/VerificationCode/login.html?id=88&url=http://bulletin.cebpubservice.com/xxfbcmses/search/bulletin.html?searchDate=1995-06-30&dates=300&categoryId=88&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=&word=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
}
res = s.post(url_1, headers=headers)
jsonData = res.json()
dataToken = jsonData.get('dataToken', '')
sourceImgName = jsonData.get('sourceImgName', '')
bigImgName = jsonData.get('bigImgName', '')
baseImgUrl = 'http://47.95.70.97:8950/captcha/captcha/image/'

with open('./img/sourceImg.jpg', 'wb') as p:
    p.write(s.get(url=baseImgUrl+sourceImgName).content)

with open('./img/bigImg.jpg', 'wb') as p:
    p.write(s.get(url=baseImgUrl+bigImgName).content)

img2 = Image.open(r'./img/bigImg.jpg')
img1 = Image.open(r'./img/sourceImg.jpg')

data = {
    'dataToken': dataToken,
    'point': get_gap(img1, img2)-7
}
res = s.post(url_2, headers=headers, data=data)
token = res.json().get('data')


url_3 = 'http://bulletin.cebpubservice.com/xxfbcmses/search/bulletin.html?searchDate=1995-06-30&dates=300&categoryId=88&industryName=&area=&status=&publishMedia=&sourceInfo=&showStatus=&word=&token={}'.format(token)
headers['Host'] = 'bulletin.cebpubservice.com'
res_3 = requests.get(url_3, headers=headers)
print(res_3.text)




