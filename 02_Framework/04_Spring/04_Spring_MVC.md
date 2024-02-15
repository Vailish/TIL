# Spring MVC - 요청 처리 흐름
1. 클라이언트 요청이 들어오면 DispatcherServlet이 받음
2. HandlerMapping이 어떤 Controller가 요청을 처리할 지 결정
3. DispatcherServlet은 Controller에 요청을 전달
4. Controller는 요청을 처리
5. 결과(요청처리를 위한 data, 결과를 보여줄 view의 이름)를 ModelAndView에 담아 반환
6. ViewResolver에 의해서 실제 결과를 처리할 View를 결정하고 반환
7. 결과를 처리할 View에 ModelAndView를 전달
8. DispatcherServlet은 View가 만들어낸 결과를 응답

# eGovFramework(SpringMVC)를 통한 Spring 구조 파악
## Web.xml
- web.xml은 웹어플리케이션의 시작이자 설정 파일
- Deployment Descriptor(DD)라고도 불림
- 크게 3가지 기능 설정을 함
    - DispatcherServlet
    - ContextLoaderListener
    - Filter

## servlet 버전 설정
```xml
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee" 
		 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		 xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
		 version="3.1">
```
## annotaion
### @ResponseBody
- Json 기반의 HTTP Body를 자가 객체로 변환
- Jackson view를 사용

### 참고자료
- [공식문서 - Spring.io - @ResponseBody](https://docs.spring.io/spring-framework/reference/web/webflux/controller/ann-methods/responsebody.html)

## Spring Session
- 스프링 프레임워크에서 제공하는 모듈 중 하나로 기존의 HttpSession 을 대체
- 분산된 스케일링 가능한 환경에서 세션 데이터를 관리
- 외부 저장소를 사용하게끔 하여 서블릿 컨테이너에서 세션 데이터를 분리할 수 있도록 도와줌
- 애플리케이션 퍼포먼스 향상과 분산 환경에서 세션 관리가 쉬워진다는 장점

### HttpSession?
- [블로그 - 톰캣에서 지원하는 HttpSession 이란? (feat. Servlet API)](https://jake-seo-dev.tistory.com/495#%EC%--%B-%EC%--%--%--%EC%--%-D%EC%--%B-%---Session%--Creation-)
- web.xml `<session-config>`에서 시간을 설정할 수 있음(분)
- encodeURL은 말그대로 쿠키를 사용할 수 없을 때 (가능할 때는 쿠키를 통해서 정보를 확인함, `jssesionId`)
- setAttribute()와 getAttribue()를 사용하여 사용 가능

# 어노테이션
- @SuppressWarnings : 경고 제거(노란 밑줄)

- @Resource : Name으로 Bean을 지정한다.(필드/메서드에만 적용 가능)
    - vs @Autowired : 타입(클래스)로 Bean을 지정한다.(생성자/필드/메서드에 모두 적용 가능)

```java
@Repository
public class CommonDao {
    @Autowired
    private SqlSessionTemplate sqlSession;
}

@Repository
public class TestDao {
    @Resource(name="BlueSqlSessionTemplate")
    private SqlSessionTemplate sqlSession;
 }
```

# Mybatis - nfu
데이터베이스 조작시 commonService에서 원하는 리턴값을 선택해서(selectList, selectObject, 등등) sqlid를 보내면 src/main/resources/egovframework/sqlmap에 해당하는 xml파일의 id의 쿼리문을 실행시켜서 작동함

# Mybatis - include, sql 사용법
- sql : id를 정해줘서 해당 쿼리를 재활용할 수 있게 하는 태그
- include : 미리 선언해두고 가져와 사용할 때 사용하여 가져온 쿼리를 붙여 재활용성을 높이는 태그
    - sql태그를 활용하여 id를 위에 미리선언, 사용할 때 include 태그를 통해 refid를 통해 가져올 id를 사용
- parameterType : 구문에 전달될 파라미터의 패키지 경로를 포함한 전체 클래스명이나 별칭
- resultMap : 외부 resultMap을 반환타입으로 참조
- resultType : 리턴되는 기대타입의 패키지 경로를 포함한 전체 클래스명이나 별칭
- https://kimvampa.tistory.com/176 / https://yermi.tistory.com/entry/MyBatis-MyBatis-SQL-select-%EB%A7%88%EC%9D%B4%EB%B0%94%ED%8B%B0%EC%8A%A4%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A1%B0%ED%9A%8C%ED%95%98%EA%B8%B0 : 블로그
- https://mybatis.org/mybatis-3/ko/sqlmap-xml.html : 공식문서

# query 조건에 where 1=1 사용하는 이유
1. 주석처리하기 쉽다.
2. 추가 조건이 붙을 때 처리하기 쉽다. -> 뒤에 조건만 and로 붙여주면 되기 때문
"select * from table1 where 1=1" 이면 뒤에 "and a>5" 이런식으로, 없다면 뒤에 조건이 있었다면 and를 없었다면 where을 붙이고 조건을 써야 하기 때문에
- 참고 https://hyjykelly.tistory.com/5


# HttpServletResponse
- getWriter() : 화면단에 출력할때 사용

# jstl
- JSTL은 JSP 표준라이브러리(JSP Standard Tag Library)의 약어이다. 자주 사용될 수 있는 커스텀 태그들을 모아서 표준으로 모아놓은 태그 라이브러리다.
- foreach 문의 상태용 변수를 설정할 수 있음
- ```js
    <c:foreach items="${리스트가 받아올 배열이름}"
    var="for문 내부에서 사용할 변수"
    varStatus="상태용 변수">
        </c:foreach>
    ```
- ${status.method}
    - current 현재 for문의 해당하는 번호
    - index 0부터의 순서
    - count 1부터의 순서
    - first 첫 번째인지 여부
    - last 마지막인지 여부
    - begin for문의 시작 번호
    - end for문의 끝 번호
    - step for문의 증가값
- https://devlogofchris.tistory.com/47
- https://jetalog.net/20


# servlet
- https://kimcomdong.tistory.com/140

# 이클립스 추가기능
- XML 파일볼때 하단의 Design(도표양식) / Source(돔형식)로 보는 양식을 변경할 수 있음
- ![xml이미지](참고자료/images/Design_Source.png)

# OG 타입
- https://seons-dev.tistory.com/entry/html-Meta-OG

# SpringMVC에서 클라이언트 ip주소 가져오기
- request.getRemoteAddr();
```java
   @RequestMapping("/login.do")
    private ModelAndView doLogin(@Valid LoginVO loginVO, BindingResult result,
            RedirectAttributes redirect, HttpServletRequest request, HttpServletResponse response) throws Exception {
        /*
         * 로그인 처리 SVC 호출
         * */
        loginVO.setLoginIp(request.getRemoteAddr());
        String loginRslt = loginSvc.doLogin(loginVO);
        /*
         * 분기
         * Login성공
         * */
        if(loginRslt.equals(StaticStringUtil.USER_LOGIN_SUCCESS)){
            return new ModelAndView("redirect:/moveMain.do");
        }else{
            return new ModelAndView("login/login", "loginErr", loginRslt);
        }
        
    }
```
- https://www.leafcats.com/35