import time

import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
url = "https://www.baidu.com/"
driver.get(url)
driver.find_element(By.ID,"kw").send_keys("美女")
driver.find_element(By.ID,"su").click()
time.sleep(5)
driver.close()


# url="https://www.baidu.com/s?tn=14075395_2_hao_pg&ie=utf-8&sc=UWYkPj0LPHn4PNtzgv99UdqsuzuY5HDvPjDLrj04rjc3n1mhm1dCmytknWnhmynqnH03n1ckPjT4n6&ssl_sample=normal&srcqid=5995038432877561961&H123Tmp=nunew7&word=%E5%8C%97%E4%BA%AC"

# driver = webdriver.Chrome()
#
# driver.get(url)

# driver.find_element(By.name,"word").sub.keys()


# time.sleep(5)
# driver.close()

# driver.find_element(By.XPATH,"/html/body/div[2]/div/div[3]/div[1]/div[1]/form/div[2]/input").click()
#
# time.sleep(5)
# driver.close()

# driver.find_element(By.CLASS_NAME,"textInput input-hook").click()


# driver.find_element(By.CSS_SELECTOR,"#search > form > div.g-ib.textWrapper.shadow-hook.wrapper-hook > input").click()

# driver.find_element(By.LINK_TEXT,"新闻").click()
# driver.find_element(By.LINK_TEXT,"su").click()



# driver.find_element(By.TAG_NAME,"input").send_keys('off')

# time.sleep(5)
# driver.close()


# 1.获取所有的标签句柄列表
# import driver as driver

# driver.window_handles
# 2.切换到指定标签
# driver.switch_to_window(driver.window_handles[1])
# 3.switch_to(更为推荐的方法)
# driver.switch_to.window(driver.window_handles[n])
# 练习案例
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'http://bj.58.com'
driver.get(url)
# 打印点击之前的窗口句柄列表
# print('点击之前的窗口句柄:',driver.window_handles)
# print('当前的url:',driver.current_url,'当前的标题:',driver.title)

# 定位到房屋出租，点击
el = driver.find_element(By.ID,"keyword").send_keys("房屋出租")
driver.find_element(By.ID,"searchbtn").click()
print('-------------------------------------------------------------')
driver.close()
time.sleep(5)
# 获取到所有的窗口
# handles = driver.window_handles
# print('点击之后的窗口句柄:',handles)
# print('当前的url:',driver.current_url,'当前的标题:',driver.title)
#
# # 切换到新开窗口
# driver.switch_to.window(handles[1])
# print('切换之后的窗口句柄:',handles)
# print('当前的url:',driver.current_url,'当前的标题:',driver.title)
#
# try:
#     # 定位一个再新窗口页面上的元素，如果能够定位到，则表明当前在新窗口上，如果失败则表明现在不在新窗口上
#     el = driver.find_element_by_css_selector('.listUl > li:nth-child(1) > div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)')
#     print (el.text)
#     print('driver在新页面')
# except:
#     print('没有在新页面')
# try:
#     # 定位一个在就窗口上的元素，如果能够定位到，则表明现在在就窗口上
#     el = driver.find_element_by_css_selector('div.col3:nth-child(2) > em:nth-child(1) > a:nth-child(1)')
#     print (el.text)
#     print('driver在旧页面')
# except:
#     print('没有在旧页面')