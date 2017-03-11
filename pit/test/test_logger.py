from unittest import TestCase
from pit.utils.logger import DJLogger
from pit.__main__ import main

'''
setup 함수를 overide 를 오버라이드를 하면 테스트 케이스를 전부 돌려볼 수 있다.


'''


class TestPIT(TestCase):
    def test_is_logger(self):
        logger = DJLogger.getLogger()
        logger.debug('So curious!')
        self.assertTrue(1234, 1234)

    def test_basic(self):
        main()
