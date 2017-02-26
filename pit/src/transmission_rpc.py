import json
import base64
import sys

if sys.version_info < (3,):
    from urllib2 import Request
    from urllib2 import HTTPError
    from urllib2 import urlopen
else:
    from urllib.request import Request
    from urllib.error import HTTPError
    from urllib.request import urlopen as urlopen


class TransmissionRpc:
    def __init__(self, conf):
        self.host = conf["transmission_host"]
        self.user = conf["transmission_user"]
        self.password = conf["transmission_password"]
        self.session_id = False

    def request(self, method, arguments):
        request_done = False
        response = None
        while not request_done:
            try:
                response = self.request_pure(method, arguments)
                request_done = True
            except HTTPError as e:
                if e.code == 409:
                    self.session_id = e.headers['X-Transmission-Session-Id']
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
