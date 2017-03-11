import os
import json


class PITConfig:

    service = None
    docs = None
    field = None

    def __init__(self):
        if os.environ.get('TRAVIS_SERVICE', None) is None:
            if(PITConfig.service is None):
                with open(os.environ['PROJECT_HOME']+'/conf/service_dev.json') as conf:
                    PITConfig.service = json.load(conf)
        else:
            PITConfig.service = json.loads(os.environ['TRAVIS_SERVICE'])

        if(PITConfig.docs is None):
            with open(os.environ['PROJECT_HOME']+'/conf/docs.json') as conf:
                PITConfig.docs = json.load(conf)

        if(PITConfig.field is None):
            with open(os.environ['PROJECT_HOME']+'/conf/field.json') as conf:
                PITConfig.field = json.load(conf)

        self.__dict__['config'] = {}
        self.__dict__['config']['service'] = PITConfig.service
        self.__dict__['config']['docs'] = PITConfig.docs
        self.__dict__['config']['field'] = PITConfig.field

'''
Hello
'''
