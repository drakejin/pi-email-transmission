# pi-email-transmission[PET] 

 - This program needs to set up two serivce. Email service and Transmission's Web Controller
 - It will be make cool if you download any files on Raspberry-pi through transmission 
 - This program's all about feature depend on Email service and Transmission.
 - Simply say about this. It just connect Email service and transmission web controller

# Motivate

 - I don't wanna waste resources on my laptop and Smartphone. cause' it's totally be hot when running torrent. 

# Recommand
   
1. Basically, This program is designed for reducing laptop resources. Therefore, I recommand to run this program on *raspberry-pi*.
2. Use this program with *Dropbox* or *GoogleDrive* to access your downloaded media files. 
3. If you can use E-Mail notification service on your smartphone, It's good interaction.

# Install 

 ``` bash
$ git clone https://github.com/drake-jin/pi-email-transmission
$ cd pi-email-transmission
$ python setup.py install
 ```

# Configuration

1. Set up transmission web controller setting

    - If you use Dropbox or GoogleDrive. redirect directory to there.
    - Must check you have account information and host, port

2. Check your e-mail account available IMAP and SMTP Protocol
    
    - This application need to transport through IMAP, SMTP Protocol.
    - Therefore, you must set up IMAP and SMTP protocol available on you email account.

3. Set up *pi-email-transmission*'s config.json file
 ``` js
// config.json
{
    "check_interval":10,
    "log_level":"DEBUG",
    "email":{
        "imap" : "imap.gmail.com:993",
        "smtp" : "smpt.gmail.com:465"
        "folder" : "pi-imap-transmission",
        "user" : "{email_id}@gmail.com",
        "password" : "{email_password}"
    },
    "transmission":{
        "user":"{trnsmsn_id}",
        "password":"{trnsmsn_passwd}",
        "host":"http://localhost:9091"
    }
}
  ```

4. Set up Envrironment variables 
> export PET_HOME=/home/likemilk/workspace/pi-email-transmission
 
5. Finally, You can check correct setting about this program when you execute this command
> $ python setup.py test
> # Have to finish setting Configurations! 

# How is it work going?

``` python
# *It's just psuedo code. not a real code*
class Service(Thread):

    while(True):
        time.sleep(config['interval_check'])
        # 1. read all of e-mails and check UNSEEN email 
        # 2. get torrent file and add it on tranmission through pay load
        # 3. send email about complete or failed
        # 4. send seen flag
        torrentList = email.get_torrent('(UNSEEN)')
        for torrent in torrentList:
            if(transmission.add_torrent(torrent)):
                email.send('add_complete', torrent)
            else:
                email.send('add_fail', torrent)

            email.flag('(SEEN)',torrent.email_id)

        # 1. read all of Trnasmission download Queue.
        # 2. get Completed entry and delete the entry.
        # 3. send email about complete.       
        torrentList = transmission.get_completed('Completed')
        for torrent in torrentList:
            if(transmission.delete_torrent(torrent)):
                email.send('download_complete')
            else:
                email.send('delete_error')
             
```

# Contact Me 
 - [dydwls121200@gmail.com](dydwls121200@gmail.com) is my mail
 - Welcome PR or be Contributor. I want to play coding with you.
