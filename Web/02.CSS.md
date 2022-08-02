### CSS
- CSS : Cascading Style Sheets(cascading 계단식, 폭포, 위에서 설정하면 아래 따로 설정 안하면 상속처럼, 오버라이드처럼 적용됨)
- 스타일을 지정하기 위한 언어 : 선택하고, 스타일을 지정한다
- CSS 구문
  - ex) h1{                <-선택자(Selector)
          color: blue;     <- 선언(Declaration)
          font-size: 15px; <- font-size : 속성(property, not attribute), 15px : 값(value)
        }
- CSS
  - css구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
  - 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
  - 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
    - 속성(Property) : 어떤 스타일 기능을 변경할 지 결정
    - 값(Value) : 어떻게 스타일 기능을 변경할 지 결정
- CSS 정의 방법
  - 인라인(inline)
  - 내부참조(embedding) - ```<style>```
  - 외부참조(link file) - 분리된 CSS 파일
  - ex)
```
    - 인라인 <h1 style="color: blue; font-size: 100px;">Hello</h1>
    - 내부참조 <style>
                 h1 {
                   color: blue;
                   font-size: 100px;
                 }
                </style>
    - 외부참조 <- 한 양식파일로 여러파일 가능해서 유용함, 분리된 css파일
      - 쓸양식(외부파일) :
        h1 {
            color: blue;
            font-size: 20px;
        }
      - 쓸파일 : <link rel="stylesheet" href="mystyle.css"
        - tip : link 쓰고 tab누르면 알아서 양식은 써줌 
```
- 주로 활용하는 CSS는 30~40가지 정도
- CSS with 개발자 도구
  - style : 해당 요소에 선언된 모든 CSS
  - computed : 해당 요소에 최종 계산된 CSS

### 선택자 결합자 display position
- 선택자
  - 전체 : *
  - 요소 = tag + 내용
  - id : 1개만 선택 <- id 선택시 #cool-color 이런식으로 씀 (되는 걸로 별도로 약속)
  - class : 여러개 선택 <- 선택시 .cool=colpr 이런 식으로함 (되는 걸로 별도로 약속)
    - 내가 원하는 거를 *선택*하고 싶어서 사용하는 것 id, class
  - 속성
  - 결합자
- 결합자(combinators)
  - 자손 결합자 : >p (하위 항목 전체)
  - 자식 결합자 : .box (한 단계 아래만)
  - 일반 형제 결합자
    - P ~ SPan : P 뒤에있는 SPan들 전부 바꿔!(뒤에 바로 안붙어도됨.)
  - 인접 형제 결합자
    -  P + **P**(같은 트리 구조, 같은 깊이) == P뒤에 있는 P 그래서 제일 앞에있는 P는 포함안됨(뒤의 P가 기준), 바로 뒤만 가능하기 때문에 사이에 자식이 있으면 안됨.
```
  <style>
    /* 전체 선택자 */
    * {
      color: red;
    }

    /* 요소 선택자 */
    h2 {
      color: orange;
    }

    h3, 
    h4 {
      font-size: 10px;
    }

    /* 클래스 선택자 */
    .green {
      color: green;
    }

    /* id 선택자 */
    #purple {
      color: purple;
    }

    /* 자식 결합자 */
    .box > p {
      font-size: 30px;
    }

    /* 자손 결합자 */
    .box p {
      color: blue;
    }
  </style>
</head>
<body>
  <h1 class="green">SSAFY</h1>
  <h2>선택자 연습</h2>
  <div class="green box">
    box contents
    <div>
      <p>지역 목록</p>
      <ul>
        <li>서울</li>
        <li id="purple">인천</li>
        <li>강원</li>
        <li>경기</li>
      </ul>
    </div>
    <p>lo</p>
  </div>
  <h3>HELLO</h3>
  <h4>CSS</h4>
</body>
```
- Display
  - block
    - 줄바꿈이 일어나는 요소
    - 화면 크기 전체의 가로 폭을 차지한다
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
    - ex) div / ul, ol, li / p / hr / form, etc
  -  inline
    -  줄 바꿈이 일어나지 않은 행의 일부 요소
    -  content 너비 만큼 가로 폭을 차지한다.
    -  width, height, margin-top, margin-bottom,을 지정할 수 없음
    -  span / a / img / input, label / b, em, i, strong, etc
  - inline-block
    - 외부적으로는 inline : inline 처럼 자기 영역만큼만 차지함
    - 내부적으로는 block : block의 속성, 즉 너비 높이 등 다 조절 가능함.

