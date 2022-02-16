# a="hello world"
# print(a[2:3])
# print(a[3: : 2])
# print(a[3:2:-1])

# b=[1,2,3,4,5,6]
# num =0
# for i in b:
#     num = num+i
# print(num)
#
# print(b[2])

# n=5
# b=[1,2,3,4,5,6]
# for i in b:
#     if i>n:
#         print('我大于5')
#     else:
#         print('我小于5')


# list1=[]
# for i in range(10):
#     if i%2==0:
#         list1.append(i)
#     else:
#         print(i)
# print(list1)

# array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
# print(len(array))
# #i 表示第几轮“冒泡”(对比的轮数是实际的长度-1)
# for i in range(1, len(array)):
#     #j 表示“走访”到的元素索引，每一轮“冒泡”中，j 需要从列表开头“走访”到 len(array) - i 的位置
#         for j in range(0, len(array) - i):
#             #列表中第j个元素大于第j+1个元素
#             if array[j] > array[j + 1]:
#                 #升序
#                 array[j], array[j + 1] = array[j + 1], array[j]
# print(array)


# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.run="跑步"
#     def dog(self):
#         b=(f"这个狗名字是:{self.name}，年龄是：{self.age}，喜欢{self.run}")
#         return b
#
# s=Dog("旺旺",18)
# print(s.name)
# print(s.run)
# print(s.dog())

# import requests
# if __name__ == '__main__':
#     url_="https://blog.csdn.net/u010569893/article/details/97538914"
#     headers_={
#         "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
#     }
#
#     response=requests.get(url_,headers=headers_)
#     str_data=response.content.decode()

#
#
#     with open("字典与json区别.html","w",encoding="utf-8") as f:
#         f.write(str_data)


#
# import requests
# import json
#
#
# url = 'http://localhost:8080/EasyBuy/Login'
# data = 'loginName=admin&password=123456&action=login'
#
# req=requests.post(url=url,params=data)
# print(req.text)
# print(json.dumps(req.json(),indent=4, ensure_ascii=False))
#
#
# import requests
#
# headers = {'Content-Type':'application/json'}
#
# url = 'https://www.baidu.com'   #请求的url
# response = requests.get(url=url,params=None,headers=headers) #http请求头这些信息
# print(response)
# print(response.text)



import requests
import unittest
class EasyBuyLogin(unittest.TestCase):
    #易买网登录接口
    def test01(self):
        url = 'http://localhost:8080/EasyBuy/Login'

        data = 'loginName=admin&password=123456&action=login'

        headers = {
            'Content-Type': 'application/x-www-from-urlencoded'
        }

        response = requests.request('POST', url, headers=headers, params=data)

        #print(response.text.encode('utf8'))
        #print(response.json())
        #获取返回的结果
        print(response.text)
        #获取状态码
        result = response.json()['status']
        print(result)
        #断言
        self.assertEqual(1,result)
        self.assertIn('登陆成功',response.text)
        self.assertTrue('操作成功'in response.text)
if __name__ == '__main__':
    unittest.main()