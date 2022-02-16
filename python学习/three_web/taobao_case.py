import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

url="https://www.taobao.com/"
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
#获取左侧种类元素列表
#mylist=driver.find_element(By.CSS_SELECTOR,"body > div.screen-outer.clearfix > div.main > div > div.tbh-service.J_Module > div.service.J_Service > ul > li:nth-child(1)")
#mylist=driver.find_elements_by_xpath('/html/body/div[4]/div[1]/div/div[1]/div[2]/ul/li[2]')
# mylist = driver.find_elements_by_css_selector('li.J_Cat a-all')
mylist= driver.find_elements_by_class_name('J_Cat.a-all')
time.sleep(3)
# mylist = driver.find_element(By.CLASS_NAME,'service-bd')
# print(mylist)

# 创建动作对象
acobj = ActionChains(driver)
time.sleep(1)
for i in mylist:
    acobj.move_to_element(i).perform()
    time.sleep(3)

driver.close()




# url ="http://www.baidu.com"
# driver=webdriver.Chrome()
# driver.get(url)
#
# acobj=ActionChains(driver)
#
# lg_=driver.find_element(By.ID,'')
