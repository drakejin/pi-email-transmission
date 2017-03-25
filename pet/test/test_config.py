from unittest import TestCase
from pet.utils.config import PETConfig
import logging

log_print = logging.getLogger('pet').debug


def t_print(string):
    log_print('\n'+string)


class Test_PETConfig(TestCase):
    def test_initialize(self):
        config = PETConfig().config
        config_initialize = True

        if(config['transmission']['host'] is None
           or len(config['transmission']['host'].split(':')) != 3
           ):
            config_initialize = False
            self.assertTrue(config_initialize)
        if(config['transmission']['user'] is None):
            config_initialize = False
            self.assertTrue(config_initialize)
        if(config['transmission']['password'] is None):
            config_initialize = False
            self.assertTrue(config_initialize)
        if(config['log_level'] is None):
            config_initialize = False
            self.assertTrue(config_initialize)
        if(config['check_interval'] is None
           or
           not isinstance(config['check_interval'], (int, ))
           ):
            config_initialize = False
            self.assertTrue(config_initialize)
        if(config['email']['smtp'] is None
           or
           2 != len(config['email']['smtp'].split(':'))
           ):
            config_initialize = False
            self.assertTrue(config_initialize)
        if(config['email']['imap'] is None
           or
           2 != len(config['email']['imap'].split(':'))
           ):
            config_initialize = False
            self.assertTrue(config_initialize)
        if(config['email']['user'] is None):
            config_initialize = False
            self.assertTrue(config_initialize)
        if(config['email']['password'] is None):
            config_initialize = False
            self.assertTrue(config_initialize)
        if(config['email']['folder'] is None):
            config_initialize = False
            self.assertTrue(config_initialize)

        if(id(config) != id(PETConfig().config)):
            config_initialize = False
            self.assertTrue(config_initialize)

        if(config_initialize):
            t_print('\tConfiguration "config.json" Syntax passed')
        else:
            t_print('\tConfiguration "config.json" Syntax failed')
