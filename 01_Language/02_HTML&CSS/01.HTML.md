# Web
## HTML & CSS
- 웹
  - 웹 표준과 크로스 브라우징
  - 개발 환경 설정
- HTML
  - HTML 기본구조
  - HTML 문서 구조화
- CSS
  - CSS Selectors
  - CSS 단위
  - Selectors 심화
  - Box model
  - Display
  - Position

### Web
- 웹 사이트의 구성 요소
  - 웹 사이트란 브라우저를 통해서 접속하는 **웹 페이지(문서, text)**들의 모음
  - 웹페이지는 글, 그림, 동영상 등 여러가지 정보를 담고 있으며, 마우스로 클릭하면 다른 웹 페이지로 이동하는 '링크'들이 있음. '링크'를 통해 여러 웹 페이지를 연결한 것을 웹 사이트라고 함.
  - HTML -> 구조
  - CSS -> 표현
  - Javascript -> 동작
- 웹 사이트와 브라우저
  - 웹 사이트는 브라우저를 통해 동작
    - ex) Chrome, Edge, Firefox, etc
  - -> 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많음(파편화)
  - -> 해결책으로 웹 표준이 등장
- 웹 표준
  - 웹에서 표준적으로 사용되는 기술이나 규칙
  - 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)
  - ex) WSC 팀 버너스리 : 1994년에 설립, 약 437개 회원사
  - ex) WHATWG HTML Living standard : Apple, Google, Microsoft, Mozilla <- html 5
  - Can I use? : 검색하면 브라우저별 호환성 체크 가능
    - 붉은색은 불가
    - 노란색은 불확실
    - 녹색은 가능

### 개발 환경 설정
- Visual studio code
  - HTML/CSS 코드 작성을 위한 Visual Studio code 추천 확장 프로그램
    - Open in browser
    - Auto rename tag
    - Highlight Matcing Tag
- 크롬 개발자 도구
  - 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공
  - 주요기능
    - Elements - DOM 탐색 및 CSS 확인 및 변경
      - Styles - 요소에 적용된 CSS 확인
      - Computed - 스타일이 계산된 최종 결과
      - Event Listeners - 해당 요소에 적용된 이벤트(JS)
    - Sources, Network, Performance, Application, Security, Audits 등

### HTML
- HTML
  - 요소 == 태그 + 내용
    - 인라인요소(inline) : 내용만큼 장소?를 가지고 있는 것
    - 블록요소(block)
  - 속성 == 이름 + 값
- CSS 삭제 시 HTML만 남은 웹 사이트 확인 가능 <- 렉걸릴때 가끔 글만 나열되는 현상이랑 같음
- HTML : Hyper Text Markup Language, 웹 페이지를 작성(구조화)하기 위한 언어
  - Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
  - Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
    - ex) HTML, Markdown
  - .html : HTML파일
  - HTML 스타일 가이드 (2 space) cf) python 4 space
```
    - ex) 마크업 스타일 가이드
    - <body>
    -   <h1> 웹문서 </h1>
    -   <ul>
    -     <li>HTML</li>
    -     <li>CSS</li>
    -   <ul>
    - </body>
```


##### HTML 기본 구조
- HTML 기본구조
  - html : 문서의 최상위(root) 요소 <-주소창쪽
  - head : 문서 메타데이터 요소 (<- 사진에 대한 메타 데이터면, 찍은 시간, 장소 등등 포함)
    - 문서 제목, 인코딩, 스타일, 외부파일 로딩 등
    - 일반적으로 브라우저에 나타나지 않는 내용
  - body : 문서 본문 요소
    - 실제 화면 구성과 관련된 내용
  - head 예시
