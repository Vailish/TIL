# Django
- The Django authentication system
- HTTP Cookies
- Authentication in Web requests
- Authentication with User
- Limiting access to logged-in users


# The Django authentication system

- Authentication(인증)
  - 신원 확인
  - 사용자가 자신이 누구인지 확인하는 것
- Authorization(권한, 허가)
  - 권한 부여
  - 인증된 사용자가 수행할 수 있는 작업을 결정
- 보통 Authentication과 Authorization을 합쳐서 authentication system(인증시스템)이라고 부름.
  - 배우는 내용은 Authentication만
- auth와 관련한 경로ㅇ나 키워드들을 Django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것을 권장

### Substituting a custom User model

- Django에서도 기본적인 user가 있지만 쓰지 않는게 권장되는 이유가
- email로 username으로 식별 값으로 쓰는 경우 등 **후에 변경하기 매우 어려움**. 그래서 Django에서 대체하고 시작하는걸 권장 함
  - **첫 migrate를 실행하기 전**에 이 작업을 마쳐야함

```python
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
# 이런식으로 일단 대체해놓고 시작해라 <- 권장사항
```

### 데이터 베이스 초기화

- 만일 프로젝트 중간에 변경해야 할 경우 데이터베이스를 초기화 한 뒤 진행하는 방법이 있음(프로젝트 중간일 경우)
- migrations 파일 삭제
  - migrations 폴더 및 **init**.py는 삭제하지 않음
  - 번호가 붙은 파일만 삭제
- db.sqlite3 삭제
- migrations 진행 : makemigrations, migrate

### How to substituting a custom User model
- Abstract base classes(추상 기본 클래스)
  - 왜 class로 안하고 굳이 상속 받아서 하냐?
    - 데이터베이스 테이블을 만들지 않게 하고, 다른 모델의 기본 클래스로 사용하여 찍어내기 위해서임
- 첫 makemigrations 이전에 작업하자(db가 만들어지기 전에)

# HTTP Cookies

### HTTP
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜(규칙,규약)
- requests & response(요청 & 응답)
- HTTP 특징
  - 비연결지향 : 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  - 무상태(stateless)
    -  연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
    -  클라이언트와 서버가 주고받는 메시지들은 서로 완전히 독립적임
    -  그럼 페이지 받은 뒤 로그인도 끊겨야하는데 유지됨 왜 유지될까?
       -  <- Cookies와 session이 역할을 수행함

### Cookie
- HTTP쿠키는 상태가 있는 세션을 만들도록 해줌
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각이다.
- 사용자가 웹사이트를 방문할 경우 해당 웹사이트의 서버를 통해 사용자의 컴퓨터에 설치되는 작은 기록 정보 파일
  - 브라우저(클라이언트)는 쿠키를 로컬에 KEY-VALUE의 데이터 형식으로 저장
  - 이렇게 쿠키를 저장해 놓았다가, 동일한 서버에 재요청 시 저장된 쿠키를 함께 전송
    - 나 로그인된 사용자야라는 쿠키를 요청할 때마다 매번 보냄(비연결지향인 HTTP를 바꿀 수는 없기 때문)
- 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용됨
  - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
  - 상태가 없는(stateless) HTTP 프로토콜에서 상태 정보를 기억시켜주기 떄문
- 즉, 웹 페이지에 접속하면 웹 페이지를 응답한 서버로부터 쿠키를 받아 브라우저에 저장 후 클라이언트가 같은 서버에 재요청시마다 요청과 함께 저장해 두었던 쿠키도 함께 전송
- 쿠키 사용 목적
  - 세션 관리(Session management)
    - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
    - 개인화(Personalization)
      - 사용자 선호, 테마 등의 설정
    - 트래킹(Tracking)
      - 사용자 행동을 기록 및 분석

