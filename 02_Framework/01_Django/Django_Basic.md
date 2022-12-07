# Django
- Djago Intro
- Django 구조 이해하기(MTV Design Pattern)
- Django Quick start
- Django Template
- Sending and Retrieving form data
- Django URLs
- 마무리

### Django Intro
- Framework
   - 틀을 가지고 일한다 (Framework == 밀키트)a
   - 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
     - 내가 만들고자 하는 본질에 집중 -> 소프트웨어의 생산성과 품질을 높임
- Django를 배워야하는 이유
  - Flask, Django, FastAPI와 같은 python으로 작성된 프레임워크
  - Python이라는 언어의 강력함과 거대한 커뮤니티
  - 수많은 여러 유용한 기능들
  - 검증된 웹 프레임워크
    - Toss, 당근마켓, 요기요등 유명 서비스에서 사용

#### Web 이해하기
- 세계는 해저케이블을 통해 연결되어 있음
- 스타링크 프로젝트를 이용해 위성간 데이터 통신
- 인터넷을 이용하는 건, 전세계의 컴퓨터가 연결되어 있는 하나의 인프라를 이용하는 것

#### 클라이언트와 서버
- 클라이언트 - 서버 구조 : 요청, 응답
- 클라이언트
  - 웹 사용자의 인터넷에 연결된 장치(ex) wifi에 연결된 컴퓨터 또는 모바일)
  - Chrome과 같은 웹 브라우저
  - 서비스를 요청하는 주체
- 서버
  - 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
  - 클라이언트가 웹 페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
  - 요청에 대해 서비스를 응답하는 주체
  - **Django는 서버를 구현하는 웹 프레임워크**

#### Web browser와 Web page
- 웹 브라우저
  - 웹에서 페이지를 찾아 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
  - 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는(redering) 프로그램
- 웹 페이지
  - 웹에 있는 문서
    - 우리가 보는 화면 각각 한 장 한 장이 웹페이지
  - 웹 페이지의 종류
    - 정적 웹 페이지
    - 동적 웹 페이지
  - 정적 웹 페이지(Static Web page)
    - 있는 그대로 제공하는 것, 모든 사용자에게 동일한 모습으로 전달되는 것
  - 동적 웹 페이지
    - 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
    - 웹 페이지의 내용을 바꿔주는 주체 == 서버
      - 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌
      - 이렇게 사용자의 요청을 받아서 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크 : Django, Spring boot 등등

### Django 구조 이해하기

#### Design Pattern
- 자주 사용되는 구조를 일반화해서 하나의 패턴으로 만듦
- 소프트웨어 디자인 패턴의 장점
  - 커뮤니케이션이 매우 간단해짐
    - ex) "클라이언트-서버 구조로 구현하자"

#### Django's Design Pattern
- Django의 디자인 패턴은 MTV패턴
  - MTV 패턴은 MVC 디자인 패턴을 기반으로 조금 변형된 패턴
    - MVC vs MTV
    - 큰 차이점은 없지만 일부 역할에 대해 부르는 이름이 다름
    - Model == Model
    - View == Template
    - Contrioller == View
  - MVC 소프트웨어 디자인 패턴
    - Model - View - Controller의 준말
      - Model : 데이터와 관련된 로직을 관리
      - View : 레이아웃과 화면을 처리
      - Controller : 명령을 model과 view 부분으로 연결
    - 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
    - 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
- MTV 디자인 패턴
  - Template -> 화면
  - View <- 요청
  - Model <-> 'DB'
  - 실행과정 (Django가 담당하는 부분)
    - (HTTP가 Request <- 브라우저가 수행)
    - URLS가 View로 Request
    - View가 받고 Model에 데이터 요청
    - Model이 DB를 가지고 데이터 응답
    - Template이 화면에 뿌림
    - View가 HTML의 요청에 응답

### 가상환경 설정(window)
- *첫 자만 쓰고 tab하면 편하게 쓸 수 있음*
- cf) .gitignore를 사용할거면 먼저 만들고 해야 제대로 작동시킬 수 있음.
  - (가상환경 파일이 너무 크기 때문에, 깃에 공유하려면 하는게 좋음)
