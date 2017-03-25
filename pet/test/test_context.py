from unittest import TestCase
from pet.utils.config import PETContext
import logging

log_print = logging.getLogger('pet').debug


def t_print(string):
    log_print('\n'+string)


class Test_PETContext(TestCase):
    def test_variables(self):
        context_initialize = True

        if(PETContext.TEXT is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.HELP is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.HELP['wrong'] is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.HELP['usage'] is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.EMAIL_FORMATTING is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.EMAIL_FORMAT is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.EMAIL_FORMAT['add_success'] is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.EMAIL_FORMAT['add_fail'] is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.EMAIL_FORMAT['delete_success'] is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.EMAIL_FORMAT['delete_fail'] is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.TRNS_FIELD is None):
            context_initialize = False
            self.assertTrue(context_initialize)
        if(PETContext.TRNS_FIELD['torrent-get'] is None):
            context_initialize = False
            self.assertTrue(context_initialize)

        if(context_initialize):
            t_print('\tPETContext has been passed to use')
        else:
            t_print('\tPETContext has an error or lost variables')