### 세션 (session)
  - 사이트와 특정 브라우저 사이의 "state(상태)"를 유지시키는 것
  - 클라이언트가 서버에 접속하면 서버가 특정 session id를 발급하고, 클라이언트는 session id를 쿠키에 저장
    - 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달
    - 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 session id를 확인해 알맞는 로직을 처리
  - session id는 세션을 구별하기 위해 필요하며, 쿠키에는 session id만 저장

### 쿠키 Lifetime (수명)
  - Session cookie
     - 현재 세션(current session)이 종료되면 삭제됨
     - 브라우저 종료와 함께 세션이 삭제됨
  - Persistent cookies
    - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

### Session in Django
- Django는 database-backed sessions 저장 방식을 기본 값으로 사용
  - session 정보는 Django DB의 django_session 테이블에 저장
  - 설정을 통해 다른 저장방식으로 변경 가능(공식문서 참고)
- Django는 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session을 알아냄
- Django는 우리가 session 메커니즘(복잡한 동작원리)에 대부분을 생각하지 않도록 많은 도움을 줌
- 데이터는 서버가 가지고 있고, Key만 클라이언트에게 줌

# login
- python manage.py createsuperuser
  - 관리자계정생성
### AuthenticationForm
- 로그인을 위한 built-in form
  - 로그인 하고자 하는 사용자 정보를 입력 받음
  - 기본적으로 username과 password를 받아 데이터가 유효한지 검증
- request를 첫번째 인자로 취함
- login(request, user, backend=None)
- 인증된 사용자를 로그인 시키는 로직으로 view 함수에서 사용됨
- 현재 세션에 연결하려는 인증 된 사용자가 있는 경우 사용
- HttpRequest객체와 User객체가 필요

### get_user()
- AuthenticationForm의 인스턴스 메서드
- 유효성 검사를 통과했을 경우 로그인한 사용자 객체를 반환

# Authentication with User
- 현재 로그인 되어있는 유저 정보 출력하기
- 어떻게 base 템플릿에서 context 데이터 없이 user변수를 사용할 수 있는 걸까?
  - settings.py의 context processors 설정 값 때문

# logout
- 로그아웃은 Session을 Delete하는 과정
- logout(request)
- HttpRequest 객체를 인자로 받고 반환 값이 없음
- 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음
- 2가지 처리
  - 현재 요청에 대한 session data를 DB에서 삭제
  - 클라이언트의 쿠키에서도 sessionid를 삭제
  - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함

# 회원가입
- User를 create하는 것, UserCreationForm built-in form을 사용
- UserCreationForm
  - 주어진 username과 password로 권한이 없는 새 user를 생성하는 ModelForm
  - 3개의 필드를 가짐
    1. username(from the user model)
    2. password1
    3. password2
- 커스텀 유저 모델을 사용하려면 다시작성하거나 확장해야 하는 forms
  - UserCreationForm
  - UserChangForm
  - 두 form 모두 class Meta: model = user가 등록된 form이기 때문에 반드시 커스텀(확장)해야함

# Custom user & Built-in auth forms
### get_user_model()
- 현재 프로젝트에서 활성화된 사용자 모델(active user model)을 반환
- 직접 참조하지 않는 이유
  - 기존 User모델이 아닌 User모델을 커스텀 상황에서는 커스텀 User 모델을 자동으로 반환해주기 때문
- Django는 User 클래스를 직접 참조하는 대신 get_user_model()을 사용해 참조해야 한다고 강조

# 회원탈퇴
- DB에서 User를 Delete하는 것과 같음

# 회원정보 수정
- UserChangeForm
- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용하는 ModelForm
- UserChangeForm 또한 ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일
- *UserChangeForm 사용 시 문제점*
  - **일반 사용자가 접근해서는 안 될 정보들(fields)까지 모두 수정이 가능**해짐
    - admin 인터페이스에서 사용되는 ModelForm이기 떄문
  - 따라서 UserChangeForm을 상속받아 작성해 두었던 서브 클래스 CustomUserChangeForm에서 접근 가능한 필드를 조정해야함


