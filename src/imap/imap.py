import imaplib
import json
import os
import time
from email import parser
import email
from logger import DJLogger
from transmission_rpc import TransmissionRpc

logger = DJLogger.getLogger()

logger.debug("read")

with open(os.environ['PROJECT_HOME']+'/config.json') as configJson:
    logger.debug(configJson)
    configData = json.load(configJson)
    logger.debug(configData)


emailConnection = imaplib.IMAP4_SSL(
    configData['email_host'],
    configData['email_port']
)
emailConnection.login(
    configData['email_user'],
    configData['email_password']
)

transmissionConnection = TransmissionRpc(configData)


def proc_email(message, mail_id):
    msg = email.message_from_bytes(message)
    seen_flag = False

    for part in msg.walk():
        logger.debug(part.get_content_type())
        if part.get_content_type() == 'application/x-bittorrent':
            torrent_data_64 = part.get_payload()

            # regist torrent file
            result = transmissionConnection.request(
                "torrent-add",
                {"metainfo": torrent_data_64}
            )
            logger.debug(result)

        # set seen flag
        seen_flag = True

    return seen_flag


def run():
    logger.debug("run")
    # transmissionRpc(config)

    while True:
        time.sleep(configData['email_check_interval'])
        logger.debug("loop start----------------------- ")
        logger.debug("-- Check Email ")
        emailConnection.select(configData['email_input_folder'])
        logger.debug(emailConnection.search(None, 'ALL'))

        # result, data = emailConnection.uid('SEARCH', None, '(UNSEEN)')
        result, data = emailConnection.uid('SEARCH', None, '(UNSEEN)')

        logger.debug(result)
        logger.debug(data)
        uids = data[0].split()

        for uid in uids:
            try:
                result, data = emailConnection.uid('fetch', uid, '(RFC822)')
                seen = proc_email(data[0][1], uid.decode('UTF-8'))
                if seen:
                    result = emailConnection.store(uid, '+FLAGS', '\\Seen')
                    # result = emailConnection.fetch(uid.decode('UTF-8'), '(+FLAGS (\\Seen)')
                    logger.debug(result)
            except Exception as e:
                logger.debug(e)

        logger.debug("loop end----------------------- ")


run()




