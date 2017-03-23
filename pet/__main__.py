import sys
from pet.utils import Logger
from pet.src import PETService
from pet.utils.config import PETContext
logger = Logger.getLogger()


def main():
    # help
    argv = sys.argv

    service = PETService()

    if(len(argv) == 1):
        print(PETContext.HELP['wrong'])
    elif(len(argv) == 2):
        cmd = argv[1]
        if(cmd == 'start'):
            service.start()

        elif(cmd == 'stop'):
            service.stop()

        elif(cmd == 'restart'):
            service.restart()

        elif(cmd == 'status'):
            service.status()

        elif(cmd == 'test'):
            service.test()

        elif(cmd == 'help'):
            print(PETContext.HELP['usage'])
        else:
            print(PETContext.HELP['wrong'])

    else:
        print(PETContext.HELP['wrong'])


if __name__ == '__main__':
    main()
