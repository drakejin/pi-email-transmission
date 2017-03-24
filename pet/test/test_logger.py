from unittest import TestCase
from pet.utils import Logger
from pet.__main__ import main

'''


'''


class TestPET(TestCase):
    def test_is_logger(self):
        logger = Logger().getLogger()
        logger.debug('So curious!')
        self.assertTrue(1234, 1234)

    def test_basic(self):
        main()