- position
  - 문서 상에서 요소의 위치를 지정
  - 모든 요소는 기본 posion == static
  - static : 모든 태그의 기본 값(기준 위치)
    - 일반적인 요소의 배치 순서에 따름(좌측 상단)
    - 부모 요소내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
  - 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
    - 기본적으로 이동하는 규칙을 변경하는 것
      - ex) (position: static) -> position: relative
    - relative
      - 내가 스태틱일때 공간은 남겨두고 이동한다.
      - 기존 속성의 끝 부분(대각아래)에서 다시 그린다고 생각하면됨.
      - 하지만 자신이 기존에 있던 공간은 차지하고 있는 것이고, 모습만 이동한 것
    - absolute
      - relative에서 기존 공간 자체도 없앰(공간을 차지하지 않음).
      - 붕 떠있다.
      - 부모가 스태틱이 아닌 기준으로 움직임
        - 스태틱일 시 바깥으로 쫓겨남(스택틱이 아닌 부모가 없으면 화면을 기준으로 이동함) -> 사용시 부모를 항상 주의 깊게 봐야함!
    - fixed
    - sticky





##### CSS Selectors
- 선택자(Selector) 유형
  - 기본 선택자
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자
  - 결합자(Combinators)
    - 자손 결합자, 자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자
  - 의사 클래스/요소(Pseudo Class)
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
- CSS 선택자 정리
  - 요소 선택자
    - HTML **태그**를 직접 선택
  - 클래스(Class) 선택자
    - 마침표(.)문자로 시작하여, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자 <- #이름
  - \# 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권함
- CSS 적용 우선순위(cascading order)
  - CSS 우선순위를 아래와 같이 그룹을 지어 볼 수 있다
    - 중요도(importance) - 사용시 주의 !important
    - 우선순위(Specificity)
      - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
    - CSS 파일 로딩 순서
  - 요소 > 클래스 > 아이디 : 범위가 좁아짐 == 파워가 쌔짐
    - 범위가 동급이면 아래에 있는게 이김!, 그리고 다 이기는 건 !important
    - ex) 한국인 > 성 > 이름
- ex)
    h2 {
      color: darkviolet !important;
    }

    p {
      color: orange;
    }
    
    .blue {
      color: blue;
    }

    .green {
      color: green;
    }

    #red {
      color: red;
    }
```
  </style>
</head>
<body>
  <p>1</p>
  <p class="blue">2</p>
  <p class="blue green">3</p>
  <p class="green blue">4</p>
  <p id="red" class="blue">5</p>
  <h2 id="red" class="blue">6</h2>
  <p id="red" class="blue" style="color: yellow;">7</p>
  <h2 id="red" class="blue" style="color: yellow;">8</h2>
</body>
</html>
```
- CSS 상속
  - CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
    - 속성(프로퍼티) 중에서 상속되는 것과 되지 않는 것들이 있다.
    - 상속되는 것 예시
      - Text관련 요소(font, color, text-align), opacity, visibility 등
      - 상속되지 않는 것 예시
      - 에) Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index)등

##### CSS 기본 스타일
- 크기 단위
  - px(픽셀)
    - 모니터 해상도의 한 화소인 '픽셀'기준
    - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
  - %
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
  - em
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
    - 배수단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
  - rem
    - (바로 위, 부모요소에 대한) 상속의 영향을 받지 않음
    - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
    - ex) 기본글자 기준으로 몇배
- 크기 단위(viewport)
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax
- 색상 단위
  - 색상 키워드(background-color: red;)
    - 대소문자를 구분하지 않음
    - red, blue, black 과 같은 특정 색을 직접 글자로 나타냄
  - RGB색상(background-color: rgb(0, 255, 0);)
    - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
  - HSL 색상(background-color: hsl(0, 100%, 50%);)
    - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
  - 색상 키워드
  - RGb 색상
    - '#' + 16진수 표기법
    - rgb() 함수형 표기법
  - HSL 색상
    - 색상, 채도, 명도
  - a는 alpha(투명도) rgba(0, 0, 0, 0.5)<- 여기서 0.5가 투명도
- CSS 문서 표현-추후에 하나씩
  - 텍스트
    - 서체(font-family), 서체 스타일(font-style, font-weight 등)
    - 자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height)등
    - 컬러(color), 배경(background-image, background-color)
    - 기타 HTML 태그별 스타일링
      - 목록(li), 표(table)


##### sectors 심화
- 결합자(Combinators)
  - 자손 결합자(공백)
    - selectorA 하위의 모든 selectorB 요소
```
<div>
  <span>이건 빨강입니다.</span>
  <p>이건 빨강이 아닙니다.</p>
  <p>
    <span>이건 빨강입니다.</span>
  </p>
</div>  
```
  - 자식 결합자(>)
    - selectorA 바로 아래의 selectorB 요소
```
<div>
  <span>이건 빨강입니다.</span>
  <p>이건 빨강이 아닙니다.</p>
  <p>
    <span>이건 빨강이 아닙니다.</span>
  </p>
</div>  
```
  - 반 형제 결합자(~)
    - selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택
  - 인접 형제 결합자(combinators)(+)
    - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택
- 자손결합자, 자식결합자
  - ex) span 태그

CSS Box model
여기부터는 그냥 교재보고 하는게 나을듯...(시간날때 이미지로 정리해서 올리기)
- margin
- border
- padding
- content
