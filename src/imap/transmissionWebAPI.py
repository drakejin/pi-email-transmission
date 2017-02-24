import json
import base64
import os
from urllib.request import Request
from urllib.error import HTTPError
from urllib.request import urlopen as urlopen


from logger import DJLogger

logger = DJLogger.getLogger()


class Connection:
    def __init__(self, config):
        '''
For initialize, It need to '$PROJECT_HOME/config.json'
Becuase It use 'transmission_host','transmission_user'
and 'transmission_password'
        '''
        self.host = "%s/transmission/rpc" % config["transmission_host"]
        self.user = config["transmission_user"]
        self.password = config["transmission_password"]
        self.session_id = None
        self.getSession_id()

    def getSession_id(self):
        auth_string = base64.encodestring(
            ('%s:%s' % (self.user, self.password)).encode()
        ).decode().replace('\n', '')

        logger.debug(auth_string)

        message = {
            "method": "session-get"
        }
        message_json = json.dumps(message).encode("UTF-8")
        request_obj = Request(
            self.host,
            message_json
        )

        request_obj.add_header("Content-Type", "application/json")
        request_obj.add_header("Authorization", "Basic %s" % auth_string)

        if self.session_id:
            request_obj.add_header(
                "X-Transmission-Session-Id",
                self.session_id
            )

        request_done = False
        while not request_done:
            try:
                response = urlopen(request_obj)
                request_done = True
                logger.debug('Success')
            except HTTPError as e:
                logger.debug('Fail')
                if e.code == 409:
                    self.session_id = e.headers['X-Transmission-Session-Id']
                    logger.debug('Set X-Transmission-Session-Id')
                    request_obj.add_header(
                        "X-Transmission-Session-Id",
                        self.session_id
                    )

        logger.debug(response.read().decode('UTF-8'))


        return response

    def request_pure(self, method, arguments):
        auth_string = base64.encodestring(
            ('%s:%s' % (self.user, self.password)).encode())\
            .decode()\
            .replace('\n', '')

        message = {
            "method": method,
            "arguments": arguments
        }
        message_json = json.dumps(message).encode("utf-8")
        request_obj = Request(
            "%s/transmission/rpc" % (self.host, ),
            message_json
        )

        request_obj.add_header("Content-Type", "application/json")
        request_obj.add_header("Authorization", "Basic %s" % auth_string)

        if self.session_id:
            request_obj.add_header(
                "X-Transmission-Session-Id",
                self.session_id
            )

        response = urlopen(request_obj)
        return response


with open(os.environ['PROJECT_HOME']+'/config.json') as configJson:
    logger.debug(configJson)
    configData = json.load(configJson)
    logger.debug(configData)

conn = Connection(configData)
logger.debug(conn)
