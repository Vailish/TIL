# 기타팁
### VSC Tip
- 단축키
  - ctrl alt 화살표 : 동시선택
  - ctrl d : 동시에 선택된 모든 것 바꿀 수 있음
  - ctrl l : 터미널 초기화
  - alt click : 동시선택
  - alt 화살표 : 줄이동
  - tab : 터미널에서 일정량 친 후에 텝 누르면 파일이름 자동 입력 해줌
  - 방향키 : 사용했던 명령어 그대로 복사
  - import random : random이라는 모듈 안에서
  - ctrl / : 주석처리  
- 기타 방법
  - setting -> "format" -> Editor, Format on save : 저장시 자동 정렬

- window + E : 폴더 열기
- jupyter notebook 단축기 만들기
  - 기본 : git bash -> jupyter notebook 입력
  - 별명(단축키, alias) 설정 git bash -> jp 입력
    - git bash -> code ~/. bashrc -> VSC로 이동됨 -> alias jp="jupyter notebook" 입력후 저장 -> git bash로 이동 -> source ~/. bashrc 입력 -> jp 입력 -> 이제 jp 입력할때마다 실행됨.
  - 필요한 거 있을 때 "jp"랑 "jupyter notebook" 자리에 맞춰서 넣으면 단축키 설정 가능함!
    
  


##### commit convention message

- 넷상에 검색에서 검색해서 규칙 정할 필요가 있음 <- 정리하는 법 배우면 좋을듯!
- 회사나 조직에 따라서 다 다르게 정의 할 수 있기때문에 유동적으로 하면됨


##### cf) 컴퓨터는 시간을 어떻게 잴까?
- datatime
- timestamp
- 1970년 1월 1일 기준, 영국 그리니치 천문대에서 정한 시간을 기준으로 숫자로 세고있음 -> Timestamp

##### Chat bot

- **요청과 응답**

  ​                                                  요청 - API를 사용한 소통

  - 클라이언트(정보를 원하는) 와 서버(정보를 주는) 

    ​                                             응답 - 문서(HTML)

  - API 두 소프트웨어가 서로 통신할 수 있도록 연결 시켜주는 인터페이스(접점)

    - ex) 음식점에서 클라이언트와 서버, 그리고 메뉴판

  - http://apis.data.go.kr : 공공데이터 관리 사이트

    - 웹 크롤링 할때 좋음, 웹 크롤링 : 데이터를 긁어와서 필요한 정보 뽑아내는 것

  - 파이썬 챗봇 [파이썬 챗봇 (hphk.io)](https://py.hphk.io/) : 텔레그램 계정 연결