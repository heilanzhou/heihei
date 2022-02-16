import requests
import unittest
import HTMLTestRunnerCN


class interfacetest01(unittest.TestCase):
    #实时天气查询接口
    def test01(self):
        url = 'https://tianqiapi.com/api'
        data = 'version=v6&appid=73691227&appsecret=123456'
        response = requests.request('GET',url,params=data)
        print(response.json())

#文件路径
Testcase_dir = 'C:\\Users\\EDZ\\Desktop\\python学习\\www'
# #覆盖该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'bb.py')
filename = 'C:\\Users\\EDZ\\Desktop\\python学习\\www\\bb.html'
fp = open(filename, 'wb')
runner = HTMLTestRunnerCN.HTMLTestRunner(
stream=fp,
title='接口测试报告',
description='用例执行情况：')
# runner.run(testunit)
runner.run(dis)
fp.close()