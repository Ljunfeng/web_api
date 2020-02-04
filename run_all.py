import unittest
from BSTestRunner import BSTestRunner
import os
import time

def all_case():
    '''加载指定目录下的所有用例'''
    #指定测试用例路径
    curpath = os.path.dirname(os.path.realpath(__file__))
    casepath = os.path.join(curpath,"test_case")
    pattern= "test*.py"
    discover = unittest.defaultTestLoader.discover(start_dir=casepath,pattern=pattern)

    #定义报告的路径和文件格式
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_path = os.path.join(curpath,"reports",now+"report.html")

    #运行用例并生成测试报告
    with open(report_path,"wb") as fp:
        runner = BSTestRunner(stream=fp,
                             title="Weather Api 测试报告",
                             description="China City Weather Test Report",
                             # verbosity=2,     #显示用例注释
                             )
        runner.run(discover)

if __name__=="__main__":
    all_case()
