from pit.utils.config import PITConfig
import threading


class PITThread(PITConfig):
    def __init__(self):
        PITConfig.__init__(self)
        self.sync_thread = PITThread.__SyncThread()
        self.interval_thread = PITThread.__IntervalThread()

    def start(self):
        self.interval_thread.start()
        self.sync_thread.start()

    def stop(self):
        self.interval_thread.stop()
        self.sync_thread.stop()

    class __IntervalThread(threading.Thread):
        def __init(self):
            threading.Thread.__init__(self)

        def run(self):
            i = 5
            while(i):
                print('__IntervalThread ')
                i -= 1

    class __SyncThread(threading.Thread):
        def __init(self):
            threading.Thread.__init__(self)

        def run(self):
            lock = threading.Lock()
            lock.acquire()
            print('__SyncThread')
            lock.release()


'''

'''
