import requests

#流式请求，不是一次返回一个结果，而是多个结果

#针对这种接口，可以对结果集的处理使用迭代方法iter_lines()来处理

import json
url='https://www.httpbin.org'
r = requests.get(url+'/stream/10',stream=True) #stream=True  表示接收流式请求

#如果相应内容没有设置编码，则默认设置为utf-8
if r.encoding is None:
    r.encoding='utf-8'

#对响应结果进行迭代处理
for line in r.iter_lines(decode_unicode=True): #decode_unicode=True
    if line:
        data = json.loads(line)  #json转字典
        print(data['id'])


