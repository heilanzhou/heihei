import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):
    #构造方法
    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        #加载百度首页
        self.driver.get('https://www.baidu.com')
        time.sleep(5)
    def test01(self):
        #搜索中国
        self.driver.find_element(By.ID,'kw').send_keys('中国')
        #点击百度一下
        self.driver.find_element(By.ID,'su').click()
        time.sleep(5)
    def test02(self):
        #搜索图片
        self.driver.find_element(By.ID,'kw').send_keys('图片')
        #点击百度一下
        self.driver.find_element(By.ID,'su').click()
        time.sleep(5)
    def testDown(self):
        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
