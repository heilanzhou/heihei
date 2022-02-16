import time
import unittest

from ddt import ddt,data
from three_web.BaiduPage import BaiduPage


@ddt
class BaiduTest(unittest.TestCase):
    # @data('软件测试','硬件测试')
    @data('qq邮箱')
    def test01(self,seaString):
        BaiduPage().search(seaString)
        time.sleep(5)




if __name__ == '__main__':
    unittest.main()