**User와 Form의 View함수 구조는 똑같다.**

# 비밀번호 변경
### passwordChangeForm
- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스
- 암호 변경 시 세션 무효화 방지하기
  - 비밀번호가 변경되면 기존 세션과의 회원 인증 정보가 일치하지 않게 되어 버려 로그인 상태가 유지되지 못함
  - 비밀번호는 잘 변경되었으나 비밀번호가 변경 되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문
- update_session_auth_hash()
  -  update_session_auth_hash(request, user)
  -  현재 요청(current request)과 새 session data가 파생 될 업데이트 된 사용자 객체를 가져오고, session data를 적절하게 업데이트 해줌
  -  암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트


- 참고, 안전한 패스워드 저장 https://d2.naver.com/helloworld/318732
  - 안전한 패스워드 저장을 위해서 단방향 해시 함수를 많이 사용한다.(단방향 : 원본 메시지로는 암호화된 값을 알기 쉽지만 반대는 어려운 구조)
  - 하지만, 해시함수의 특성상 빠른 속성, 그리고 많은 표본을 가지고 있으면 보안성에 문제가 생길 수 있다.
  - 그래서 이를 보완하기 위해서 다음과 같은 방법들을 사용한다.(개인적인 방법은 가급적 사용하지 말자)
    - salting : 32바이트 이상일 시 salt와 다이제스트를 추측하기 어려움
      - 단방향 해시 함수에서 다이제스트를 생성할 때 추가되는 바이트 단위의 임의의 문자열을 password에 추가해 다이제스트를 생성하는 방법
    - key stretching
      - password를 다이제스트 생성을 일정 횟수만큼 반복해서 실행하는 것을 의미함. 이를 통해서 1초에 50억번 확인하는 것을 1초에 5번 정도로 확인 횟수를 줄일 수 있어서 공격하기 어렵게 만듦(컴퓨터 성능이 좋아지면, 그 만큼 반복 횟수를 증가시키면 됨)
    - 대안) Adaptive Key Derivation Functions
      - 다이제스트를 생성할 때 솔팅과 키 스트레칭을 반복하며 솔트와 패스워드 외에도 입력 값을 추가하는 방법
      - PBKDF2 : 가장 많이 사용되는 key derivation function
      - bcrypt
      - scrypt :  PBKDF2와 유사


# Limiting access to logged-in users
- 로그인 사용자에 대한 접근 제한하기
- 로그인 사용자에 대해 접근을 제한하는 2가지 방법
  - The raw way
    - **is_authenticated** attribute
  - The **login_required** decorator

### is_authenticated
- User model의 속성(attributes) 중 하나
- 사용자가 인증 되었는지 여부를 알 수 있는 방법
- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
  - AnonymousUser에 대해서는 항상 False
-  일반적으로 request.user에서 이 속성을 사용(request.user.is_authenticated)
-  **권한과는 관련이 없으며, 사용자가 활성화 상태이거나, 유효한 세션을 가지고 있는지도 확인안함**)
   -  순수 login 여부만 봄

### login_required
- django는 @login_required를 써줄 때 주소를 /accounts/login/ 로 보냄, 그래서 주소 맞춰줘도 좋음
- 뒤에 next=/이 있는 것은, 로그인하면 갈수 있게끔, 주소에 남겨두는것
- 하지만 넘어가지 못함 그래서 넘겨주고 싶으면 로그인 페이지에서 form안에 주소를 비어두면됨
- 그리고 result = request.Get.get('next')으로 처리를 하면 result를 받아줄 수 있음

### 두 데코레이터로 인해 발생하는 구조적 문제
login_required
require_POST가 같이 붙으면 안됨. why? login_required 뒤에 next가 get이기 떄문에 로직이 막힘
따라서 is_authenticated를 if문으로 써주고 login_required를 포기하면 됨.