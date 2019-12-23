import execjs,re,requests,json,time

def get_index():
    pass

def login():
    pwd_password = execjs.compile(open('weike.js', 'r').read()).call("hex_md5", '123456789')
    data = {
        'formhash': '859656',
        'txt_account': '13764891295',
        'pwd_password': pwd_password,
        'login_type': '3',
        'ckb_cookie': '0',
        'hdn_refer': 'https://www.epwk.com/',
        # 'txt_code': 'pvz7',
        'pre': 'login',
        'inajax': '1'
    }
    url = 'https://www.epwk.com/index.php?do=login'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
    }
    l = requests.post(url=url,data=data, headers=headers)
    print(l.text)

login()
# print(u'\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef')