import requests
import re
#调试记录
'''
思路

'''
s = requests.session()

#登录网站,第二步操作接第一步
url = "http://127.0.0.1/zentao/user-login.html"   #？后面有参数用params,放在url里就ok了

h = {'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Content-Type': 'application/x-www-form-urlencoded'
}

body  ={'account':'admin',
        'password':'e10adc3949ba59abbe56e057f20f883e',
        'keepLogin[]':'on',
        'referer':'http://127.0.0.1/zentao/my/'
}



r = s.post(url,headers= h,data=body)
print(r.status_code)

url2 = "http://127.0.0.1/zentao/my/"
r2 = s.get(url2) #session不需要传cookies
print(r2.content.decode('utf-8'))
