import time
import unittest

from ddt import ddt, data
from qqyouxiang.youxiang import Base


@ddt
class Fsg(unittest.TestCase):
    @data('qq邮箱')
    def test01(self, seater):
        Base().search(seater)
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
