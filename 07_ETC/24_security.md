# 정보보호 보안의 개념 / 웹보안

## 정보보호의 개념
### 정보보호의 개념
- 정보의 수집, 가공, 저장, 검색, 송신 중에 정보의 훼손, 변조, 유출 등을 방지하기 위한 관리적, 기술적 수단, 또는 그러한 수단으로 이루어 지는 행위

### 정보보호 대책
- 관리적 보호 대책 : 제도, 보안교육, 훈련, 보안직무
- 물리적 보호 대책 : 출입통제, 재난방지
- 기술적 보호 대책 : 네트워크 접근 통제, 보안소프트웨어, 방화벽
- 정보보호 - 기업의 정보자산

# 웹보안 강화
1. 사이트 보안
2. 웹서버 보안
3. 웹 방화벽(WAF)

## 사이트 보안
- 파일 업로드 취약점
- XXS(Cross Site Scripting)
- SQL Injection

### 파일 업로드 취약점
- 게시판 등의 첨부파일 기능을 이용해 허가되지 않은 파일들을 웹서버로 업로드 할 수 있는 취약점(php, jsp, asp, cgi, js, py등)

### 파일 업로드 취약점 예방
- 파일 업로드 디렉토리 "실행"권한 제거
- 허용되지 않은 확장자 업로드 제한

```httpd.conf
<Directory "/user/local/apache">
  AllowOverride FileInfo
</Directory>
```

```.htaccess
<FilesMatch "\.{ph|inc|lib}">
  Order allow, deny
  Deny from all
</FilesMatch>

AddType text/html .html .htm .php .php3 .php4 .phtml .phps /in ~~~~~~기타~~~~~~~~~~
```

### XSS(Cross Site Scripting)
- 홈페이지 접속자의 권한 정보를 탈취하거나 악성코드 감염을 유발할 수 있는 취약점

### XSS 예방
- XSS 필터 라이브러리 사용
- X-XSS-Protection 응답 헤더 사용
- 문자열 치환(`<>&" 등을 &It; &gt; &amp; &quot;로 치환`)

- spring의 경우
- XSS Filter Library
  - ESAPI : XSS등 웹어플리케이션 시큐어코딩 라이브러리, 문자열 기반 유효성 검사
  - Lucyxss filter : 자바 서블릿 기반 필터, XML 설정만으로 세팅 가능
  - 
```httpd.conf
Header.set X-XSS-Protection "1; mode=block"
```
```nginx.cof
add_header X-XSS-Protection "1; mode=block;"
```

### SQL Injection
- 게시판, 회원가입 창, URL 등을 통해 부적절한 값을 삽입하여 DB데이터를 빼내거나 로그인 절차 우회 등 비정상 동작을 유발

