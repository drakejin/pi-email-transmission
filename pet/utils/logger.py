import logging
import logging.handlers
import os

from pet.utils.config import PETConfig
from pet.utils.config import PETContext


class Logger:
    class __Logger:
        def getLogger(purpose=None):
            ''' Need to set 2 of OS Enviro value $PROJECT_ENV $PROJECT_HOME '''
            config = PETConfig().config
            level = purpose and purpose or config['log_level']
            home = config['pet_home']
            foldername = home+'/logs'
            filename = foldername+'/'+level+'.log'
            if (not os.path.exists(foldername)):
                print(foldername)
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

            logger = logging.getLogger('transNoty')

            logger.addHandler(fileHandler)
            logger.addHandler(streamHandler)

            logger.setLevel(level)

            return logger

    instance = None

    def getLogger(purpose=None):
        if(Logger.instance):
            Logger.instance
        else:
            Logger.instance = Logger.__Logger.getLogger(purpose)
        return Logger.instance
