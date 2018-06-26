#encoding=utf-8
import sys
import time
import random
import string
# import httplib
# import urllib
import socket
import urllib.request
import urllib.parse
from random import randint
# 生成指定位数的随机字符串，字符为字母或数字
def getRandomString(id_length):
    charSeq = string.ascii_letters + string.digits
    randString = 'oZBXij'
    for i in range(id_length):
        randString += random.choice(charSeq)
    return randString
# randon number 10-99
def random_sleep_time(digits_length):
    digits_char = string.digits
    need_sleep_time = ''
    for i in range(digits_length):
        need_sleep_time += random.choice(digits_char)
    return int(need_sleep_time)

userAgentList = [
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15F79 MicroMessenger/6.6.7 NetType/WIFI Language/en',
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E302 MicroMessenger/6.7.0 NetType/WIFI Language/zh_CN',
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/13B53 MicroMessenger/6.6.4 NetType/WIFI Language/zh_CN',
'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15G108 MicroMessenger/6.6.7 NetType/WIFI Language/zh_CN',
'Mozilla/5.0 (Linux; Android 6.0.1; SM-G930V Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 MicroMessenger/6.6.31.921 NetType/WIFI Language/zh_CN',
'Mozilla/5.0 (Linux; Android 5.0.2; HTC 8088; Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) MicroMessenger/4.5.255Chrome/37.0.2049.0 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.4.4; HM NOTE 1LTEW Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.6.0.54_r849063.501 NetType/WIFI',
'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Mobile/14E304 MicroMessenger/6.6.5 NetType/4G Language/zh_CN',
'mozilla/5.0 (linux; u; android 4.1.2; zh-cn; mi-one plus build/jzo54k) applewebkit/534.30 (khtml, like gecko) version/4.0 mobile safari/534.30 MicroMessenger/6.6.7',
'mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 MicroMessenger/6.0',
'Mozilla/5.0 (Linux; Android 4.4.2; GT-N7100 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 MicroMessenger/6.6.3 NetType/cmnet',
'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; HTC D820mu Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.7 NetType/WIFI',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; SM-N9008V Build/KOT49H) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.6 NetType/cmnet',
'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_2 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11A501 MicroMessenger/6.1.1 NetType/3G',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HM NOTE 1LTETD Build/KVT49L) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.5 NetType/cmnet',
'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-cn; N918St Build/KTU84P) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.7.0 NetType/3gnet',
'Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; HM 1SC Build/JLS36C) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.7 NetType/#777',
'Mozilla/5.0 (Linux; U; Android 4.2.2; zh-cn; vivo Y22 Build/JDQ39) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.7.0.62_r1062275.542 NetType/WIFI',
'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-I9128V Build/JZO54K) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025410 Mobile Safari/533.1 MicroMessenger/6.6.0.65_r1022275.542 NetType/WIFI',
'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT2-L01 Build/HuaweiMT2-L01) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.7 Mobile Safari/533.1 MicroMessenger/6.5.2.56_r958800.520 NetType/cmnet'
]

# start here to post request
voteCount = 0;
while True:
    wechatOpenId = getRandomString(24);
    #wechatOpenId = 'oZBX3qpqgmIDaBOUh7hD2oGOF8cT';
    contentid = '46102'
    wechat_data = {'contentid': contentid, 'sectionid': '2563','openid':wechatOpenId}
    data = urllib.parse.urlencode(wechat_data).encode(encoding='utf-8')
    #postParams = urllib.urlencode(wechat_data)
    print(wechatOpenId)

    url = 'http://api.sdetv.com.cn/front/content/teacher/dianzan'
    headers = {'Accept': '*/*', \
               'Accept-Encoding': 'gzip, deflate', \
               'Accept-Language': 'zh-CN', \
               'Content-Length': '66', \
               'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', \
               'Host': 'api.sdetv.com.cn', \
               'Origin': 'http://www.sdetv.com.cn', \
               'Proxy-Connection': 'keep-alive', \
               'Referer': 'http://www.sdetv.com.cn/zuimeijiaoshi2018/detail.html?contentid='+contentid, \
               'User-Agent': userAgentList[randint(0, 19)], \
                }

    # conn = httplib.HTTPConnection("api.sdetv.com.cn/front/content/teacher/dianzan")
    # conn.request("POST", "/front/content/teacher/dianzan", postParams, headers)
    # response = conn.getresponse()
    # data = response.read()
    # print (response.status, response.reason, data)
    # conn.close()
    # v2
    # ###############
    # v3
    try:
        request = urllib.request.Request(url=url, data=data, headers=headers)
        response = urllib.request.urlopen(request)
        json = response.read().decode()
        voteCount += 1
        print(json)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # next_people_time = random_sleep_time(2)
        next_people_time = randint(2, 10)
        print('Vote Count: ' + str(voteCount))
        print('Wait', next_people_time, 's next vote\n')
        time.sleep(next_people_time)
    except socket.error:
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print('Failed')
        continue
# try:
#     response = urllib.request.urlopen(request)
#     data = response.read().decode('utf-8')
#     print('data: ' + data)
#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#     next_people_time = random_sleep_time(2)*60
#     print('Wait', next_people_time, 'next vote\n')
#     time.sleep(next_people_time)
# except socket.error:
#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
#     print('timeout')