### SQL Injection 예방
- 시큐어 코딩(`; -- # /* */ 등 입력내용 필터링)
- 웹 방화벽(Web Application Firewall, WAF) 구축
- PreparedStatement : 값을 바인딩하는 시점에서 전달된 특수문자 쿼리 등을 필터링하여 sql injection을 막는다.
```
preparedStatement = "SELECT * FROM users WHERE name = '" + userName + "';";

# If someone put
' or '1'='1'

# Result
SELECT * FROM users WHERE name = '' OR '1' = '1';

preparedStatement = "SELECT * FROM users WHERE name = ?";
preparedStatement.setString(1, userName);

# If someone puts
' or '1'='1'

# Result
SQL FIND name : ' or '1'='1
```

## 웹 서버 보안
- 계정관리
- root계정의 PATH 환경변수 설정
- 서비스 관리

### 계정관리
- root 계정 원격 접속 제한
- 로그인 실패 임계값 설정
- 패스워드 복잡도 설정

- Root 계정 원격 접속 제한
- Telnet 원격접속 차단
```
vi /etc/securetty
pts/0 ~ pts/x 설정 제거

vi /etc/pam.d/login
# auth required /lib/security/pam)security/pam_securetty.so #제거(주석제거)
auth required/lib/security/pam_securetty.so
```
- SSH 원격접속 차단
```
vi /etc/ssh/sshd_config
"PermitRootLogin no" 설정
```

### root 계정의 PATH 환경변수 설정
- PATH에 디렉토리 경로보다 "."(현재 디렉토리)가 먼저오면, 변조된 명령어 삽입으로 악의적인 기능이 실행될 수 있음

```
# vi 편집기를 이용하여 root 계정의 설정파일(~/.profile 과 /etc/profile) 열기

vi /etc/profile 또는 vi /etc/environment

(Before) PATH=.:$PATH:$HOME/bin
(After) PATH=$PATH:$HOME/bin:.
```

### 서비스 관리
- Apache, Nginx 등 잘못된 보안 설정으로 발생 할 수 있는 비인가자의 원격접속, 정보 노출 등을 제한하는 것을 목적으로 한다.
- Directory Listing: 설정된 모든 Directory 옵션 지시자에서 Indexes 제거
- httpd.conf
```
<Directory />
  #Options Indexes
  AllowOverride None
  Order allow, deny
  Allow from all
</Directory>
```

### 웹 방화벽(WAF)
- L7(OSI 7 Layers)에서 보안 유지
- SQL Injection, XSS 등 웹 공격 탐지, 차단
- DDOS, IP 차단, Rate limit등 규칙 생성

# AWS 보안가이드
- AWS 계정 보호하기 위한 모범 사례
- 목차
  - 개요 - 클라우드 장점과 보안
  - 사고 사례 - 클라우드 보안 사고 사례와 시사점
  - 모범 사례 - 계정 보안 문제를 피하는 모범 사례

## 개요 - 클라우드 장점과 보안
### 클라우드의 장점
- 초기 선투자 비용 없음 : 고정비용을 가변비요으로 대체 미리 서버를 구매할 필요 없음
- 운영 비용 절감 : 사용한 만큼만 지불하며 규모의 경제로 인한 지속적인 비용 절감
- 탄력적인 운영 및 확장 : 필요 용량에 대한 예측 불필요 수요에 맞춘 유연한 확장
- 속도 및 민첩성 : 수 분 만에 인프라 구축 가능, 빠르게 변화에 대응
- 비즈니스에만 집중 가능 : 혁신을 위한 다양한 실험 가능, 불필요한 인프라 관리 업무 제거
- 글로벌 확장 : 빠른 시간 내 글로벌 서비스 구현 가능

### 사고 사례 - 주요 사고 사례
- 계정 해킹
- 데이터(개인정보) 유출
- 복구 실패(랜섬웨어)

### 사고 사례 - 시사점
- 계정 보안에 대한 책임은 사용자 본인에게 있다
- 예방 : MFA 활성화, AWS Access Key 보호
- 리스크 관리 : ROOT 사용자 보안강화, IAM 사용자를 통한 관리
- 감지 : 비용 관련 알림 설정

### 모범 사례 - MFA 활성화
- Multi-Factor Authentication
- 일반적으로 Authenticator app 사용
  - Google OTP, Twilio Authy, Microsoft Authenticator

### 모범 사례 - AWS Access Key 보호
- AWS CLI나 API 사용시, 인증을 위해 사용되는 자격 증명
- 엑세스 키 ID와 보안 액세스 키로 구성
- 가이드
  - 주기적인 Access Key 교체 및 미사용 Key 제거
  - 어플리케이션별 최소 권한 적용
  - GitHub등에 Commit시 주의
  - git-secrets등을 활용한 Access Key 암호화 및 보호

### 모범 사례 - ROOT 사용자 보안 강화
- ROOT 사용자
  - AWS 계정 생성시 사용한 이메일주소와 패스워드로 인증하는 계정
  - 모든 권한을 지니고 있으며, 권한 제약 설정이 불가능
- 가이드
  - 평상시에는 미사용
  - Access Key 생성 금지
  - 비밀번호 정책 강화
  - MFA 활성화

### 모범 사례 - IAM 사용자를 통한 관리
- AWS Identity and Access Management
  - AWS리소스에 대한 엑세스를 안전하게 제어할 수 있는 서비스
  - 사용자 및 그룹별 인증 및 권한 부여를 통하여, AWS 리소스에 대한 액세스를 안전하게 제어
- 가이드
  - 개별/용도별 사용자 생성
  - 그룹을 통한 권한 관리
  - 비밀번호 정책강화

### 모범 사례 - 비용 관련 알림 설정
- 이메일 정보 업데이트
  - 자주 쓰는 이메일로 설정 및 확인
- Free Tier 한도 초과 경보 생성
  - Free Tier한도 초과시 메일이나 SMS 설정
- 월별/실시간 예상 요금 경고 생성
  - Amazon CloudWatch를 이용한 월간 예상 AWS 요금 알림 설정
  - AWS Chatbot을 사용한 Slack에서 예산 알림 수신

### 참고 - 계정 침해시, 후속조치
- AWS Support 센터에 Case 등록
- AWS 가이드에 따라, 후속 조치
  - 무단으로 생성된 비정상 리소스 삭제
  - 전체 사용자(Root 및 IAM 사용자) 암호 변경
  - 모든 AWS Access Key 교체 및 삭제



