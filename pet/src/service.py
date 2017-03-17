from pet.utils.config import PETConfig
from pet.src.daemon import PETDaemon


class PETService(PETConfig):
    def __init__(self):
        # 'config' is in self.__dict__
        PETConfig.__init__(self)
        self.daemon = PETDaemon('/tmp/pet-daemon.pid')

    def start(self):
        self.daemon.start(self.config)

    def stop(self):
        self.daemon.stop(self.config)

    def status(self):
        self.daemon.status(self.config)

    def test(self):
        self.daemon.test(self.config)

    def help(self):
        print(self.config['docs']['help']['usage'])
