import unittest
import requests
from urllib import parse
import time

class WeatherTest(unittest.TestCase):

    def setUp(self):
        self.url = 'http://v.juhe.cn/weather/index'
        #ip代理，防止被封
        self.proxies = {'https':'https://123.149.136.241:9999'}

    def test_weather_beijing(self):
        '''测试正常的情况--北京天气'''

        data ={
            'cityname':'北京',
            'dtype':'json',
            'format':2,
            'key':'cb0b5216f38bb38ca3f5bd1f4ea0fa67'
            }

        #中文参数要编码，才能传过去
        city = parse.urlencode(data).encode('utf-8')
        r = requests.get(self.url,params=city,proxies=self.proxies)
        result = r.json()

        #断言
        self.assertEqual(result['resultcode'],'200')
        self.assertEqual(result['reason'],'successed!')


    def test_weather_param_error(self):
        '''参数异常'''
        data ={
            'cityname':'安徽',
            'dtype':'json',
            'format':2,
            'key':'cb0b5216f38bb38ca3f5bd1f4ea0fa67'
            }
        r = requests.get(self.url,params=data,proxies=self.proxies)
        result = r.json()

        self.assertEqual(result['reason'],'查询不到该城市的信息')
        time.sleep(1) #防止请求过快被封，ip代理后会好一些

    def test_weather_no_param(self):
        '''无参数'''
        r = requests.get(self.url, proxies=self.proxies)
        result = r.json()

        self.assertEqual(result['resultcode'],'101')
        self.assertEqual(result['reason'],'错误的请求KEY')


if __name__ == '__main__':
    unittest.main()
