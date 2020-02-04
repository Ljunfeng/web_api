import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

#requests 身份认证,注意HTTPBasicAuth('51zxw','8888')里的用户名密码跟url里一样
url='https://www.httpbin.org'
r = requests.get(url+'/basic-auth/51zxw/8888',auth = HTTPBasicAuth('51zxw','8888'))
print(r.content.decode(encoding='gbk'))

r = requests.get(url+'/digest-auth/auth/zxw/6666',auth = HTTPDigestAuth('zxw','6666'))
print(r.text)
