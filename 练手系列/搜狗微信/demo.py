"""

练习关键点        多次请求     js用python从写

搜狗微信破解
点击的时候     a标签跳转

关键js   贴出来

<script>
    (function() {
        $("a").on("mousedown click contextmenu", function() {
            var b = Math.floor(100 * Math.random()) + 1
              , a = this.href.indexOf("url=")
              , c = this.href.indexOf("&k=");
            -1 !== a && -1 === c && (a = this.href.substr(a + 4 + parseInt("21") + b, 1),
            this.href += "&k=" + b + "&h=" + a)
        })
    }
    )();
</script>



"""
import time,re,random,uuid
from urllib.parse import quote
import requests
from lxml import etree
import user_agent




def get_article_url(s, base_article_url, headers):
    """
    获取文章链接
    :param base_article_url:
    :param headers:
    :return:
    """
    a = base_article_url.find("url=")
    b = int(random.random() * 100) + 1
    result_link = base_article_url + "&k=" + \
        str(b) + "&h=" + base_article_url[a + 4 + 21 + b: a + 4 + 21 + b + 1]

    #   处理过后 拼接
    article_url_temp = "https://weixin.sogou.com" + result_link

    #   去请求获取真正的文章url   去进行拼接
    second_url = s.get(article_url_temp, headers=headers).text
    url_text = re.findall(r"\'(\S+?)\';", second_url, re.S)
    article_url = ''.join(url_text)
    return article_url


def get_parse(url, headers):

    s = requests.session()
    headers['Referer'] = url

    #   第一次请求获取  setcookie
    s.get(url, headers=headers)
    #   第二次请求携带setcookie 请求页面
    res = s.get(url=url, headers=headers)
    html = etree.HTML(res.text)
    article_list = html.xpath('//*[@id="main"]/div[@class="news-box"]/ul/li')
    for article in article_list:

        #  获取到假的url
        base_article_url = article.xpath(
            './div[@class="txt-box"]/h3/a/@href')[0]

        #   将假的url 传入  get_article_url  进行处理  获取真正的文章url
        article_url = get_article_url(s, base_article_url, headers)

        print('真正的文章url', article_url)


def main():
    keyword = "python"

    #   爬取10页关于python的文章

    base_url = "https://weixin.sogou.com/weixin?type=2&query={query}&page={page}"
    for i in range(1, 11):
        headers = {
            'Host': "weixin.sogou.com",
            'Referer': "https://weixin.sogou.com/weixin",
            'User-Agent': user_agent.generate_user_agent(),
        }
        url = base_url.format(query=quote(keyword), page=i)

        #  生成url   和   headers  传入  get_parse  方法  进行爬取
        get_parse(url, headers)

        time.sleep(3)


if __name__ == '__main__':
    main()