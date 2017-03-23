import sys
import base64
import json

from pet.utils import Logger
from pet.utils.config import PETConfig
from pet.utils.config import PETContext
if sys.version_info < (3,):
    from urllib2 import Request
    from urllib2 import HTTPError
    from urllib2 import URLError
    from urllib2 import urlopen
else:
    from urllib.request import Request
    from urllib.error import HTTPError
    from urllib.error import URLError
    from urllib.request import urlopen as urlopen

logger = Logger.getLogger()


class TransmissionController(PETConfig):
    def __init__(self):
        PETConfig.__init__(self)
        self.__session_id = None
        self.__auth = base64.encodestring(
            (
                '%s:%s' %
                (
                    self.config['transmission']['user'],
                    self.config['transmission']['password']
                )
            ).encode()
        ).decode().replace('\n', '')
        self.__get_session__()

    def __request__(self, method, arguments=None):
        message = {"method": method, "arguments": arguments}
        message = json.dumps(message).encode("utf-8")

        req = Request(
            "%s/transmission/rpc"
            % (self.config['transmission']['host']),
            message
        )

        req.add_header("Content-Type", "application/json")
        req.add_header("Authorization", "Basic %s" % self.__auth)

        res = None
        for i in range(3):
            try:
                if self.__session_id:
                    req.add_header(
                        "X-Transmission-Session-Id",
                        self.__session_id
                    )
                res = urlopen(req)
                if res:
                    break
            except HTTPError as e:
                if e.code == 409:
                    self.__session_id = e.headers['X-Transmission-Session-Id']
            except URLError as e:
                logger.debug('Please check Transmission Web Controller turn on!')
                sys.exit('Please check Transmission Web Controller turn on!')

        res = json.loads(res.read().decode('utf-8'))
        return res

    def __get_session__(self):
        self.__request__('session-get')

    def __torrent_info__(self, torrent_id):
        method = 'torrent-get'
        field = PETContext.TRNS_FIELD[method]
        field['ids'] = [torrent_id, ]
        print('203 : ', field)
        return self.__request__(method, field)['arguments']['torrents'][0]

    def check(self):
        complete_torrent = []
        method = 'torrent-get'
        res = self.__request__(method, PETContext.TRNS_FIELD[method])
        if (res['result'] != 'success'):
            raise HTTPError('transmission has occured an error at torrent-get')

        for torrent in res['arguments']['torrents']:
            if(torrent['percentDone'] is 1):
                complete_torrent.append(torrent)
        return complete_torrent

    def add(self, payload):
        print("add")
        method = 'torrent-add'
        res = self.__request__(method, {"metainfo": payload})
        if(res['result'] != 'success'):
            return None
        else:
            torrent = res['arguments'].get('torrent-added', None)
            torrent_id = 0
            if torrent is not None:
                torrent_id = torrent['id']
            else:
                torrent_id = res['arguments']['torrent-duplicate']['id']

            return self.__torrent_info__(torrent_id)

    def delete(self, torrent):
        method = 'torrent-remove'
        torrent_info = self.__torrent_info__(torrent['id'])
        res = self.__request__(method, {"ids": torrent['id']})
        if(res['result'] != 'success'):
            return None
        else:
            return torrent_info

    def pause(self, torrent):
        method = 'torrent-stop'
        torrent_info = self.__torrent_info__(torrent['id'])
        res = self.__request__(method, {"ids": torrent['id']})
        if(res['result'] != 'success'):
            return None
        else:
            return torrent_info


'''

'''
