import unittest
from BSTestRunner import BSTestRunner
from BeautifulReport import BeautifulReport  #新的可视化报告模板
import os
import time

def BSTestRunner_all_case():
    '''报告模板一'''
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

def BeautifulReport_all_case():
    '''报告模板二'''
    curpath = os.path.dirname(os.path.realpath(__file__))
    casepath = os.path.join(curpath,"test_case")
    pattern= "test*.py"

    #定义报告的路径和文件格式
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_path = os.path.join(curpath,"reports")

    suite_tests = unittest.defaultTestLoader.discover(casepath,pattern=pattern,top_level_dir=None)
    BeautifulReport(suite_tests).report(filename=now+'_baidu_test', description='阿里云听', log_path=report_path)



if __name__=="__main__":
    # BSTestRunner_all_case()
    BeautifulReport_all_case()
