import logging
import logging.handlers
import os

from pet.utils.config import PETConfig


class Logger:
    instance = None

    class __Logger:
        def getLogger(self):
            '''
            Need to set 2 of OS Enviroment value $PROJECT_ENV $PROJECT_HOME
            '''
            config = PETConfig().config
            level = config['log_level']
            home = os.environ['PET_HOME']
            foldername = home+'/logs'
            filename = foldername+'/'+level+'.log'
            if (not os.path.exists(foldername)):
                os.makedirs(foldername)

            fileHandler = logging.handlers.TimedRotatingFileHandler(
                filename,
                when='m',
                backupCount=10
            )

            fomatter = logging.Formatter(
                '[%(levelname)s|%(filename)s:%(lineno)s]'
                + '%(asctime)s > %(message)s'
            )

            fileHandler = logging.FileHandler(filename)
            streamHandler = logging.StreamHandler()

            fileHandler.setFormatter(fomatter)
            streamHandler.setFormatter(fomatter)

            logger = logging.getLogger(config['email']['folder'])

            logger.addHandler(fileHandler)
            logger.addHandler(streamHandler)

            logger.setLevel(level)

            return logger

    def getLogger(self):
        if(Logger.instance):
            Logger.instance
        else:
            Logger.instance = Logger.__Logger().getLogger()
        return Logger.instance
