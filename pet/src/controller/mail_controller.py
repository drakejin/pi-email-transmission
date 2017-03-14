import imaplib
from smtplib import SMTP_SSL
from smtplib import SMTPException
import email

from pet.utils import Logger

logger = Logger.getLogger()


class MailController:
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
        imap = self.config['service']['email']['imap'].split(':')
        self.IMAPconnection = imaplib.IMAP4_SSL(
            imap[0],
            imap[1]
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
        except SMTPException as e:
            logger.debug(str(e))
            logger.debug(e)
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

        email_form = MailController.email_format % (
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
        email_form = MailController.email_format % (
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

        email_form = MailController.email_format % (
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

        email_form = MailController.email_format % (
            self.config['service']['email']['user'],
            self.config['service']['email']['user'],
            email_form['subject'].replace('{subject}', torrent_info['name']),
            content
        )
        self.__send_email__(email_form)


'''

'''
