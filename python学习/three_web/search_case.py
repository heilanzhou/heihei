import time

from selenium import webdriver

class Mylib():

    def __init__(self):
        #打开浏览器
        self.driver=webdriver.Chrome()

    def delay(self):
        #等待5秒
        self.driver.implicitly_wait(5)

    def open_url(self,url):
        #获取url
        self.driver.get(url)
        #调用delay()函数
        self.delay()
        print(f"访问{url}成功")

    def locate_element(self,locate_type,value):
        #确定返回值
        data_=self.driver.find_element(locate_type,value)
        return data_
    def __del__(self):
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    #给类一个对象
    web=Mylib()
    #类对象调用函数
    web.open_url('https://www.baidu.com')
    el=web.locate_element('id','kw')
    el.send_keys('美女')
    el_sub=web.locate_element('id','su')
    el_sub.click()





