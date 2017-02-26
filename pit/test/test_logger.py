from unittest import TestCase
from pit.utils.logger import DJLogger
from pit.command_line import main


class TestPIT(TestCase):
    def test_is_logger(self):
        logger = DJLogger.getLogger()
        logger.debug('So curious!')
        self.assertTrue(1234, 1234)

    def test_basic(self):
        main()
