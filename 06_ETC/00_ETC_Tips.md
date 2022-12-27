# 기타팁
### VSC Tip
- 단축키
  - ctrl d : 동시에 선택된 모든 것 바꿀 수 있음
  - ctrl l : 터미널 초기화
  - ctrl / : 주석처리
  - ctrl x : 한 줄 잘라내기(그냥 지우기 용도로 편함)  
  - ctrl alt 화살표 : 동시선택
  - alt click : 동시선택
  - alt 방향키 : 줄이동
  - alt shift 방향키 : 복제
  - tab : 터미널에서 일정량 친 후에 텝 누르면 파일이름 자동 입력 해줌
  - import random : random이라는 모듈 안에서
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


# API vs Json
- API : **A**pplication **P**rograming **I**nterface
- 브라우저: --요청(request, API)--> 서버
  - Client <--응답(respond, Json)-- Server
- source : ex) mnd, agify.io , naver api (네이버api 검색하면 오픈api를 얻을 수 있음), kakao api, etc..
- mnd key 이건 지우자고 7135f382285b7a42b12f2513bd58adb1

```python
URL = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(URL).json() #.json : json 형태로온걸 딕셔너리 형태로 변환
print(response)
```

##### in request module's method
- 주소에 직접 입력 할 수 있는 것을 request를 이용하여 보내는 것임.
  - 즉, 그냥 풀 주소를 써서 넣어도 됨, 같은 거
- get : (서버에 있는) 데이터를 조회할때
- post : (서버에 있는) 수정할때(ex) 댓글 생성 or 수정)
- put : (서버에 있는) 수정
- delete : (서버에 있는) 지우는 것(ex) 댓글 삭제, 회원 탈퇴 등)

##### URL
https://www.blabla.com/api/v1/movie/now_playing/?key=as535&name=user_name&region=korea
프로토콜 / Base url / path(movie~now_playing) / parameter(?~) : key = value & k = v & ...이런 구조임 (처음 나오는 key는 사용자가 권한이 있는지 확인하는 것, 권한 없으면 안줌..)



a = [1, 2, 3]
b = [4, 5, 6]
c = a.extend(b)
print(c) #None : 반환값... mutable

a = 'abc'
a.replace(z)
print(a) #zbc : immutable

if not users: <- 비어있는지 확인할 때는 이렇게 쓰자
if len(users) == 0 <- 이렇게 쓰지말자

1. 변수, 함수명은 의미있게 짓자.
2. 변수, 함수명은 스네이크 케이스 / 클래스는 캐멀 케이스
3. True/False evaluation -> 빈 컨테이너, ZBoolean 검사, 단 값은 무조건 그대로
4. else가 필요없는 경우
5. 중복된 코드는 함수로 묶자
6. 복잡한 코드는 주석을 달자

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


# CMD 관리자권한 실행법
- 윈도우 마크 우클릭 -> 터미널(관리자) (window11)
- 마리아 DB Dump등 사용시 엑세스 거부가 뜨는 경우가 있는데 이러할 때 관리자 권한으로 실행하면 해결할 수 있음