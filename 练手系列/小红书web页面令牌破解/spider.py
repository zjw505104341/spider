import requests,execjs,json,re,os

"""
目标

https://www.xiaohongshu.com/explore
 X-Sign   这一个参数效验
 
 
"""

def token_encode(token):
    ctx = execjs.compile(open('xhs_js.js', 'r').read())
    code = ctx.call('decodes', token)
    print(code)
    return code

def get_list():
    token = '/fe_api/burdock/v2/homefeed/notes?pageSize=20&oid=recommend&page=1'
    url = 'https://www.xiaohongshu.com' + token
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Sign': token_encode(token)
    }
    res = requests.get(url=url, headers=headers)
    de_id = res.json()
    id = de_id['data'][0]['id']
    print(id)
    return id


def get_l(id):
    s = requests.session()
    url = 'https://www.xiaohongshu.com/discovery/item/' + str(id)
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    s.get(url, headers=headers)
    res = s.get(url, headers=headers)
    print(res.text)





if __name__ == '__main__':

    #   获取list 页面的id
    id = get_list()

    #  去请求详情页
    get_l(id)

