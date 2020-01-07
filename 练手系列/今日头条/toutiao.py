import re,requests,json,execjs,time


class toutiao:

    def __init__(self) -> None:
        self.url_1 = 'https://www.toutiao.com/ch/news_game/'
        self.url_2 = 'https://www.toutiao.com/api/pc/feed/?'
        self.ctx = execjs.compile(open('toutiao.js','r', encoding='utf-8').read())
        self.headers = {
            'referer': 'https://www.toutiao.com/ch/news_game/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        self.s = requests.session()


    def index_1(self):
        self.s.get(self.url_1, headers=self.headers)

    def index_2(self,time_s, as_cp, sign):
        params = {
            'category': 'news_game',
            'utm_source': 'toutiao',
            'widen': '1',
            'max_behot_time': str(time_s),
            'max_behot_time_tmp': str(time_s),
            'tadrequire': 'true',
            'as': as_cp['as'],
            'cp': as_cp['cp'],
            '_signature': sign
        }
        res = self.s.get(url=self.url_2,params=params, headers=self.headers)
        html = res.text
        print(html)
        json_html = json.loads(html)
        data_list = json_html['data']
        for i in data_list:
            title = i['title']
            print(title)

        #   下一页时间搓
        next_time = json_html['next']['max_behot_time']
        print(next_time)
        return next_time


    def get_sign(self, time_s):
        as_cp = self.ctx.call('as_cp')
        _signature = self.ctx.call('get_sign', time_s)

        # 1578374849
        # print(_signature)
        # print(as_cp['as'])
        # print(as_cp['cp'])

        return as_cp, _signature




if __name__ == '__main__':
    obj_ = toutiao()

    time_s = int(time.time())
    as_cp, sign = obj_.get_sign(time_s)
    obj_.index_1()

    next_time = obj_.index_2(time_s, as_cp, sign)
    as_cp, sign = obj_.get_sign(next_time)
    obj_.index_2(time_s, as_cp, sign)





