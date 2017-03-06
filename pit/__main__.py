import sys
from pit.utils.logger import DJLogger

logger = DJLogger.getLogger()


def main():
    # help
    argv = sys.argv

    if(len(argv) == 1):
        logger.info('help')
    elif(len(argv) == 2):
        cmd = argv[1]
        if(cmd == 'start'):
            print('start')

        elif(cmd == 'stop'):
            print('stop')

        elif(cmd == 'restart'):
            print('restart')

        elif(cmd == 'status'):
            print('status')

        elif(cmd == 'test'):
            print('test')

        elif(cmd == 'help'):
            print('help')
        else:
            logger.error("Doesn't Exist command")
            print("Doesn't Exist command")

    else:
        logger.error('exception')


if __name__ == '__main__':
    main()
