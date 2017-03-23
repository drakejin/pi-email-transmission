import os
import json


class PETConfig:

    config = None

    def __init__(self):
        if os.environ.get('TRAVIS_SERVICE', None) is None:
            try:
                if(PETConfig.config is None):
                    with open(os.path.dirname(os.path.abspath(__file__))
                              + '/../../../conf/config.json') as conf:
                        PETConfig.config = json.load(conf)
            except Exception as e:
                print(e)
        else:
            PETConfig.config = json.loads(
                os.environ['TRAVIS_SERVICE'].replace("'", "\"")
            )

        self.__dict__['config'] = PETConfig.config


'''
Hello
'''
