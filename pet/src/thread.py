from pet.utils.config import PETConfig
from pet.src.controller import MailController
from pet.src.controller import TransmissionController
import threading
import time


class PETThread(PETConfig):
    config = None

    def __init__(self):
        PETConfig.__init__(self)
        self.interval_thread = PETThread.__IntervalThread()
        PETThread.config = self.config

    def start(self):
        self.interval_thread.start()

    def stop(self):
        self.interval_thread.stop()

    class __IntervalThread(threading.Thread):
        def __init(self):
            threading.Thread.__init__(self)

        def run(self):
            mail_ctrl = MailController(PETThread.config)
            trnsmsn_ctrl = TransmissionController(PETThread.config)
            while(True):
                # set Interval sleep time
                time.sleep(PETThread.config['service']['check_interval'])
                print('------------Yeah----------------')
                # imap checker [To t`ransport torrent file to transmission]
                # will return type of list
                torrent_files = mail_ctrl.check()
                for torrent in torrent_files:
                    # test code IMAP_ctrl.add_fail(torrent['uid'])
                    print ('Yeap? ')
                    torrent_info = trnsmsn_ctrl.add(torrent['payload'])
                    if(torrent_info):
                        mail_ctrl.add_success(torrent_info, torrent['uid'])
                        # send seen flag and email what did success
                    else:
                        mail_ctrl.add_fail(torrent['uid'])
                        # send seen falg and email what has been occured email

                # transmission checker [To delete completed download]
                # will return type of list
                completed_list = trnsmsn_ctrl.check()
                for completed in completed_list:
                    if(trnsmsn_ctrl.delete(completed)):
                        mail_ctrl.delete_success(completed)
                    else:
                        mail_ctrl.delete_fail(completed)


'''

'''
