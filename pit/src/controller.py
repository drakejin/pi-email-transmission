import sys
import imaplib
import email
import base64
import json

if sys.version_info < (3,):
    from urllib2 import Request
    from urllib2 import HTTPError
    from urllib2 import urlopen
else:
    from urllib.request import Request
    from urllib.error import HTTPError
    from urllib.request import urlopen as urlopen


class IMAPController:
    def __init__(self, config):
        self.config = config
        # get imap connection
        self.connection = imaplib.IMAP4_SSL(
            self.config['service']['email']['host'],
            self.config['service']['email']['port']
        )
        self.connection.login(
            self.config['service']['email']['user'],
            self.config['service']['email']['password']
        )

    def check(self):
        self.connection.select(self.config['service']['email']['folder'])
        result, data = self.connection.uid('SEARCH', None, '(UNSEEN)')
        uids = data[0].split()
        payload_list = []

        for uid in uids:
            try:
                result, data = self.connection.uid('fetch', uid, '(RFC822)')
                # message = data[0][1] ,mail_id = uid.decode('UTF-8')
                msg = email.message_from_bytes(data[0][1])
                for part in msg.walk():
                    if(part.get_content_type() == 'application/x-bittorrent'):
                        # send email's uid and payload
                        payload_list.append(part.get_payload())

            except Exception as e:
                print(e)
        return payload_list

    def send(self, torrent, cmd=None):
        print('Email -- send --- =================================')
        if(cmd is None):
            print('send:[', cmd, ']')
        elif(cmd == 'dd'):
            pass
        else:
            print('send:[', cmd, ']')


class TransmissionController:
    def __init__(self, config):
        self.__config = config
        self.__session_id = None
        self.__auth = base64.encodestring(
            (
                '%s:%s' %
                (
                    self.__config['service']['transmission']['user'],
                    self.__config['service']['transmission']['password']
                )
            ).encode()
        ).decode().replace('\n', '')
        self.__get_session__()

    def __request__(self, method, arguments=None):
        message = {"method": method, "arguments": arguments}
        message = json.dumps(message).encode("utf-8")

        req = Request(
            "%s/transmission/rpc"
            % (self.__config['service']['transmission']['host']), message)
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
            except HTTPError as e:
                if e.code == 409:
                    self.__session_id = e.headers['X-Transmission-Session-Id']

        res = json.loads(res.read().decode('utf-8'))
        return res

    def __get_session__(self):
        # It just for getting the ' X-Transmission-Session-Id '
        self.__request__('session-get')

    def check(self):
        complete_torrent = []
        method = 'torrent-get'
        res = self.__request__(method, self.__config['field'][method])
        if (res['result'] != 'success'):
            raise HTTPError('transmission has occured an error at torrent-get')

        for torrent in res['arguments']['torrents']:
            if(torrent['percentDone'] is 1):
                complete_torrent.append(torrent)
        return complete_torrent

    def add_torrent(self, payload):
        print('TransmissionController-add_torrent')
        method = 'torrent-add'
        res = self.__request__(method, {"metainfo": payload})
        if(res['result'] != 'success'):
            return False
        else:
            return True

    def delete(self, torrent):
        method = 'torrent-remove'
        res = self.__request__(method, {"id": torrent['id']})
        if(res['result'] != 'success'):
            return False
        else:
            return True


'''

'''
