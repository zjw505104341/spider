import requests,execjs,json

def get_token(username):
    url = 'http://www.lrts.me/user/login_token.do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    data = {
        'accountName': username
    }
    res = requests.post(url=url, headers=headers, data=data)
    res = json.loads(res.text)
    if res['status'] == 'success':
        token = res['data']
        return token


def login(username, pwd, token):
    url = 'http://www.lrts.me/user/login.do'
    password = execjs.compile(open('lanren.js').read())
    password = password.call('cryptoLogin', pwd, token)
    data = {
        'accountName': username,
        'hashPass': password,
        'autoLogin': '1',
        'validateCode': ''
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    res = requests.post(url=url, headers=headers, data=data)
    print(res.text)

if __name__ == '__main__':

    username = input('请输入账号：')
    pwd = input('请输入密码：')
    token = get_token(username)
    login(username, pwd, token)
