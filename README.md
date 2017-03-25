# pi-email-transmission[PET] 

 - 이 프로그램은 *이메일 서비스*와 *트렌스미션 웹 컨트롤러* 두 개를 이용합니다.
 - 이것은 라즈베리의 트렌스 미션을 통해 여러분의 소중한 노트북의 자원을 아껴줍니다. 
 - 이 프로그램은 트랜스미션과 이메일 서비스의 기능들에 의존합니다.
 - 간단히 말하면 이메일 서비스와 트렌스미션 웹 컨트롤러를 융합해놓은 CLI환경의 프로그램입니다. 

# 동기

 - "토렌트 다운받는데 느린 주제 리소스도 많이 잡아먹고... 그와 동시에 자원낭비도 하기 싫고.. 지금 당장 안봐도 집에가서 볼껀대.. 무엇보다 노트북과 핸드폰 발열이 짜증나!" 

# 추천 사용 방법!!
   
1. 라즈베리파이에서 구동해주세요. 여러분의 소중한 노트북을 위해!
2. 트랜스미션의 다운로드 경로를 *Dropbox*와 *Google-Drive*의 폴더로 지정해서 사용해주세요.
3. 라즈베리파이를 사용하기 때문에 저장공간이 많이 부족할것입니다. 외장하드가 있거나 HDD가 있다면 사용해주세요. 
4. 스마트폰에 자신이 사용하고 있는 메일서비스 알람을 켜두세요. 그리고 구글 드라이브와 드롭박스를 이용하세요! 매우 편리할것입니다. 

# 설치

 ``` bash
$ git clone https://github.com/drake-jin/pi-email-transmission
$ cd pi-email-transmission
$ python setup.py install
 ```

# 설정방법

1. 트렌스미션 웹 컨트롤러 셋팅을 해주세요.

    - 편집-> 기본설정 -> 원격접속에서 "{호스트}:{포트}", "{계정}/{비밀번호}" 설정을 잡아줍니다.
    - 주의 !! 반드시 host주소와port를 확인해주세요 !! 

2. 이메일 계정의 IMAP과 SMTP의 접근을 허용해주세요. 
    - (IMAP과 SMTP중 하나만 쓸 수 있는 방법이 있다면 이슈를 달아주세요)
    - 이 프로그램은 IMAP과 SMTP 프로토콜 두 개를 사용합니다.(약간 비 효율적이게도...)
    - 그러므로 이용하고 계신 이메일의 IMAP과 SMTP프로토콜 접근을 허용해주셔야 합니다.

3. *pi-email-transmission*/config.json 셋팅을 잡아주세요

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

4. 환경변수를 셋팅해줍니다.(환경변수를 셋팅하지 않아도 되는 방법이 있다면 이슈 달아주세요) 
 ```
  export PET_HOME=/home/likemilk/workspace/pi-email-transmission
 ``` 

5. 마지막으로 여러분들이 셋팅한것을 확인해 봅니다.
 
 ```
  $ python setup.py test
 ```

6. 정상적으로 테스트 코드가 돌았으면 설정이 완료된것입니다. 축하합니다! 

 ```
  $ pet help 
 ```
 
를 이용하여 사용방법에 대해 알아보세요 

# 작동 원리

``` python
# 단지 수도코드 입니다. 실제 코드가 아닙니다.
class Service(Thread):

    while(True):
        time.sleep(config['interval_check'])
        # 1. 이메일 계정에 있는 UNSEEN플래그를 가진 이메일을 가져옵니다. 
        # 2. 안 읽은 이메일 토렌트 첨부파일을 가져와서 "트렌스미션"에 페이로드를 전송합니다.
        # 3. 트렌스미션에 추가하면서 성공과 실패에 대한 메일을 전송합니다.
        # 4. 작업이 끝난 이메일에게 SEEN 플래그를 남겨서 읽음 표시를 합니다.
        torrentList = email.get_torrent('(UNSEEN)')
        for torrent in torrentList:
            if(transmission.add_torrent(torrent)):
                email.send('add_complete', torrent)
            else:
                email.send('add_fail', torrent)

            email.flag('(SEEN)',torrent.email_id)

        # 1. 트렌스미션의 다운로드 Queue에 있는 목록들을 읽어옵니다.
        # 2. 완료된 목록을 가져오고 그 완료된 녀석을 다운로드 Queue에서 삭제합니다.
        # 3. 그리고 자신의 계정에 다운로드 완료 표시의 메일을 전송합니다. 
        torrentList = transmission.get_completed('Completed')
        for torrent in torrentList:
            if(transmission.delete_torrent(torrent)):
                email.send('download_complete')
            else:
                email.send('delete_error')
             
```

# 연락처 
 - [dydwls121200@gmail.com](dydwls121200@gmail.com) 
 - [github 주소](https://github.com/drake-jin) 
 - 카카오톡 주소 : dydwls121200 

# 맺음말 
 - *PR* 이나*MR* 뭐든지 환영합니다. 
 - *피드백*, *조언* 그리고 *지적* 정말 전부 *환영*합니다. 뭐든지 환영합니다.
 - 함께하는 오픈소스 코딩은 너무 재밌다구용!
 - 버전이 나오고 오랜기간이 지나도 피드백을 주시거나 이용하시는 분이 계시다면 언제든지 수정할 용의가 있습니다 
