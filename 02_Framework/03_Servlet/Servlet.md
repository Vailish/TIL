# Web-BackEnd
- Servlet
- JSP

# Servlet
## 웹과 웹 프로그래밍
- URL (Uniform Resource Locator) - 웹 상의 자원을 참조하기 위한 웹 주소
- 웹 페이지 (Web page) - 웹 브라우저를 통해서 보여지는 화면
- 웹 서버 (Web Server) - 클라이언트 요청에 맞는 응답(웹 페이지)을 제공
- 웹 어플리케이션 (Web Application) - 웹 서버를 기반으로 실행되는 응용 소프트웨어
- 웹 어플리케이션 서버 (Web Application Server, WAS) - 요청이 오면 알맞은 프로그램을 실행하여 응답을 만들고 제공하는 서버

## Web Architecture
![image](https://user-images.githubusercontent.com/109258380/210078264-868c4396-0877-4fc0-81b4-2495290eeb7a.png)
- client == 브라우저
- WAS(Web Application Server)은 tomcat(오픈소스)사용

## Eclipse 톰켓 연결
- 이클립스 -> 하단 servers -> 톰켓 등록

## Servlet(서블릿)
- 자바를 사용하여 웹페이지를 동적으로 생성하는 서버측 프로그램 혹은 그 사양
- 웹 서버의 성능을 향상하기 위해 사용되는 자바 클래스의 일종
- 웹 기반 응용 프로그램을 구축하기 위한 구성 요소 기반의 플랫폼 독립적 방법을 제공
- 대화형 웹 응용 프로그램을 구축하는 데 널리 사용
- JSP와 비슷한 점이 있지만, JSP가 HTML문서 안에 Java 코드를 포함
- 서블릿은 자바 코드 안에 HTML을 포함

## Servlet 생명주기
- 서블릿 인스턴스는 서블릿이 포함된 웹컨테이너에 의해 제어된다.
- 서블릿 인스턴스가 존재하지 않으면 다음과 같은 작업을 수행한다.
  1. 서블릿클래스 로드
  2. 서블릿 클래스 인스턴스 생성
  3. 서블릿 인스턴스 초기화
  4. 웹 컨테이너에 의한 서비스 메서드 호출
  5. destroy 메서드를 호출하여 서블릿 종료
- 서비스 메서드는 요청이 들어올 때 마다 호출된다.

![image](https://user-images.githubusercontent.com/109258380/210078919-9e772c67-678b-4ad5-91be-8ded2fa8acba.png)

## Servlet API
```java
Class HttpServlet

java.lang.Object
    javax.servlet.GenericServlet
        Javax.servlet.http.HttpServlet

All Implemented Interfaces:
Serializable, Servlet, ServletConfig
////////////////////////////////////
public abstract class HttpServlet
extends GenericServlet
```

## Servlet 작성
- HttpServlet을 상속하는 클래스는 다음 중 적어도 하나의 메서드를 재정의 해야 함

|메서드|설명|
|------|---|
|doGet()|HTTP GET 요청 처리시 작성|
|doPost()|HTTP POST 요청시 작성|
|doPut()|HTTP PUT 요청시 작성|
|doDelete()|HTTP DELETE 요청시 작성|
|init(), destroy()|서블릿 수명 동안 보유되는 리소스 관리|

## GET과 POST
|GET|POST|
|------|---|
|지정된 리소스에서 데이터를 요청하는 데 사용|리소스를 생성/업데이트하기 위해 서버에 데이터를 보내는데 사용|
|query string(name/value 쌍)이 URL에 포함되어 전송됨. POST와 비교하여 보안에 취약함|HTTP header의 body에 파라미터를 포함하여 전송, 데이터 길이에 대한 제한 없음, 매개변수가 브라우저나 웹 서버에 저장되지 않음|
|URL이 길이 제한이 있으므로, 전송가능한 데이터의 길이가 제한적(URL maximum characters: 2048), ASCII 문자만 가능|제한 없음. 바이너리 데이터도 허용|

# URL 구성요소
- https://www.google.com/search?q=vailish
- https: 프로토콜
- www.google.com URL
- (context root)
- search 경로
- q=vailish Query String
- 프로토콜 : 웹 브라우저가 서버와 통신하기 위한 규약
- 서버 : 웹 페이지를 요청할 서버의 주소, 실제 IP주소나 도메인을 입력할 수 있음
- 경로 : 서버 내의 상세 경로
- 쿼리 스트링 : 추가로 서버로 데이터를 전송하기 위해서 사용, '?'마크를 적어 시작을 표시, parameter_name=value형태로 작성하며 여러개 일 경우 '&'로 구분하여 작성