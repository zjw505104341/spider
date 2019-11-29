import requests,re,json,execjs

def getcode(name):
    ctx = execjs.compile(open('youdao.js', 'r').read())
    decode_name = ctx.call('getcode', name)
    return decode_name

def youdao(name):
    s = requests.session()
    url_1 = 'http://fanyi.youdao.com/'

    url_2 = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    code_list = getcode(name)
    ts = code_list['ts']
    bv = code_list['bv']
    salt = code_list['salt']
    sign = code_list['sign']

    data = {
        'i': name,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
    }
    headers = {
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    s.get(url=url_1, headers=headers)
    res = s.post(url=url_2, data=data, headers=headers)
    print(res.status_code)
    print(res.text)




if __name__ == '__main__':
    name = '中国'
    youdao(name)