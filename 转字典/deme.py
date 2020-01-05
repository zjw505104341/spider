import re

headers_str = """

Accept: application/json, text/javascript, */*; q=0.01
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: keep-alive
Content-Length: 2700
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Cookie: mgnd_session_id=ADARFAG5K2-2F5CKZWB5WSNK5C0WY192-8UVCN05K-0; mgnd_session_create=1578206425904; mgnd_session_last_access=1578206425904
Host: passport.migu.cn
Origin: https://passport.migu.cn
Pragma: no-cache
Referer: https://passport.migu.cn/login?sourceid=203021&apptype=2&forceAuthn=true&isPassive=false&authType=&display=&nodeId=70027513&relayState=login&weibo=1&callbackURL=http%3A%2F%2Fwww.miguvideo.com%2Fmgs%2Fwebsite%2Fprd%2Findex.html%3FisIframe%3Dweb
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36
X-Requested-With: XMLHttpRequest



"""


pattern = '^(.*?): (.*?)$'
for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\': \'\\2\',', line))