```
    - <title> : 브라우저 상단 타이틀 <- 텝 이름
    - <meta> : 문서 레벨 메타데이터 요소
    - <link> : 외부 리소스 연결 요소(CSS 파일, favicon 등)
    - <script> : 스크립트 요소(Javascript 파일/코드)
    - <style> : CSS 직접 작성
    - Open Graph Protocal (카톡 같은곳에 링크 주면 뜨는 이미지 같은것)
      - 메타 데이터를 표현하는 새로운 규약, META(구 facebook)에서 처음 만듦
        - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
        - 메타 정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
```
- 요소(element) == 태그(tag) + 내용(content)
  - HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
    - 요소는 태그로 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
    - ex) ```(여는/시작) 태그 -> <h1> contests </h1> <-(닫는/종료)태그```
    - 내용이 없는 태그들도 존재(닫는 태그가 없음)
      - br, hr, img, input, link, meta
  - 요소는 중첩(nested)될 수 있음 <- 태그 안에 태그 가능
    - 요소의 중첩을 통해 하나의 문서를 구조화
    - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
      - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, <u>디버깅이 힘들어 질 수 있음</u>
- HTML with 개발자 도구
  - elements : 해당 요소의 HTML 태그
  - 우클릭 -> 검사 -> 원하는 요소를 선택해서 HTML 구조를 탐색가능
- 속성(attribute)
```- <a herf="https://google.com"></a>``` <- herf : 속성명, "" : 속성값
  - (herf=여기서 =앞뒤로 **공백X**, ""사용)
  - 속성 지정 스타일 가이드 : 태그별로 사용할 수 있는 속성은 다름
  - 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
  - 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
  - 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
  - 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음
  - HtML Global Attribute
    - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇몇 요소에는 아무 효과가 없을 수 있음)
      - **id** : 문서 전체에서 유일한 고유 식별자 지정
      - **class** : 공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근)
      - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용 <- 좋아요 기능
      - **style** : inline 스타일
      - title : 요소에 대한 추가 정보 지정
      - tabindex : 요소의 탭 순서 <- 사이트에서 텝을 누르면 선택이 되는 순서
- 시맨틱 태그
  - HTML 태그가 특정 목적, 역할 및 의미적 가치(semantic value)를 가지는 것
    - ex) h1 태그는 "이 페이지에서 최상위 제목"인 텍스트를 감싸는 역할(또는 의미)을 나타냄
  - Non semantic 요소로는 div, span 등이 있으며, a, form, table 태그들도 시맨틱 태그로 볼 수 있음
  - HTML5에서는 기존에 단순히 컨텐츠의 구획을 나타내기 위해 사용한 div 태그를 대체하여 사용하기 위해 의미론적 요소를 담은 태그들이 추가됨
  - 시맨틱 태그을 사용함으로 인해서 구조를 잘 알수가 있게 되고 이에 따라서 읽어주는 등 서비스 개발을 하기 수월하게 해줌
  - 대표적인 태그 목록
  - header : 문서 전체나 섹션의 헤더(머리말 부분)
  - nav : 내비게이션
  - aside : 사이드에 위치한 공간, 메인 컨텐츠와 관련성이 적은 컨텐츠
  - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - footer : 문서 전체나 섹션의 푸터(마지막 부분)
  - 시맨틱 태그를 사용해야 하는 이유
    - 의미론적 마크업
      - 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
      - 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
      - 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
      - 검색 엔진 최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해아함
- 렌더링(Rendering)
  - 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정 <- 브라우저가 수행
- DOM(Document Object Model) 트리
  - 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
    - HTML 문서에 대한 모델을 구성함
    - HTML문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함
  - 자바스크립트 객체 같은 것으로 각각 요소별(head, body 등등)로 잘라서 그려줌
  - ex)
```
- document
    - Root element <html>
        - Element <head>
            - Element <title>
                - Text "My title"
    - Element <body>
        - Element <h1>
            - Text "A heading"
        - Element <a> - Attribute: href
            - Text "Link text"
```

