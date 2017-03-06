import os
import json


class PITConfig:
    def __init__(self):
        pass

    instance = None

    def __new__(self):
        if(PITConfig.instance is None):
            print('읽는중')
            with open(os.environ['PROJECT_HOME']+'/config_dev.json') as conf:
                PITConfig.instance = json.load(conf)

        return PITConfig.instance


'''
Hello
'''
