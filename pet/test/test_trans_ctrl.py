from unittest import TestCase
from pet.src.controller import TransmissionController
import logging

log_print = logging.getLogger('pet').debug


def t_print(string):
    log_print('\n'+string)


class Test_TransmissionController(TestCase):
    def test_initialize(self):
        self.controller = TransmissionController()
        init_success = False
        if self.controller.__dict__.get('_TransmissionController__session_id',
                                        False):
            init_success = True
        self.assertTrue(init_success)

    def test_check(self):
        self.controller = TransmissionController()
        self.controller.check()
