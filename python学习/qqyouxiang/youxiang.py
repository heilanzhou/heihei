import time

from selenium.webdriver.common.by import By

from www.denglu import Test


class Base(Test):
    """"打开qq邮箱页面"""
    # 页面元素
    baidu_text_loc = (By.ID, 'kw')
    baidu_submit_loc = (By.ID, 'su')
    baidu_ret_loc = (By.XPATH, '//*[@id="1"]/h3/a[1]')
    time.sleep(3)

    # 页面元素动作
    def get_text_obj(self):
        el = self.find_ele(*Base.baidu_text_loc)
        return el

    def get_submit_obj(self):
        el = self.find_ele(*Base.baidu_submit_loc)
        return el

    def get_em_obj(self):
        el = self.find_ele(*Base.baidu_ret_loc)
        return el

    def search(self, loc):
        self.get_text_obj().send_keys(loc)
        self.get_submit_obj().click()
        self.get_em_obj().click()
        time.sleep(5)
