import requests
from urllib import parse

#ip代理设置，这样就不是自己的ip去访问了,参数为 proxies
#代理网址 https://www.xicidaili.com/nn/

url = 'http://v.juhe.cn/weather/index'

param = {
            'cityname':'北京',
            'dtype':'json',
            'format':2,
            'key':'cb0b5216f38bb38ca3f5bd1f4ea0fa67'
}
city = parse.urlencode(param).encode('utf-8')

proxies = {'https':'https://123.149.136.241:9999'}
r = requests.get(url,params=city,proxies=proxies,timeout=1)
response_data = r.json()


print(response_data['resultcode'])
print(r.content.decode('utf-8'))


