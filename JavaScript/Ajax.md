# Java Script
- DOM
- Event
- this

# DOM
- 브라우저에서의 JavaScript
  - 웹 페이지에서 복잡한 기능을 구현하는 스크립트 언어
  - 가만히 정적인 정보만 보여주는 것이 아닌 주기적으로 갱신되거나, 사용자와 상호작용이 가능하거나, 애니메이션이 적용된 그래픽 등에 관여
  - Script Language(스크립트 언어)
    - 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어
- Browser APIs
  - 웹 브라우저에 내장된 API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용한 ~~~~~


# this
1. 전역에서 window
2. 함수 -> 함수 : window
        -> 메서드 : 앞 객체 (.앞 객체)
3. bind를 통한 명시
4. 화살표 함수는 상위의 this
5. 콜백함수에서의 this는 각각 다름
    - 콜백함수는 제어권을 넘겨준 함수 ex) setTimeout(func, 5000), 알람 - 제어권이 시계한테 있음
    - 함수로 호출하면 전역객체(window) - 콜백함수도 함수임!
    - 메서드로 호출하면 앞 객체(.(dot) 앞의 객체)
    - addEventListener : this가 이벤트가 발생하는 녀석을 가리킴, 그래서 화살표함수 사용하지말자, 화살표 함수를 사용하면 상위객체(window)를 가리키기 때문에

# JavaScript
INDEX
- 동기와 비동기
- JavaScript의 비동기 처리
- Axios 라이브러리
- Callback & Promise
- AJAX

## 동기와 비동기
- task를 줄 때, 한 명씩 다 주는 게 아니라 조금씩 한 명씩 주는데 이걸 빠르게 하면 동시에 주s는 것 처럼 보인다. : Javascript의 비동기성 원리


## PROMISE
- javascript를 비동기 방식으로 사용하다보니... 순서가 보장되지 않는다.. 그래서 callback 함수안에 넣어서(앞의 데이터에 의존) 순서를 보장하기로했었다.. 이로 인해 callback hell이 만들어져서 불편함을 감수하고 있었다.
- 이러한 콜백지옥을 해결하기 위해서 순서가 보장된 PROMISE가 등장하게 되었다.
- PROMISE
  - then, 정상적인 코드
  - catch, 에러코드

## AJAX (Asynchronous JavaScript And XML)
- 