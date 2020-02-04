import requests

#cookie 设置

url = 'http://www.baidu.com'
cookie = {'user':'zuw'}
# r = requests.get(url,cookies = cookie)
# print(r.text)


#cookie获取
r = requests.get(url)
print(r.cookies)

for key,value in r.cookies.items():  #cookie转元祖 输出
    print(key+':'+value)

#cookie超时
r = requests.get(url,cookies=cookie,timeout=0.1)
print(r.text)

#文件上传,还是字典的形式
file= {'file':open('1.png','rb')}
r = requests.post(url,files=file)
print(r.text)


#session会话对象。这个以后都要这么做

s = requests.Session()  #先创建一个session然后当前会话cookie都会保存，用于模拟登录后的下一步操作
r = s.get(url)

#证书验证
s = requests.Session()
r = s.get(url,verify=False)
print(r.text)

