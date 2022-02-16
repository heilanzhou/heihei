from selenium import  webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com')

    def test1(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("新闻")
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        time.sleep(3)

    def test2(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('旅游')
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        time.sleep(3)


    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
# 方法一：
# if __name__ == '__main__':
#     unittest.main()

# 方法二：
#创建一个测试套件，并向其中加载测试用例
# suit=unittest.TestLoader().loadTestsFromTestCase(Test)
#显式运行测试没并且通过设置verbosity设定对每一个测试方法产生测试结果；run中传入要执行的测试套件
# unittest.TextTestRunner(verbosity=2).run(suit)

#方法三：
testunit=unittest.TestSuite()
testunit.addTest(Test('test1'))
testunit.addTest(Test('test2'))
unittest.TextTestRunner().run(testunit)


