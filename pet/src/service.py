from pet.utils.config import PETConfig
from pet.utils.config import PETContext
from pet.src.daemon import PETDaemon


class PETService(PETConfig):
    def __init__(self):
        # 'config' is in self.__dict__
        PETConfig.__init__(self)
        self.daemon = PETDaemon('/tmp/pet-daemon.pid')

    def start(self):
        self.daemon.start()

    def stop(self):
        self.daemon.stop()

    def status(self):
        self.daemon.status()

    def test(self):
        self.daemon.nose()
