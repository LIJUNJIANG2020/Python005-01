import requests


# 在同一个 Session 实例发出的所有请求之间保持 cookie 
# s = requests.Session()

# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")

# print(r.text)


'''
{
  "cookies": {
    "sessioncookie": "123456789"
  }
}
'''
################################################3

# 使用上文管理器实现上面的代码
# with requests.Session() as s:
#     r = s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
#     print(r.text)

'''
{
  "cookies": {
    "sessioncookie": "123456789"
  }
}
'''

################################################3

# 登陆豆瓣
import requests
import time
from fake_useragent import UserAgent


login_url = "https://accounts.douban.com/j/mobile/login/basic"
get_url = "https://movie.douban.com/top250"
referer_url = 'https://accounts.douban.com/passport/login?source=movie'
ua = UserAgent(verify_ssl=False)

headers = {
    'User-Agent': ua.random,
    "Referer": referer_url
}

cookies = {
    "ck" : 'v2zK',
    'dbcl2' : "60477041:/ksUvou+w6k",
    '__utmv' : 30149280.6047,
    '__utmt' : '1',
    'douban-fav-remind' : '1',
    'push_noty_num' : 0,
    '_pk_ref.100001.8cb4' : '%5B%22%22%2C%22%22%2C1607161166%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D',
    'apiKey' : 'accounts.douban.com',
    '_pk_ses.100001.2fad' : '*',
    '__utma' : '30149280.699551532.1597632009.1607149022.1607160239.5',
    '__utmz' : '30149280.1607160239.5.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
    '_pk_ref.100001.2fad' : '%5B%22%22%2C%22%22%2C1607160244%2C%22https%3A%2F%2Fmovie.douban.com%2Ftop250%22%5D',
    '_pk_id.100001.8cb4' : 'f705e6c18b7cbc8f.1597979808.3.1607161166.1606366305.',
    'push_doumail_num' : 0,
    '__utmb' : '30149280.2.10.1607160239',
    '_gid' : 'GA1.2.1730567909.1607149004',
    '_pk_id.100001.2fad' : '2c8ee607b737eaf8.1607160244.1.1607161350.1607160244.',
    '__utmc' : '30149280',
    '_ga' : 'GA1.2.699551532.1597632009',
    'll' : "108288",
    '_pk_ses.100001.8cb4' : '*',
    'bid' : 'IrlUaEMTDcs',
    'ap_v' : '0,6.0',
    'gr_user_id' : '01a13ec0-ba60-439d-896c-e19088846c3d',
    'login_start_time' : '1607161353471',
    'last_login_way' : 'account',
    'viewed' : "34613263_30964334_33423512_26836475",
    '_vwo_uuid_v2' : 'D6264577DC367A0423336581643C92224|63ebafa9a5766fd8a8d69045b5683636',

}

form_data = {
    'ck':'',
    'remember': "false",
    'name': 'lijunjiang2012@163.com',
    'password': 'ljj.1105!!',
}

# with requests.Session() as s:
session = requests.Session()
session.headers = headers
requests.utils.add_dict_to_cookiejar(session.cookies, cookies)

res = session.get("https://movie.douban.com/top250")
# print(r.text)

