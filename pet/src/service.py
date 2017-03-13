from pet.utils.config import PETConfig
from pet.src.thread import PETThread


class PETService(PETConfig):
    def __init__(self):
        # 'config' is in self.__dict__
        PETConfig.__init__(self)
        self.thread = PETThread()

    def start(self):
        self.thread.start()

    def stop(self):
        print('stop')

    def status(self):
        print('status')

    def test(self):
        print('test')

    def help(self):
        print(self.config['docs']['help']['usage'])
