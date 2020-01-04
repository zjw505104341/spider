import re,requests,execjs,json

"""

目标网站   http://j.esf.leju.com/ucenter/login?curcity=sh

"""

class login():

    def __init__(self, pwd) -> None:
        self.s = requests.session()
        self.ctx = execjs.compile(open('test.js', 'r').read())
        self.e_pwd = self.ctx.call('get_pwd', pwd)
        self.g_url = self.ctx.call('s_url')
        self.url_1 = f'http://j.esf.leju.com/ucenter/qrlogin/?_={self.g_url}'
        self.url_2 = 'http://j.esf.leju.com/ucenter/login?curcity=sh'
        self.url_3 = 'http://j.esf.leju.com/ucenter/login?curcity=sh'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }


    def index_1(self):
        res = self.s.get(url=self.url_1, headers=self.headers)
        print(res.headers)

    def index_2(self):
        res = self.s.get(url=self.url_2, headers=self.headers)
        html = res.text
        ckey = ''.join(re.findall('name="ckey" value="(.*?)" />', html, re.S|re.M))
        return ckey


    def index_3(self,ckey):
        data = {
            'password': self.e_pwd,
            'username': '18366669999',
            'ckey': ckey,
            'imgcode': ''
        }

        res = self.s.post(url=self.url_3, data=data, headers=self.headers)
        html = res.text
        print(html)
        json_html = json.loads(html)
        l = json_html['msg']
        print(l)


if __name__ == '__main__':
    log_obj = login('123456')
    log_obj.index_1()
    ckey = log_obj.index_2()
    log_obj.index_3(ckey)





