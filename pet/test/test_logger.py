from unittest import TestCase
from pet.utils import Logger
import logging

log_print = logging.getLogger('pet').debug


def t_print(string):
    log_print('\n'+string)


class Test_Logger(TestCase):
    def test_logger(self):
        logger = Logger().getLogger()
        config_initialize = True

        if(id(logger) != id(Logger().getLogger())):
            config_initialize = False

        self.assertTrue(config_initialize)
