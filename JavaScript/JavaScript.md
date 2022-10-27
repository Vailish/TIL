# JavaScript

## JavaScript를 배워야 하는 이유
- Web 기술의 기반이 되는 언어
  - HTML 문서의 컨텐츠를 `동적으로 변경`할 수 있는 언어
- 다양한 분야로 확장이 가능한 언어
  - 단순히 Web 조작을 넘어서 `다양한 분야에서 활용이 가능한 언어`가 됨.
- 2022년 현재, 가장 인기있는 언어

## JavaScript의 역사
- Web을 조작하기 위한 언어 -> `Web Browser와 깊은 연관 관계가 있음`

### 웹 브라우저와 스크립트 언어
- 1993, Mosaic Web Browser : GUI 기반의 웹 브라우저(버튼 등 탑재)
- 1994, Netscape Navigator : Mosaic Web Browser를 개선한 후속작, 시장 점유율 80%차지
  - 이때까지 정적 웹 페이지를 보여주는 용도 -> 동적 웹페이지를 위한 `script언어개발` 필요
    - script언어 : 컴파일러 없이 바로 실행 가능한 언어, 단) 속도가 느림
  - Netscape에서 약 10일의 개발기간을 통해 script언어인 Mocha 개발
  - Mocha -> LiveScript(브라우저에 해석 Engine내장) -> JavaScript(단순 Java인기에 탑승하고자 이름변경)
- 1995, Microsoft의 Internet Explorer
  - Netscape의 JavaScript를 그대로 복사한 JScript 제작 후 탑재한 웹 브라우저인 Internet Explorer 출시
  - 이후 각자의 기능을 추가, 개발자들의 피로도 증가
- 1996-2000 ECMA표준 발의
  - Netscape가 ECMA에게 JavaScript 기반의 표준안 발의 제안, ECMAScript1 출시, 버전업데이트
  - Microsoft Window에 Internet Explorer 기본 탑재로 인해 시장 점유율 95% 이상 증가, ECMAScript 안지킨다고 선언
- 2001-2004, 다양한 웹 브라우저의 등장
  - ActionScript3 기반의 Firefox 웹 브라우저 출시 -> Opera등의 다양한 웹 브라우저 출시 -> 늘어가는 개발자 고통 -> 개발자 수요 증가 -> 집단 지성 형성
- jQuery 등의 라이브러리 등장
  - 중간에 하나의 레이어를 두고 코딩하는 방법인 jQuery
  - jQuery 문법에 맞춰 작성하면 브라우저별 엔진에 맞는 스크립트로 변환해줌
- 2008, Google의 Chrome 등장과 대통합의 시대
  - V8 엔진을 탑재한 Chrome 등장
  - JavaScript 해석이 월등히 빠름
  - 다른 웹 브라우저들의 표준안 제안
- 2009, ES5(ECMAScript5)표준안 제정
- 2015, `ES6` 표준안 제정
  - ES6에서 큰 변화가 일어남
  - 이런 표준화로인해 jQuery등의 라이브러리 사용이 필요 없어짐
- Chrome V8의 경우 JavaScript를 번역하는 속도가 매우 빨라 Browser 밖에서 활용하려고 시도함
  - node.js, react.js, electron 등의 내부 엔진으로 사용 -> 많은 분야에서 JavaScript로 개발이 가능해짐


### JavaScript 실행방법
1. HTML파일에 직접 JavaScript를 작성 후 웹 브라우저로 파일 열기
  - Chrome 개발자 도구 console에서 실행가능(엔진이 있기때문)
  - `Vanilla JavaScript` : 웹 브라우저에서 바로 실행할 수 있는 JavaScript문법 들
2. Node.js로 실행

## JavaScript 기초 문법

### 코드 작성법
- 세미콜론
  - 세미클론이 없으면 ASI에 의해 자동으로 세미클론이 삽입 됨.(선택적 사용가능)
    - ASI(Automatic Semicolon Insertion)
```js
console.log('hello');
console.log('vailish')
```

