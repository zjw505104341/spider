import re

headers_str = """

BAIDUID=F80467EF94F8546E9D9890C64853F654:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1584594991; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1584595016; __yjsv5_shitong=1.0_7_7dab2f724ca9b14ccaf82ed721bb45d6e3e6_300_1584595016644_139.226.186.43_b0c3ad4e; yjs_js_security_passport=a6f5b8ae4beb29996817f09481877276ea26c399_1584595017_js;


"""


pattern = '^(.*?)=(.*?);$'
for line in headers_str.split():
    print(re.sub(pattern, '\'\\1\': \'\\2\',', line))