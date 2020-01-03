import re,requests,execjs


def code(data):
    ctx = execjs.compile(open('code.js', 'r').read())
    text = ctx.call('m', data)
    return text

def test():
    url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/project/list?pg=0&pgsz=15&total=0'
    headers = {
        'Referer': 'http://jzsc.mohurd.gov.cn/data/project',
        'timeout': '30000',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    res = requests.get(url=url, headers=headers)
    data = res.text
    l = code(data)
    print(l)

if __name__ == '__main__':
    test()