# REST API
- HTTP
- REST API
- Response JSON
- Django REST framework - Single Model
- Django REST framework - N:1 Relation

# HTTP
- HyperText Transfer Protocol
- HTML 문서와 같은 resource(HTTP 요청의 대상, 자원)들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
- 웹 상에서 컨텐츠를 전송하기 위한 약속
- 웹에서 이루어지는 모든 데이터 교환의 기초가 됨
- 'Client-Server protocol'라고도 부름
- 클라이언트와 서버는 다음과 같은 개별적인 메시지교환에 의해 통신
  - Request(요청) : 클라이언트에 의해 전송되는 메시지
  - Response(응답) : 서버에서 응답으로 전송되는 메시지
- 위 사항은 기본 명세, 기타 심화내용 존재

## HTTP 특징
- Stateless(무상태)
  - 동일한 연결(connection)에서 연속적으로 수행되는 두 요청 사이에 링크가 없음
  - 즉, 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
- 이는 특정 페이지와 일관되게 상호작용 하려는 사용자에게 문제가 될 수 있으며, 이를 해결하기 위해 쿠키와 세션을 사용해 서버 상태를 요청과 연결하도록 함

## HTTP Request Methods
- 리소스에 대한 행위(수행하고자 하는 동작)를 정의
- 즉, 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의
- HTTP verb 라고도 함
- ex)
  - GET : 서버에 리소스의 표현을 요청, `데이터만 검색`
  - POST : 데이터를 지정된 리소스에 제출, `서버의 상태를 변경`
  - PUT : 요청한 주소의 리소스를 수정
  - DELETE : 지정된 리소스를 삭제
  - ...

# HTTP response status codes
- 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
- 응답은 5개의 그룹으로 나뉨
  1. Informational responses(100-199)
  2. Successful response(200-299)
  3. Redirection message(300-399)
  4. Client error responses(400-499)
  5. Server error responses(500-599)

# Identifying resources on the Web
- 각 리소스는 식별을 위해 URI로 식별됨

## URI
- Uniform Resource Identifier(통합 자원 식별자)
- 인터넷에서 하나의 리소스를 가리키는 문자열
- 가장 일반적인 URI는 웹주소로 알려진 URL
- 특정 이름공간에서 이름으로 리소스를 식별하는 URI는 URN
  - ex) urn:isbn:9788937461736 (ISBN국제표준도서 에서 식별되는 '로미오와 줄리엣'도서의 URN)

## URL
- Uniform Resource Locator (통합 자원 위치)
- 웹에서 주어진 리소스의 주소
- 네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속, 이러한 리소스는 HTML, CSS, 이미지 등
- URL은 다음과 같이 여러 부분으로 구성되며 일부는 필수, 나머지는 선택사항
  - ex) https://www.example.com:80/path/to/myfile.html/?key=value#quick-start
  
- URL 구조
  - Authority




# REST API

# Response JSON

# Django REST framework - Single Model

# Django REST framework - N:1 Relation

