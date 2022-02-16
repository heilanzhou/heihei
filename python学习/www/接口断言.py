import requests
import unittest

class EasyBuyLogin(unittest.TestCase):
    # 易卖网登录接口
    def test01(self):
        url='http://localhost:8080/EasyBuy/Login'
        data = 'loginName=admin&password=123456&action=login'

        headers = {
            'Content-Type': 'application/x-www-from-urlencoded'
        }

        response = requests.post(url,headers=headers,params=data)
        # 获取返回结果
        print(response.json())
        # 获取状态码
        result = response.json()['status']
        print(result)
        # 断言
        self.assertEqual(1,result)
        self.assertIn('登陆成功',response.text)
        self.assertTrue('操作成功',response.text)

if __name__ == '__main__':
    unittest.main()