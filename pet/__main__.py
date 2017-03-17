import sys
from pet.utils import Logger
from pet.src import PETService
from pet.src import PETDaemon

logger = Logger.getLogger()


def main():
    # help
    argv = sys.argv

    service = PETService()

    if(len(argv) == 1):
        print("Please insert any command")
        service.help()
    elif(len(argv) == 2):
        cmd = argv[1]
        if(cmd == 'start'):
            service.start()

        elif(cmd == 'stop'):
            service.stop()

        elif(cmd == 'restart'):
            if(service.stop()):
                service.start()
            else:
                service.stopForce()

        elif(cmd == 'status'):
            service.status()

        elif(cmd == 'test'):
            service.test()

        elif(cmd == 'help'):
            service.help()

        else:
            logger.error("Doesn't Exist command")
            print("Doesn't Exist command")

    else:
        logger.debug("Usage: {}start|stop|restart|status".format(sys.argv[0]))
        logger.error("Don't need 2 more ")


if __name__ == '__main__':
    main()
