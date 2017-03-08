import os
import json


class PITConfig:

    config = None

    def __init__(self):
        if(PITConfig.config is None):
            print('읽는중')
            with open(os.environ['PROJECT_HOME']+'/config_dev.json') as conf:
                PITConfig.config = json.load(conf)

        self.__dict__['config'] = PITConfig.config


'''
Hello
'''
