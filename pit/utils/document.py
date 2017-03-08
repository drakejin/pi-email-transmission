import os
import json


class PITDocument:
    docs = None

    def printHelp(self, part):
        '''part parameter only use 'usage','first','contact'   '''
        if(PITDocument.docs is None):
            with open(os.environ['PROJECT_HOME']+'/DOCUMENT.json') as docs:
                PITDocument.docs = json.load(docs)

        print(PITDocument.docs['help'][part])


'''

'''
