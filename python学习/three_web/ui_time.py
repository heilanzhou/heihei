# import os
# import time
#
# while 1 :
#     now_time = time.strftime("%H:%M")
#     if now_time == '17:03' or now_time == '17:21':
#         os.chdir("C:\\Users\\EDZ\\Desktop\\python学习\\qqq")
#         os.system('python fasong.py')
#         print (u'运行完成退出!')
#         break
#     else:
#         time.sleep(3)
#         print(now_time)



from selenium import webdriver
import time
import xlrd

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
#读取文件
data = xlrd.open_workbook("C:\\Users\\EDZ\\Desktop\\qq.xls")
#读取第一个工作表
table = data.sheet_by_name('Sheet1')
#使用for循环输出所有数据
list=[]
for i in range (0,table.nrows):
    # 读取excel第一行
    list = table.row_values(i)
    break
print(list)
time.sleep(3)
#通过索引在excel表中获取百度URL
driver.get(list[0])
time.sleep(3)
#通过索引在excel表中获取百度输入框元素并输入要搜索的字段
driver.find_element_by_id(list[3]).send_keys(list[4])
time.sleep(3)
#通过索引在excel表中获取百度点击“百度一下”元素并点击
driver.find_element_by_id(list[7]).click()
time.sleep(3)
list=[]
for i in range (1,table.nrows):
    # 读取excel第二行
    list = table.row_values(i)
    break
print(list)
#跳转到“百度首页”
driver.find_element_by_css_selector(list[0]).click()
time.sleep(3)
driver.close()