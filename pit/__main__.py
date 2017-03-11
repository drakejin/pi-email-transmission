import sys
from pit.utils.logger import DJLogger
from pit.src.service import PITService

logger = DJLogger.getLogger()


def main():
    # help
    argv = sys.argv
    service = PITService()

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
        print('')
        logger.error("Don't need 2 more ")


if __name__ == '__main__':
    main()
