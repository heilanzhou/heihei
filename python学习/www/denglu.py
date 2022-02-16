import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Test:

    def __init__(self):

        global driver

        # 打开百度

        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.get("https://www.baidu.com")
        # 打开网页
        self.handles = driver.window_handles
        self.driver.implicitly_wait(5)
        time.sleep(10)

    # 定位元素
    def find_ele(self, *args):
        ele = self.driver.find_element(*args)
        return ele

    # #获取所有窗口并切换窗口
    def find_handles(self):
        self.driver.switch_to.window(self.handles[1])

    # 定位登录表单关键字
    def switch_frame(self):
        self.driver.switch_to.frame(self.find_ele(By.XPATH, '//*[@id="login_frame"]'))

    # 定位收件人表单关键字
    def frame_wen(self):
        self.driver.switch_to.frame(self.find_ele(By.XPATH, '//*[@id="mainFrame"]'))

    # 返回上一级
    def get_parent(self):
        self.driver.switch_to.parent_frame()

    # 定位正文表单关键字
    def get_wen(self):
        self.driver.switch_to.frame(self.find_ele(By.CLASS_NAME, 'qmEditorIfrmEditArea'))


