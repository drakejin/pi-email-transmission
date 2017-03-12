import sys
import imaplib
from smtplib import SMTP_SSL
import email
import base64
import json

from pit.utils.logger import DJLogger
if sys.version_info < (3,):
    from urllib2 import Request
    from urllib2 import HTTPError
    from urllib2 import urlopen
else:
    from urllib.request import Request
    from urllib.error import HTTPError
    from urllib.request import urlopen as urlopen

logger = DJLogger.getLogger()


class IMAPController:
    email_format = '''From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: %s

%s
'''

    def __init__(self, config):
        self.config = config
        # get imap connection
        self.IMAPconnection = imaplib.IMAP4_SSL(
            self.config['service']['email']['host'],
            self.config['service']['email']['port']
        )
        self.IMAPconnection.login(
            self.config['service']['email']['user'],
            self.config['service']['email']['password']
        )

    def __send_seen_flag__(self, uid):
        print('__send_flag email:', email)
        result = self.IMAPconnection.uid('STORE', uid, '+FLAGS', '\\Seen')
        logger.debug(result)

    def __send_email__(self, email):
        logger.debug(email)
        try:
            server = SMTP_SSL(self.config['service']['email']['smtp'])
            server.ehlo()
            server.login(
                self.config['service']['email']['user'],
                self.config['service']['email']['password']
            )
            server.sendmail(
                self.config['service']['email']['user'],
                self.config['service']['email']['user'],
                email
            )
            server.quit()
        except Exception as e:
            logger.debug(str(e))
            logger.debug(str(e.__dict__))

    def check(self):
        self.IMAPconnection.select(self.config['service']['email']['folder'])
        result, data = self.IMAPconnection.uid('SEARCH', None, '(UNSEEN)')
        uids = data[0].split()
        payload_list = []

        for uid in uids:
            try:
                result, data = self.IMAPconnection.uid(
                    'fetch', uid, '(RFC822)'
                )
                msg = email.message_from_bytes(data[0][1])
                for part in msg.walk():
                    if(part.get_content_type() == 'application/x-bittorrent'):
                        # send email's uid and payload
                        payload_list.append(
                            {
                                "payload": part.get_payload(),
                                "uid": uid
                            }
                        )

            except Exception as e:
                print(e)

        return payload_list

    def add_success(self, torrent_info, uid):
        logger.debug('add_success | torrent_info: ' + str(torrent_info))
        logger.debug('add_success | uid: ' + str(uid))
        self.__send_seen_flag__(uid)
        email_form = self.config['docs']['email']['add_success']
        content = email_form['content']
        files = email_form['files']
        file_list = []

        for f in torrent_info['files']:
            file_list.append(
                files.replace("{name}", f['name']).replace(
                    "{length}", str(f['length']))
            )

        print("</br>".join(file_list))
        content = content.replace("{name}", torrent_info['name'])\
            .replace("{downloadDir}", torrent_info['downloadDir'])\
            .replace("{sizeWhenDone}", str(torrent_info['sizeWhenDone']))\
            .replace("{files}", "</br>".join(file_list))

        email_form = IMAPController.email_format % (
            self.config['service']['email']['user'],
            self.config['service']['email']['user'],
            email_form['subject'].replace('{subject}', torrent_info['name']),
            content
        )

        self.__send_email__(email_form)

    def add_fail(self, uid):
        logger.debug('add_fail | uid: ' + str(uid))
        self.__send_seen_flag__(uid)

        email_form = self.config['docs']['email']['add_fail']
        filenames = []
        try:
            result, data = self.IMAPconnection.uid(
                'fetch', uid, '(RFC822)'
            )
            msg = email.message_from_bytes(data[0][1])
            for part in msg.walk():
                if(part.get_content_type() == 'application/x-bittorrent'):
                    filenames.append(part.get_param('name'))

        except Exception as e:
            print(e)

        form_files = email_form['files']
        file_list = []
        for f in filenames:
            file_list.append(form_files.replace("{file}", f))

        content = email_form['content']
        content = content.replace("{files}", "</br>".join(file_list))
        print("149149149: ", "</br>".join(file_list))
        email_form = IMAPController.email_format % (
            self.config['service']['email']['user'],
            self.config['service']['email']['user'],
            email_form['subject'],
            content
        )
        self.__send_email__(email_form)

    def delete_fail(self, torrent_info):
        logger.debug('delete_fail | torrent_info: ' + str(torrent_info))
        email_form = self.config['docs']['email']['delete_fail']
        content = email_form['content']
        files = email_form['files']
        file_list = []

        for f in torrent_info['files']:
            file_list.append(
                files.replace("{name}", f['name']).replace(
                    "{length}", str(f['length']))
            )

        print("</br>".join(file_list))
        content = content.replace("{name}", torrent_info['name'])\
            .replace("{downloadDir}", torrent_info['downloadDir'])\
            .replace("{sizeWhenDone}", str(torrent_info['sizeWhenDone']))\
            .replace("{files}", "</br>".join(file_list))

        email_form = IMAPController.email_format % (
            self.config['service']['email']['user'],
            self.config['service']['email']['user'],
            email_form['subject'].replace('{subject}', torrent_info['name']),
            content
        )

        self.__send_email__(email_form)

    def delete_success(self, torrent_info):
        logger.debug('delete_success | torrent_info: ' + str(torrent_info))
        email_form = self.config['docs']['email']['delete_success']
        content = email_form['content']
        files = email_form['files']
        file_list = []

        for f in torrent_info['files']:
            file_list.append(
                files.replace("{name}", f['name']).replace(
                    "{length}", str(f['length']))
            )

        print("</br>".join(file_list))
        content = content.replace("{name}", torrent_info['name'])\
            .replace("{downloadDir}", torrent_info['downloadDir'])\
            .replace("{sizeWhenDone}", str(torrent_info['sizeWhenDone']))\
            .replace("{files}", "</br>".join(file_list))

        email_form = IMAPController.email_format % (
            self.config['service']['email']['user'],
            self.config['service']['email']['user'],
            email_form['subject'].replace('{subject}', torrent_info['name']),
            content
        )
        self.__send_email__(email_form)


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
            % (self.__config['service']['transmission']['host']),
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
            except HTTPError as e:
                if e.code == 409:
                    self.__session_id = e.headers['X-Transmission-Session-Id']

        res = json.loads(res.read().decode('utf-8'))
        return res

    def __get_session__(self):
        self.__request__('session-get')

    def __torrent_info__(self, torrent_id):
        method = 'torrent-get'
        field = self.__config['field'][method]
        field['ids'] = [torrent_id, ]
        print('203 : ', field)
        return self.__request__(method, field)['arguments']['torrents'][0]

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

    def add(self, payload):
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
        res = self.__request__(method, {"id": torrent['id']})
        if(res['result'] != 'success'):
            return None
        else:
            return torrent_info


'''

'''