- 폴더에 가상환경 생성 : python -m venv venv
- 가상환경 켜기 : source venv/Scripts/activate  // mac의 경우 Scripts 대신에 bin
  - 켜지면 (venv)와 같이 켜진환경 표시
  - 끌때는 deactivate
- 설치한 패키지 목록 조회 : pip list
- django 설치하기 : pip  install django==3.2.13
- requirements.txt 생성 : pip freeze > requirements.txt   // <- 이 파일에 들어가면 pip list내용이 들어감
  - 이걸 왜하냐, 가상환경 용량이 크기 때문에 따로 기입해두고, 이거를 통해서 한 번에 다른 컴퓨터에서 편하게 설치 가능. 나중에 따로 추가하는 건 똑같이 해서 덮어씌우면 됨
  - requirements.txt 목록 설치 pip install -r requirements.txt
- django 프로젝트 생성 : django-admin startproject firstpjt . <- **'.'** 중요!!
- django 서버 실행 : python manage.py runserver
- python manage.py startapp articles
- INSTALLED_APPS에 앱을 등록
  - firstpjt폴더(프로젝트)에서 settings.py에 만든 앱 이름을 넣어주면됨 여기서는 articles
- urls.py에 path 등록
  - urls사용시 path 뒤에는 /를 꼭 붙여주자
  - 뒤에 데이터가 없더라도 ,를 붙여주자(확장성)
- views.py에 함수 생성  <- 첫번째 인자는 무조건 request
  - 이 방법은 fuction based view(fbv)이지만, class based view(cbv)도 있다.
- template 생성
- 확인하려면 서버열면 됨

- urls -> views -> templates 순서로


### Django Quick start

### Django Template
- Django Template Language(DTL)
- built-in template system
- 조건, 반복, 변수, 치환, 필터 등의 기능
  - python 코드로 실행되는 것이 아님
  - python이 HTML에 포함된 것이 아님
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것임을 명심!
  - 난발하는거 별로 안 좋음
- {{ name }}
- |length 와 같은게 필터 이는 사이트에서 참고하면서 봐야함
  - https://docs.djangoproject.com/en/3.2/ref/templates/builtins/   

#### template 상속
- 코드 재활용에 초점을 맞춤
- 상속을 하게되면, 수정하기에도 편리하다.
  - 상속받는 경우 반드시 최상단에 

- base.html을 만들어 주려면 최상단 폴더에 templates 폴더를 만들고 그 안에 base.html을 만들고
  setting에서 인식할 수 있게끔 TEMPLATES안에 DIR에 주소를 써주면됨
  - (ex) [BASE_DIR / 'template',],

### Sending and Retrieving form data
#### sending form data(client)
- form
  - action : 어디에 전송? URL
  - method : 어떻게 전송? HTTP METHOD - GET, POST

- HTTP 메서드
  - GET(조회), POST(생성), PVT, DELETE(삭제)
  - GET - Quary~ 형식(ex)?~) 형식으로

### Django URLs
- Django는 URL 끝에 /가(Trailing slash) 없다면 자동으로 붙여주는 것이 기본 설정
  - 그래서 모든 주소가 '/'로 끝나도록 되어있음
  - 그래서 '/'잘 쓰자!
 
#### Variable routing
- Variable routing의 필요성
- <>로 변수 설정해서 사용가능 <- 라우터, 라우팅
- ex) <int:pk>
- 너무 많은 비슷한 페이지를 작성해야할 때 사용하면 매우 편리함.

### URL mapping
- 새 앱을 만들고나서
- urls를 각각 앱마다 다 만들어주고
- project의 url에서는 include를 통해서 각각 앱과 include를 써서 연결시켜주고
- 각각 앱의 urls에서 넣어주면됨(import . from~를 꼭써주자)




# 기타
VSCODE에 설치하면 아이콘 가시성 좋아짐 Material Icon Theme