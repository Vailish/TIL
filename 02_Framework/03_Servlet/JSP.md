# JSP
- Java Server Pages
- Servlet 표준을 기반으로 작성된 웹 어플리케이션 개발 언어
- 요청을 처리하고 응답을 구성하는 방법을 작성. 정적 요소 (HTML, XML 등) 와 동적 요소 (JSP객체)를 모두 포함하는 텍스트 기반 문서인 JSP페이지를 개발하기 위한 언어
- 서버측 객체에 접근하기 위한 표현 언어
- Servlet은 java코드 안에 html을 사용할 수 있게끔, JSP는 html안에 java코드를 쓸 수 있게끔 하는 것

## JSP 동작
![image](https://user-images.githubusercontent.com/109258380/210179382-e85e1af6-2772-471f-9ac7-38674adb927c.png)

## JSP 구성요소
- 지시자(Directive)
  - JSP 페이지에 대한 설정 정보를 지정하기 위해서 사용
- 스크립트 요소 : 스크립트릿(Scriptlet, <% %>), 표현식(Expression, <%= %>), 선언부(Declaration, <%! %>)
  - JSP에서 문서의 내용을 동적으로 생성하기 위해서 사용
- JSP 기본객체
  - 요청 및 응답 관련 정보를 얻거나, 응답 결과를 만들기 위해서 사용
- 표현언어(Expression Language, EL)
- Action Tag와 JSTL
  - 자주 사용하는 기능을 모아 미리 정의하여 Tag형태로 작성
  - JSP에서 자바코드를 쉽게 작성할 수 있도록 사용

## 지시자(Directive)
- 웹 컨테이너(톰캣)가 JSP를 번역하고 실행하는 방법을 서술
- 대표적으로 page, include, taglib 와 같은 디렉티브가 있음
- page 지시자
  - JSP 페이지 실행 매개변수를 제어
  - 출력 처리, 오류 처리 등의 내용을 포함
  - 주요 속송으로, language, contentType, import, session, pageEncoding, errorPage, autoFlush 등이 있음
```jsp
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
```

## page지시자
![image](https://user-images.githubusercontent.com/109258380/210179670-1d426623-712f-41d6-bc9d-6a102c3979cc.png)
![image](https://user-images.githubusercontent.com/109258380/210179702-05550194-907a-4813-8330-1846359b79f6.png)

## 지시자(Directive)
- include 지시자
  - JSP 내에 다른 JSP 페이지를 포함하기 위해서 사용. 반복적으로 사용되는 부분(header, footer등)을 별도로 작성하여 페이지 내에 삽입하여 반복되는 코드의 재작성을 줄일 수 있음
```jsp
<%@ include file="/template/header.jsp" %>
```

- taglib 지시자
  - JSTL 또는 사용자가 작성한 커스텀 태그를 사용할 때 작성. 불필요한 자바 코드를 줄일 수 있음
```jsp
<%@ taglib url="http://java.sun.com/jsp/jstl/core" prefix="c" %>
```

## 스크립트 요소
- JSP 페이지 내에서 프로그래밍에서 로직을 수행하는데 사용
- 선언부(Declaration)
  - 멤버 변수 선언이나 메서드를 선언하는 영여거
  - 형식 <%! 스크립팅 언어 선언 %>
  - ex)
```jsp
<%!
String name = "Vailish";
public int add(int a, int b){
    return a + b;
}
%>
```
## 스크립트 요소
- 스크립트릿(Scriptlet)
  - 스크립팅 언어(java)로 작성된 코드 조각을 포함하는데 사용
  - 형식 및 예
```jsp
<% 
    scripting-language-statements
%>
```
```jsp
<%
    String username = request.getParameter("username");
    if ( username != null && username.length() > 0) {
%>
    <%@include file="response.jsp" %>
<%
    }
%>
```
- !표가 있을 때가 밖에서 선언하는 거기 때문에 사용에 문제가 없고, !를 붙이지 않으면 그냥 내부에서 쓰는거기 때문에 원하는데로 작동하지 않을 수 있음
- 예시 Back03_JSP/~/add.jsp