from pit.utils.config import PITConfig
from pit.src.controller import IMAPController
from pit.src.controller import TransmissionController
import threading
import time


class PITThread(PITConfig):
    config = None

    def __init__(self):
        PITConfig.__init__(self)
        self.interval_thread = PITThread.__IntervalThread()
        PITThread.config = self.config

    def start(self):
        self.interval_thread.start()

    def stop(self):
        self.interval_thread.stop()

    class __IntervalThread(threading.Thread):
        def __init(self):
            threading.Thread.__init__(self)

        def run(self):
            IMAP_ctrl = IMAPController(PITThread.config)
            trnsmsn_ctrl = TransmissionController(PITThread.config)
            while(True):
                # set Interval sleep time
                time.sleep(PITThread.config['service']['check_interval'])

                # imap checker [To transport torrent file to transmission]
                # will return type of list
                torrent_files = IMAP_ctrl.check()
                for torrent in torrent_files:
                    # test code IMAP_ctrl.add_fail(torrent['uid'])

                    torrent_info = trnsmsn_ctrl.add(torrent['payload'])
                    if(torrent_info):
                        IMAP_ctrl.add_success(torrent_info, torrent['uid'])
                        # send seen flag and email what did success
                    else:
                        IMAP_ctrl.add_fail(torrent['uid'])
                        # send seen falg and email what has been occured email

                # transmission checker [To delete completed download]
                # will return type of list
                completed_list = trnsmsn_ctrl.check()
                for completed in completed_list:
                    if(trnsmsn_ctrl.delete(completed)):
                        IMAP_ctrl.delete_success(completed)
                    else:
                        IMAP_ctrl.delete_fail(completed)


'''

'''
