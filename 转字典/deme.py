import re

headers_str = """

from: zh
to: en
query: 日本人
transtype: translang
simple_means_flag: 3
sign: 706490.926859
token: e55e1f610ff1f4c5c193358dbff55c20
domain: common


"""


pattern = '^(.*?): (.*?)$'
for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\': \'\\2\',', line))