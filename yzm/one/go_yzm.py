# -*- coding: utf-8 -*-
import re
from PIL import Image
from go_ocr import go_img

test = """

7     9     4      8
13,13|91,7|140,9|6,57|

破解思路:
   图片大小为 ：  150  *  150
   定位出每个    数字的矩形方框位置
   需要传的参数为  对应数字坐标  第一个参数为  x轴第二个参数为 y轴 

"""

import requests, time, json


s = requests.session()
url_1 = 'https://linzhi.baixing.com/oz/s9verify_html?identity=spider&redirect=https%3A%2F%2Flinzhi.baixing.com%2F&scene=spider'
headers_1 = {
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
}
res_1 = s.get(url_1, headers=headers_1)

temp = re.findall(r"</script><script src='(.*?)'></script>", res_1.text, re.S)
url_2 = 'https:{}'.format(temp[-1])
headers_2 = {
    'referer': 'https://linzhi.baixing.com/oz/s9verify_html?identity=spider&redirect=https%3A%2F%2Flinzhi.baixing.com%2F&scene=spider',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
res_2 = s.get(url_2, headers=headers_2)
temp_2 = re.findall('<i>(.*?)</i>', res_2.text, re.S)

print('需要的数字为', temp_2[-1])

img_url = url_2.replace('.js', '.jpg')
img_res = s.get(img_url, headers=headers_2)
with open('yzm_img/1.jpg', 'wb')as p:
    p.write(img_res.content)

# im = Image.open(r'a.jpg')
# im.show()

# '22,119|24,72|83,71|130,71|'

a = [
    int(temp_2[-1].split('-')[0].strip()),
    int(temp_2[-1].split('-')[1].strip()),
    int(temp_2[-1].split('-')[2].strip()),
    int(temp_2[-1].split('-')[3].strip()),
]

print(a)
num_1 = go_img(a, r'yzm_img/1.jpg')


go_url = url_2.replace('.js', '.valid')+'&data={}&_={}'.format(num_1, int(time.time()*1000))
print(go_url)

go_headers = {
    'referer': 'https://linzhi.baixing.com/oz/s9verify_html?identity=spider&redirect=https%3A%2F%2Flinzhi.baixing.com%2F&scene=spider',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}
res_3 = s.get(go_url, headers=go_headers)
print(res_3.text)
verify_data = json.loads(res_3.text)
ez_verify_sign = verify_data.get('code', '')
if verify_data.get('ret', '') == 0:
    post_url = 'https://linzhi.baixing.com/oz/s9redirect'              #302
    data = {
        'ez_verify_code': num_1,
        'ez_verify_sign': ez_verify_sign,
        'timestamp': str(int(time.time())),
        'identity': 'spider',
        'redirect': 'https://linzhi.baixing.com/',
        'scene': 'spider'
    }
    post_res = s.post(post_url, headers=go_headers, data=data, allow_redirects=False)
    print(post_res)
    print(post_res.headers.get('Location', ''))
    print(post_res.text)








