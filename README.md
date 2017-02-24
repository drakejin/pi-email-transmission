# *This project is not available yet. Now procceeding*


1. IMAP Read Function.
 1. [x] Connect with Email through IMAP Protocol
 2. [x] Connect with Transmission Web Controller throu http Protocol
 3. [x] Read folder of Email List And Get torrent files.
 4. [x] The torrent files will be transported to transmission web controller.
 5. If the 4th work were Okey, This program send through READ flag to
 Connected Email Account.
 6. At the same time, Send an mail to connected account what transmission
 successfully regist your torrent files with detail information.

2. Send an Notify Function






# pi-imap-transmission  
 
 - This program read your email service through IMAP protocol to install any torrent
 - This program notify download complete to send email to your email account
 - This program service to install downloaded files everywhere using web service(if you want to use this)
 - This program is recommanded using raspberry-pi to reduce desktop or laptop resources while installing media file

# Motivate

 - Inspired of [nupamore's anisub proejct](https://github.com/nupamore/anisub), [harlob's project](https://github.com/harlov/e2transmission)
 - I don't wanna waste resources on my laptop. cause' it's totally be hot when running torrent.



# Recommand
   
 1. you have to mount external storage and modify confiuration file. 


# Required

 1. Install packages 'transmission-cli transmission-web' for bittorrent.  
    
  ``` bash
sudo apt-get install transmission-cli transmission-web -y
  ```

 2. Modify 'pi-imap-config.json'

  ``` js
{
    "email_check_interval" : 5,
    "email_host" : "imap.{imap_host}",
    "email_port" : {imap_port},
    "email_torrent_folder" : "torrent-folder",
    "email_notify_folder" : "notify-folder",
    "email_user" : "*****@****.***",
    "email_password" : "*********",
    "transmission_user" : "********",
    "transmission_password" : "*********",
    "transmission_host" : "http://{host}:{port}"
}
  ```

# Install 

 ``` bash
$ git clone https://github.com/drake-jin/pi-imap-torrent
$ python pi-imap-torrent install
 ```

# Usage

 1. Modify setting file  ~/.config/transmission/settings.json
  ``` bash
{
 ...

"rpc-username": "{username}" ,
"rpc-password" : "{password}",
"rpc-port": 9091,
"rpc-authenication" : true,
 ...
}
  ```

 2. Modify setting file {THIS_PROEJC_GIT}/pi-imap-config.json

 3. Run


# Contact Me
 
 - [dydwls121200@gmail.com](dydwls121200@gmail.com) is my mail
 - Welcome PR or be Contributor. I want to play coding with you.
