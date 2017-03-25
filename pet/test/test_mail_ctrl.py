from unittest import TestCase
from pet.src.controller import MailController
import logging
'''


'''

log_print = logging.getLogger('pet').debug


def t_print(string):
    log_print('\n'+string)


class Test_MailController(TestCase):
    def test_initialize(self):
        self.controller = MailController()
        init_success = False
        if(self.controller.__dict__.get('IMAPconnection', False)):
            init_success = True
        self.assertTrue(init_success)
        t_print('IMAPconnection initialize : ' + str(init_success))

    def test_check(self):
        self.controller = MailController()
        t_print(str(self.controller.check()))
