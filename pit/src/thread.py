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
                    if(trnsmsn_ctrl.add_torrent(torrent)):
                        IMAP_ctrl.send(torrent, 'add_complete')
                        # 메일 읽음 표시를 해준다.
                    else:
                        IMAP_ctrl.send(torrent, 'add_error')
                        # 삭제하도록 메일하나를 보낸다.

                # transmission checker [To delete completed download]
                # will return type of list
                completed_list = trnsmsn_ctrl.check()
                for completed in completed_list:
                    if(trnsmsn_ctrl.delete(completed)):
                        IMAP_ctrl.send(completed, 'delete_complete')
                    else:
                        IMAP_ctrl.send(completed, 'delete_error')


'''

'''
