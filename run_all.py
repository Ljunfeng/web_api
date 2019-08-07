import unittest
import os
from common import HTMLTestRunner

# start_dir = r"D:\jiekou_auto\case"

def all_case():
    '''加载指定目录下的所有用例'''
    curpath = os.path.dirname(os.path.realpath(__file__))
    casepath = os.path.join(curpath,"case")
    pattern= "test*.py"
    discover = unittest.defaultTestLoader.discover(start_dir=casepath,pattern=pattern)
    # print(discover)

    report_path = os.path.join(curpath,"report","report.html")
    fp = open(report_path,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="接口测试报告",
                                           description="测试用例详情描述",
                                           # verbosity=2,     #显示用例注释
                                           retry=1)
    runner.run(discover)

if __name__=="__main__":
    all_case()
