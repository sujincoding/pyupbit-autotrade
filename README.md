# 1. 코인 자동 매매 프로그램 

## 1.1. 프로그램 소개   
 pyupbit 라이브러리를 활용하여 upbit 거래소에서 비트코인 자동매매를 하는 프로그램     

거래소 : UPbit
투자 전략 구현 도구 : Python
매매 알림 : Slack

## 1.2. 프로그램 개발 개요
* ### UPbit 가입 및 API 키 발급받기   
   * API 키 발급 방법   
     + UPbit 사이트>고객센터>Open API 안내>OpenAPI 사용하기>Open API Key 발급받기 (Access Key, Screte Key)   
* ### 개발 환경 셋팅   
  * 파이썬 3.8.9 설치   
  * VSCode 에 설치한 파이썬 환경 설정   
  * Pyupbit 라이브러리 다운로드 및 임폴트
* ### Slack 연동
* ### 클라우드 서버 연동 및 실행
  * AWS 가입 및 Ubuntu 서버 생성   
    + AWS 프리 티어 사이트 > AWS 서비스 > EC2 > 인스턴스 > 인턴스 시작 > Ubuntu Server 사용 > 키 페어 생성(서버에 접속하는 키)
  * UPbit 사이트 Open API 관리에서 Ubuntu 서버 추가
  * Ubuntu 서버에 본인 Github 코드 가져오기
  * Ubuntu 서버 셋팅 (1.4 참고)
  * Ubuntu 서버에서 bitcoinAutoTrade.py 실행
  
## 1.3. Project 구성  
* test.py : 잔고 조회, UPbit Open API 라이브러리를 이용하여 Key 전달하여 본인의 거래소와 연동
* backtest.py : 백테스팅 코드    
* bestK.py : 가장 좋은 k 값을 찾는 코드   
* bitcoinAutoTrade.py : 변동성 돌파 전략 비트코인 자동매매 코드   
* bitcoinAutoTradeWithMA.py : 변동성 돌파 전략 + 15일 이동평균선 이상 비트코인 자동매매 코드    
* bitcoinAutoTradeWithSlack.py : 위 코드에 슬랙 붙여 놓은 것   

## 1.4. Ubuntu 서버 명령어  
* 한국 기준으로 서버 시간 설정: sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime  
* 현재 경로 상세 출력: ls -al   
* 경로 이동: cd 경로   
* vim 에디터로 파일 열기: vim bitcoinAutoTrade.py   
* vim 에디터 입력: i   
* vim 에디터 저장: :wq!   
* 패키지 목록 업데이트: sudo apt update   
* pip3 설치: sudo apt install python3-pip   
* pip3로 pyupbit 설치: pip3 install pyupbit   
* 백그라운드 실행: nohup python3 bitcoinAutoTrade.py > output.log &   
* 실행되고 있는지 확인: ps ax | grep .py   
* 프로세스 종료(PID는 ps ax | grep .py를 했을때 확인 가능): kill -9 PID   

---------
## ○ 참고 문헌  
* [유튜브 조코딩 채널](https://youtube.com/playlist?list=PLU9-uwewPMe3KKFMiIm41D5Nzx_fx2PUJ)   
* [파이썬을 이용한 비트코인 자동매매 (개정판)](https://wikidocs.net/book/1665)     



