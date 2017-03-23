class PETContext:
    TEXT = 'THIS IS TEXT'
    HELP = {
        'wrong':
        '''
    You can only use {start|stop|restart|status|test|help} command.
    If you need more information about this.
    execute this command. 'pet help'
        ''',
        'usage':
        '''
    Welcome to PET[Raspberry-(P)i (E)mail (T)ransmission]

    [Usage]
      pet {start|stop|restart|status|test|help}

    [Command]
      start : Run 'pet' program as a daemon
      stop : Stop 'pet' program and shutdown
      restart : Exectue 'start' and 'stop'
      status : Notice about dead or alive
      test : Varify that your configurations or environments
      help : Let you know about this program

    [Contact Me]
      I really expect to send feedback or Pull Request.
      Actually, I need your helps. Thnaks for downloading.
      # Github : github.com/drake-jin/pi-email-transmission
      # E-Mail : dydwls121200@gmail.com
        '''
    }

    EMAIL_FORMATTING = '''From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: %s

%s
    '''

    EMAIL_FORMAT = {
        # help: {name,downloadDir,sizeWhenDonw,files},
        "add_success": {
            "subject": "[PET][Add Success]{subject}",
            "content": '''
    <h2>PET Success for adding torrent on transmission</h2>
    <ul>
        <li>
            <em>Torrent Name : </em> {name}
        </li>
        <li>
            <em>Downlaod Directory : </em> {downloadDir}
        </li>
        <li>
            <em>Size of download file when done : </em> {sizeWhenDone}
        </li>
        <li>
            <em>Downlaod Files:</em>{files}
        </li>
    </ul>
    <h2>Help: dydwls121200@gmail.com</h2>
                        ''',
            "files": "<div><em>{name}</em>  {length: {length} }</div>"
        },
        # help: content has {files}, files has {file}
        "add_fail": {
            "subject": "[PET][Add Fail]Opps! Occured errors ",
            "content": '''
    <h2>While adding download queue Transmission web
            controller has occured errors.</h2>
    <em> Please check tranmission queue.</em>
    This program don't know yet whether few of files were barely successed.
    <h4>There was an error of your attachments or System Environment </h4>
    <ul>{files}</ul>
    <h2>Help: dydwls121200@gmail.com</h2>
                    ''',
            "files": "<li>{file}</li>"
        },
        "delete_success": {
            "subject": '''
    [PET][Completely download & Delete completed]
            Contratulation!! Downloading is done!
            ''',
            "content": '''
    <h2>PET deleted completely downloaded torrent.</h2>
    <em>If you use Dropbox and Google Drive,
            PET recommand to change download path for there service</em>
    <h2> Description </h2>
    <ul>
        <li>
            <em>Name : </em>{name}
        </li>
        <li>
            <em>Download Directory : </em>{downloadDir}
        </li>
        <li>
            <em>Size of download file When done : </em> {sizeWhenDone}
        </li>
        <li>
            <em>Files</em>{files}
        </li>
    </ul>
    <h2> Help : dydwls121200@gmail.com </h2>
            ''',
            "files": "<div><em>{name}</em> | size :  {bytesCompleted} </div>"
        },
        "delete_fail": {
            "subject": '''
    [PET][Completely download. but, didn't delete to completed torrent]
            Opps!! Occured an error!!
                ''',
            "content": '''
    <h2>torrent is completely downloaded.
            but, PET can't delete torrent in download queue</h2>
    <em>If you use Dropbox and Google Drive,
            PET recommand to change download path for there service</em>
    <h2> Description </h2>
    <ul>
        <li><em>Name : </em>{name}</li>
        <li><em>Download Directory : </em>{downloadDir}</li>
        <li><em>Size of download file When done : </em> {sizeWhenDone}</li>
        <li><em>Files</em>{files}</li>
    </ul>
    <h2> Help : dydwls121200@gmail.com </h2>''',
            "files": "<div><em>{name}</em> | size :  {bytesCompleted} </div>"
        }
    }

    TRNS_FIELD = {
        "torrent-get": {
            "fields": [
                "id",
                "activityDate",
                "corruptEver",
                "desiredAvailable",
                "downloadedEver",
                "fileStats",
                "haveUnchecked",
                "haveValid",
                "peers",
                "startDate",
                "trackerStats",
                "comment",
                "creator",
                "dateCreated",
                "files",
                "hashString",
                "isPrivate",
                "pieceCount",
                "pieceSize",
                "name",
                "downloadDir",
                "percentDone",
                "sizeWhenDone"
            ],
            "ids": [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
                61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
                71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
                91, 92, 93, 94, 95, 96, 97, 98, 99, 100
            ]
        },
        "session-get": {
        }
    }
