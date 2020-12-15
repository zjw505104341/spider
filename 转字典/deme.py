import re

headers_str = """

page.currentPage: 2
page.perPageSize: 20
noticeBean.companyName: 
noticeBean.title: 
noticeBean.startDate: 
noticeBean.endDate: 
"""


pattern = '^(.*?): (.*?)$'
for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\': \'\\2\',', line))