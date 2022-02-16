import time
import unittest

from ddt import ddt, data
from qqyouxiang.qqdenglu import Bod
from qqyouxiang.youxiang import Base


@ddt
class Falk(unittest.TestCase):
    @data('1639314105', 'wq031787', '2592754217@qq.com', 'aiauau', 'c://aa.txt', '1212121')
    def test01(self, seaString):
        Base().search(seaString)

        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
