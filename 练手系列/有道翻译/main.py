import requests,re,json,execjs

def getcode(name):
    ctx = execjs.compile(open('youdao.js', 'r').read())
    decode_name = ctx.call('getcode', name)
    return decode_name

def youdao(name):
    s = requests.session()
    url_1 = 'http://fanyi.youdao.com/'

    url_2 = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    code_list = getcode(name)
    ts = code_list['ts']
    bv = code_list['bv']
    salt = code_list['salt']
    sign = code_list['sign']

    data = {
        'i': name,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': ts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
    }
    headers = {
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    s.get(url=url_1, headers=headers)
    res = s.post(url=url_2, data=data, headers=headers)
    print(res.status_code)
    print(res.text)




if __name__ == '__main__':
    name = """
    Havoc is what best describes the effect of the Coronavirus to the world’s trade, economy and of course the shipping industry. It seems that every single estimate and projection regarding the course of global trade, demand for raw materials and subsequently freight rates must be thrown out of the window and start from scratch again, based on a variery of scenarios.
In its latest weekly report, shipbroker Intermodal said that “as it was expected, the whole world has been focusing on the spread of the Coronavirus, with the fast outbreak being primarily a massive humanitarian concern and unavoidably a concern about the course of the world economic growth. Our European neighbor, Italy, has been taking extremely strict measures in order to deal with the epidemic that went out of control quickly in the country and has already shaped the daily life there with cinematic scenes taking place as people tried to stock both on food and medical supplies in fear of a future shortage of such products”.

According to Intermodal’s SnP Broker, Mr. George Iliopoulos, “financial markets around the world have been also getting a lot of pressure, while the impact on the shipping industry has been substantial so far as well, a development expected given the many ways shipping is interlinked with China and therefore affected by what goes around there. Despite the extended problems in China we have been recently noticing slightly increased activity in shipyards. Indeed, contrary to the previous weeks during which most local yards were closed and many ships could not complete their dry-dockings, slowly but steadily operations have been resuming despite the reduced personnel. Another sign of the gradual return to normality is the improved SnP activity as far as Chinese owners are concerned. After muted buying appetite due to the Chinese New Year and the outbreak of the virus, it seems that even while many of them are still restricted at their homes, Chinese owners have started getting their hands on dry bulk candidates again”.
Source: Intermodal
Intermodal’s broker added that “what is fairly interesting even at this stage is the extent to which the shipping industry as well as global markets in general will recover once the epidemic is contained. We have seen in the past that after the spread of a virus, a strong rebound follows, which was also the case following the containment of the SARS and Zika viruses. Many believe that after the relaxation of the strict measures that coincided with the end of the Chinese New Year, we will see a fast rebound of the market. This would also explain why among others, Greek and Chinese owners are particularly active nowadays. Indeed, during February, which was an extremely bad month for the shipping market due to the above mentioned reasons, we saw more than 45 vessels (Handysize up to Capesize) changing hands”.
Source: Intermodal
“Another notable point that is related to the activity in the second-hand dry bulk market of the past couple of months is that asset values during this environment of exceptionally – in some cases – low freight rates have not declined as much as someone would expect and compared to previous times that the market had gone through similar shocks. This is not to say that we haven’t seen discounts compared to the end of last year but there was certainly no collapse. Surprisingly enough it was Handysize values that seemed to have received the biggest discounts despite the fact that rates for the size showed the most resistance during these very bad months and that during previous market downturns this was the size that saw less pressure in terms of asset prices”, Iliopoulos concluded.
Nikos Roussanoglou, Hellenic Shipping News Worldwide

    """
    youdao(name)