- 들여쓰기와 코드 블럭
  - `2칸 들여쓰기` 사용
  - `block(블럭)`은 if, for 함수에서 중괄호 `{}` 내부를 말함
    - cf) 파이썬의 경우 들여쓰기로 코드블럭 구분
```js
if (isGood) {
  console.log('Good job!')
}
```

- 코드 스타일 가이드
  - 다양한 경우가 있지만 `Airbnb JavaScript Style guide`이 대표적임
  - 그 외에도 Google JavaScript Syle Guide, Javascript Standard Style 등이 있음

- 주석
  - 한 줄 주석(//)과 여러 줄(/* */)주석
```js
// 오늘 하루도 고생했다!!

/*
위는 한 줄 주석
이 곳은 여러줄 주석!
*/
```

### 변수와 식별자
- identifier(식별자) 정의와 특징
  - 식별자는 변수를 구분할 수 있는 변수명
  - 반드시 문자, 달러($), 밑줄(_)로 시작
  - 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
  - 예약어 사용 불가능
    - ex) for, if, function 등
  - camelCase, lower-camel-case : 변수 객체, 함수에 사용
  - PascalCase, upper-camel-case : 클래스, 생성자에 사용
  - SNAKE_CASE, 대문자 스네이크 케이스 : 상수(constants)에 사용
```js
// camelCase
let dog
let variableName

const userInfo = { name: 'Tom', age: 20 }
function add() {}
function getName() {}

//Pascal Case
class User {
  constructor(options) {
    this.name = options.name
  }
}
function User(options) { //생성자 함수
  this.name = options.name
}

//SNAKE_CASE
const API_KEY = 'my-key'  // 값 변화 X
const PI = Math.PI

const NUMBERS = [1, 2, 3]  // 재할당 X
```

- 변수 선언 키워드
  1. let - 블록 스코프 지역 변수를 선언(+ 값 초기화)
  2. const - 블록 스코프 읽기 전용 상수를 선언( + 값 초기화)
  3. var - 함수 스코프, 변수를 선언(+ 값 초기화)
      - `hoisting 현상` (할당선언 전에 출력하면 프린트에서 python의 none과 같은 undefined 값이 출력됨.., 변수만 따로 설정하는게 (내가 안했지만) 위에서 되어서 그런 것, 이게 호이스팅)
      - 이 특성 떄문에 ES6 이후 부터 const와 let 사용을 권장
      - 변수를 선언하기 전에 접근이 가능한 것은 코드의 논리적인 흐름
      - 을 깨뜨리는 행위이며 이를 방지하기 위해 ES6에서 let, const 추가 -> `var는 쓰지말자`
      - 프로그래밍 언어가 아닌 스크립트로 탄생 -> 허점이 많고, 이 버그들은 레거시코드로 인해 고치지 못하고 그대로 안고 가고있음
```js
//hoisting(호이스팅)

// var name  // JavaScript에서 변수들은 실제 실행시에 코드의 최상단으로 끌어 올려지게 되는데 이를 호이스팅 현상이라함, let과 const의 경우 호이스팅이 일어나면 에러를 발생시킴
console.log(name)  // var이라 에러가 아니라 undefined 로 초기화 됨
var name = 'Vailish'
```

```
  - cf) 선언, 할당
    - Declaration(선언) : 변수를 생성하는 행위 또는 시점
    - Assignment(할당) : 선언된 변수에 값을 저장하는 행위 또는 시점
    - Initialization : 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점
```js
// 선언, 할당, 초기화
let vailish  // 선언
console.log(vailish)  //undefined

vailish = 20  // 할당
console.log(vailish)  // 20

let score = 100  // 선언 + 할당
console.log(score)  // 100
```
  - block scope
    - if, for, 함수 등의 중괄호({}) 내부를 가리킴
    - 블록 스코프를 갖는 변수는 블록 바깥에서 접근 불가능
```js
let x = 1

if (x === 1) {
  let x = 2
  console.log(x)  // 2
}
console.log(x)  // 1
```

### 데이터 타입
p56