import imaplib
import email


class IMAPController:
    def __init__(self, config):
        self.config = config

        # get imap connection
        self.connection = imaplib.IMAP4_SSL(
            self.config['host'], self.config['port']
        )
        self.connection.login(
            self.config['user'], self.config['password']
        )

    def check(self):
        self.connection.select(self.config['input_folder'])
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
                        # dict 형태로 만들어서 메일의uid값을 함께 보내주자.
                        payload_list.append(part.get_payload())

            except Exception as e:
                print(e)
        print(payload_list)
        return payload_list

    def send(self, torrent, cmd=None):
        if(cmd is None):
            print('send:[', cmd, ']')
        elif(cmd == 'dd'):
            pass
        else:
            print('send:[', cmd, ']')


class TransmissionController:
    def __init__(self, config):
        print('TransmissionController-init')
        self.config = config
        auth = base64.encodestring(
            ('%s:%s' % (self.user, self.password)).encode()
        ).decode().replace('\n', '')
        self.auth = auth

    def __request(self, method='torrent-get', req):
        req.add_header("Content-Type", "application/json")
        req.add_header("Authorization", "Basic %s" % self.auth)

        if self.session_id:
            request_obj.add_header(
                "X-Transmission-Session-Id",
                self.session_id
            )

    def check(self):
        print('TransmissionController-check')
        complete_torrent = ['cmplt-check-1', 'cmplt-check-2']
        return complete_torrent

    def add_torrent(self, torrent):
        print('TransmissionController-add_torrent')
        return True

    def delete(self, torrent):
        print('TransmissionController-delete')
        return True
