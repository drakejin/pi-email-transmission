import os
import json


class PETConfig:

    service = None
    docs = None
    field = None

    def __init__(self):
        if os.environ.get('TRAVIS_SERVICE', None) is None:
            if(PETConfig.service is None):
                with open(os.environ['PROJECT_HOME']+'/conf/service_dev.json') as conf:
                    PETConfig.service = json.load(conf)
        else:
            print(os.environ['TRAVIS_SERVICE'])
            PETConfig.service = json.loads(os.environ['TRAVIS_SERVICE'].replace("'", "\""))
            print(PETConfig.service)

        if(PETConfig.docs is None):
            with open(os.environ['PROJECT_HOME']+'/conf/docs.json') as conf:
                PETConfig.docs = json.load(conf)

        if(PETConfig.field is None):
            with open(os.environ['PROJECT_HOME']+'/conf/field.json') as conf:
                PETConfig.field = json.load(conf)

        self.__dict__['config'] = {}
        self.__dict__['config']['service'] = PETConfig.service
        self.__dict__['config']['docs'] = PETConfig.docs
        self.__dict__['config']['field'] = PETConfig.field


'''
Hello
'''
