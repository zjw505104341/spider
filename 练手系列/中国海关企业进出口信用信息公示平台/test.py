# coding=utf-8
import requests,json
from pprint import pprint
import base64
from PIL import Image






def img_requests(s,headers):
    img_url = 'http://credit.customs.gov.cn/ccppserver/ccpp/initFirstImage'
    img_res = s.post(url=img_url, headers=headers)
    data = img_res.json()
    img = data['data']['comp']
    width = data['data']['width']
    with open('img_1.jpg', 'wb') as p:
        p.write(base64.b64decode(img.encode('utf-8')))
    X = width/260.0
    img = Image.open("img_1.jpg")
    left = recognize_edge(img)
    left = left/X
    rx = int(left)*X
    print(rx)
    return rx

def index(s,headers, rx):
    url = 'http://credit.customs.gov.cn/ccppserver/ccpp/queryList'
    data = {
        "rx": rx,
        "nameSaic": "酒泉万方线缆有限公司"
    }
    res_ = s.post(url=url, headers=headers, data=json.dumps(data))
    pprint(res_.json())

def recognize_edge(img):
    width, height = img.size
    for x in range(width):
        for y in range(height - 250):  #250是小矩形的长宽
            if is_blue(img.getpixel((x, y))):
                blue = 0
                not_blue = 0
                for z in range(y, y + 100):   #100随便定义一个界限，只要检测到y轴向下一百个像素都是蓝色，那么检测这就是小方块的最左边，此时的x轴就是滑动的终点
                    if is_blue(img.getpixel((x, z))):
                        blue += 1
                    else:
                        not_blue += 1
                if (blue / 100) > 0.85:
                    return x
    return 0

def is_blue(pixel):
    r, g, b = pixel
    return (r + g) < 20 and b > 100

if __name__ == '__main__':
    s = requests.session()
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Host': 'credit.customs.gov.cn',
        'Origin': 'http://credit.customs.gov.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://credit.customs.gov.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    rx = img_requests(s, headers)
    index(s, headers, rx)























"""

http://credit.customs.gov.cn/ccppserver/ccpp/queryDetail


{
"seqNo":"000000000003357648",
"saicSysNo":"630587272",
"queryType":"0",
"curPage":1,
"pageSize":10
}

"""





"""



页面图片大小    宽 260    高  130

countDate: "193184"
comp: "/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQ"
countTotal: "132148031"
height: 770
countUser: "184361"
compMin: "/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQ"
width: 1370
ry: 451

X=data.data.width/260
var Y=data.data.height/130
_this.slideBlock.style.cssText="width:"+250/X+"px;height:"+250/Y+"px;position: absolute;left: 0px;";

250/X = 47.44525547445256
250/Y = 42.2077922077922  
data.data.ry/Y = 76.14285714285714


$("#countTotal").html(data.data.countTotal);
$("#countDate").html(data.data.countDate);
$("#countUser").html(data.data.countUser);

X = width/260        5.269230769230769
rx = left*X          





"""


