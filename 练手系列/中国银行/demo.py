import requests,re,execjs

#   目标网站    http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/index.html
#   加密方式    sojson.v5


def get_href(s, headers):
    url_1 = 'http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/index.html'
    response = s.get(url_1, headers=headers)
    js = re.findall('<script type="text/javascript">(.*?)</script>',response.content.decode(),re.S|re.M)[0]
    ll = re.sub("window\[_0x56ae\('0x3c','\)9A&'\)\]=_0x35ace3;", "return _0x35ace3;", js)
    ctx = execjs.compile(ll)
    href = ctx.call('_0x33f22a')
    print(href)

    return href


    # Cookie = response.headers['Set-Cookie'].split(';')[0]
    # cookies = requests.utils.dict_from_cookiejar(response.cookies)
    # headers['Cookie'] = Cookie

def get_html(s, headers, href):

    url_2 = 'http://www.pbc.gov.cn' + str(href)
    print(url_2)
    response_2 = s.get(url_2, headers=headers)
    print(response_2.content.decode())


if __name__ == '__main__':
    s = requests.session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
    }

    href = get_href(s, headers)
    get_html(s, headers, href)

