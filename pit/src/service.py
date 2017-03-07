from pit.utils.config import PITConfig
from pit.utils.document import PITDocument
from pit.src.thread import PITThread


class PITService(PITConfig):
    def __init__(self):
        # 'config' is in self.__dict__
        PITConfig.__init__(self)
        self.thread = PITThread()

    def start(self):
        self.thread.start()

    def stop(self):
        print('stop')

    def status(self):
        print('status')

    def test(self):
        print('test')

    def help(self):
        PITDocument().printHelp('usage')