##### HTML 문서 구조화
```
- 인라인 / 블록 요소
  - HTML 요소는 크게 인라인 / 블록 요소로 나눔
  - 인라인 요소는 글자처럼 취급
  - 블록 요소는 한 줄 모두 사용
  - ex) <태그> 내용 </태그>
- 텍스트 요소
  - <a></a> : href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
  - <b></b> : 굵은 글씨 요소, 중요한 강조하고자 하는 요소(보통 굵은 글씨로 표현)
    <strong></strong>
  - <i></i> : 기울임 글씨 요소, 중요한 강조하고자 하는 요소(보통 기울임 글씨로 표현)
    <em></em>
  - <br> : 텍스트 내에 줄 바꿈 생성
  - <img> : src 속성을 활용하여 이미지 표현
  - <span></span> : 의미 없는 인라인 컨테이너
- 그룹 컨텐츠
  - <p></p> : 하나의 문단(paragraph)
  - <hr> : 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨(A Horizontal Rule)
  - <ol></ol> : 순서가 있는 리스트(ordered) ex) 1.~ 2.~ 3.~
    <ul><ul> : 순서가 없는 리스트(unordered) ex) -~ -~ -~
  - <pre></pre> : HTML에 작성한 내용을 그대로 표현. 보통 고정폭 글꼴이 사용되고 공백문자를 유지
  - <blockquote></blockutote> : 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨
  - <div></div> : 의미 없는 블록 레벨 컨테이너(division의 약자)
- form
  - <form>은 정보(데이터)를 서버에 제출하기 위해 사용하는 태그
    - API 에서 get을 써서 params를 보내는데 이때의 get과 비슷함.
    - ex) 로그인 시 id와 pw같은 경우, 게시판 검색의 경우
  - <form>기본 속성
    - action : form을 처리할 서버의 URL(데이터를 보낼 곳) ex) naver, google
    - method : form을 제출할 때 사용할 HTTP 메서드 <- 요청을 보낼건데 어떤 요청?
      - 보통 GET 방식(ex)구글 검색) POST 방)
    - enctype : method가 post인 경우 데이터의 유형
      - application/x-www-form-urlencoded : 기본값 (텍스트)
      - multipart/form-data : 파일 전송시(input type이 file인 경우)
      - text/plain : HTML5 디버깅 용(잘 사용안함)
- form은 데이터를 위한 종이, 쓰는건 input
- input
  - 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
  - <input>의 대표적인 속성
  - type : checkbox, text, etc..., 넘겨줄때 타입
  - name : form cotrol에 적용되는 이름(이름/값 페어로 전송됨), 넘겨줄때 이름
  - id : 연결시킬 for 이랑 같아야함
  - value : form control에 적용되는 값(이름/값 페어로 전송됨), 넘겨줄때 값 <- python dictionary랑 비슷한듯
  - required, readonly, autofocus, autocomplete, disabled 등
```
```
- input label <-스페셜한 별명
  - label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
    - 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일(터치) 환경에서 편하게 사용할 수 있음
    - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어쉽게 내용을 확인 할 수 있도록 함
  - <input>에 id 속성을, <label>에는 for 속성을 활용하여 상호 연관을 시킴
  - ex) <label for="agreement">개인정보 수집에 동의합니다.</label>
        <input type="checkbox" name="agreement" id="agreement">
        - 라벨 = id, input = agreement, 연결은 for
```
- input 유형 - 일반
  - 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 잇음
    - text : 일반 텍스트 입력
    - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
    - email : 이메일 형식이 아닌 경우 form 제출 불가
    - number: min, mas, step 속성을 활용하여 숫자 범위 설정 가능
    - file : accept 속성을 활용하여 파일 타입 지정 가능
- input 유형 - 항목 중 선택
  - 일반적으로 label 태그와 함께 사용하여 선택 항목을 작성함
  - 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
    - checkbox : 다중 선택
    - radio : 단일 선택
- input 유형 - 기타
  - 다양한 종류의 input을 위한 picker를 제공
    - color : color picker
    - date : date picker
  - hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
    - hidden : 사용자에게 보이지 않는 input
- input 유형 - 종합
  - <input> 요소의 동작은 type에 따라 달라지므로, 각각의 내용은 숙지할 것
  - 참고 사이트 : https://developer.mozilla.org/ko/docs/Web/HTML/Element/input