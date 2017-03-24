from pet.utils.config import PETConfig
from pet.utils.config import PETContext
from pet.utils import Logger
from pet.src.controller import MailController
from pet.src.controller import TransmissionController
import threading
import time

logger = Logger().getLogger()


class PETThread(threading.Thread):
    config = None

    def __init__(self):
        threading.Thread.__init__(self)
        self.mail_ctrl = MailController()
        self.trnsmsn_ctrl = TransmissionController()

    def run(self):
        while(True):
            try:
                time.sleep(PETConfig().config['check_interval'])
                torrent_files = self.mail_ctrl.check()
                for torrent in torrent_files:
                    torrent_info = self.trnsmsn_ctrl.add(torrent['payload'])
                    if(torrent_info):
                        self.mail_ctrl.add_success(torrent_info, torrent['uid'])
                    else:
                        self.mail_ctrl.add_fail(torrent['uid'])

                    logger.info('Email Torrents:\n\n' + str(torrent))

                completed_list = self.trnsmsn_ctrl.check()
                for completed in completed_list:
                    if(self.trnsmsn_ctrl.delete(completed)):
                        self.mail_ctrl.delete_success(completed)
                    else:
                        self.mail_ctrl.delete_fail(completed)
                    logger.info('Transmission Complete \n\n' + str(completed))
            except Exception as e:
                logger.warn(e)
                logger.warn(str(e))
                logger.warn(str(e.__dict__))


'''

'''
