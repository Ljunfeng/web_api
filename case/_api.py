import requests
import re
#调试记录
s = requests.session()

#登录网站,第二步操作接第一步
url = "http://127.0.0.1/zentao/user-login.html"   #？后面有参数用params,放在url里就ok了

# par={'a':'s',
#      'b':'e'}
h = {'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Content-Type': 'application/x-www-form-urlencoded'
}

body  ={'account':'admin',
        'password':'e10adc3949ba59abbe56e057f20f883e',
        'keepLogin[]':'on',
        'referer':'http://127.0.0.1/zentao/my/'
}

#一般cookies是放在返回的头部
# c ={"name1":"values1",
#     "name2":"values2"
#     }


r = s.post(url,headers= h,data=body)  #body是jason格式传json=body,其他data=body .一般是data，json会声明。cookie建议单独传。cookies= h
# r = requests.post(url,cookies= c,data=body)
print(r.status_code)
# print(r.text)
res = r.content.decode('utf-8')

try:
    result = re.findall("alert\(\'(.+?)\'\)",res)
    print(result[0])
except:
    print('登录ok')