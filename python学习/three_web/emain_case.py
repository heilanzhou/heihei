import time


from selenium import webdriver
from selenium.webdriver.common.by import By

url ="https://www.baidu.com"
# 调用url
driver=webdriver.Chrome()
driver.get(url)
# 打开网页
time.sleep(3)
driver.find_element(By.ID,"kw").send_keys("qq邮箱")
time.sleep(3)
driver.find_element(By.ID,"su").click()
# 延时
time.sleep(3)
# 打开邮箱网页
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
time.sleep(3)
# # 登录邮
handles = driver.window_handles
driver.switch_to.window(handles[1])
# #
# # 直接通过id进入
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="login_frame"]'))
# # 先定位到元素再进入
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
time .sleep(3)
# # 定位并输入账号
driver.find_element_by_xpath('//*[@id="u"]').send_keys('1639314105')
time.sleep(3)
# # 定位并输入密码
driver.find_element_by_xpath('//*[@id="p"]').send_keys('wq031787')
time.sleep(3)
# # 定位并点击登录
driver.find_element_by_id('login_button').click()
time.sleep(5)
# 写信
driver.find_element_by_id('composebtn').click()
time.sleep(3)
# 定整个表单
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="mainFrame"]'))
time.sleep(3)
# 收件人
driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('2592754217@qq.com')
time.sleep(3)
# 主题
driver.find_element_by_xpath('//*[@id="subject"]').send_keys('aiauau')
time.sleep(3)
# 附加内容
driver.find_element_by_name('UploadFile').send_keys('c://aa.txt')
time.sleep(3)
# 定正文表单
driver.switch_to.frame(driver.find_element_by_class_name('qmEditorIfrmEditArea'))
time.sleep(3)
# 正文
driver.find_element_by_xpath('/html/body').send_keys('1212121')
time.sleep(3)
# 退出正文框
driver.switch_to.parent_frame()
time.sleep(3)
# 发送
driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
time.sleep(3)