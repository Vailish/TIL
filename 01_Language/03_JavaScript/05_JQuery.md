# JQuery 내 정리
- 선택자
```js
$() // 난 이 녀석을 사용할거야!

$("p") // 난 p태그들을 선택할거야
$(".a") // 난 a class를 가진 녀석들을 사용할거야!
$("#b") // 난 id가 b인 녀석을 사용할거야!
$(inputForm) // 난 id가 inputForm인 녀석을 사용할거야!

$("#c").attr("data-id", "데이터임") // 난 id가 c인 녀석들의 data-id 특성에 "데이터임"으로 설정할거야
$(".d").css("border", "2px solid orange") // 난 클래스가 d인 녀석들의 "border"를 "2px solid orange"로 설정할거야
$(movingForm).attr("method", "GET").attr("action", "www.naver.com/").submit() // 난 movingForm 이라는 Form의 "method" 특성에 "GET"을, "action" 특성에 "www.naver.com/"을 넣고 실행할거야
```

- 함수
```js
$(".e").on("click", function() {}) // 난 e클래스를 클릭할 때 {} 함수를 실행할거야

$(function(){}) // 아래와 같음
$(document).ready(function(){}) // 난 DOM 객체가 생성되면 {} 함수를 실행할거야
```

# JQuery
## JQuery란
- jQuery는 2006년 미국의 존 레식(John Resig)이 뉴욕시 바캠프(Barcamp)에서 처음 소개한 ‘자바 스크립트 라이브러리’
- 코드가 브라우저의 영향을 받아 작동하지 못하는 문제를 해결하기 위해 개발됨
- 특히, IE(Internet Explorer)에서는 버전이나 호환성의 문제를 해결하고자 ‘크로스 브라우징’ 기능을 가진 jQuery가 탄생
    - 크로스 브라우징 : 브라우저에서 같은 코드로 동일한 동작을 할 수 있게 하는 기능

## JQuery 장점
- 뛰어난 Dom 구조 탐색
- 크로스 브라우징 지원

## 예시
```js
$().on("click", "#aaa", function(){})
```
- JQuery에서 $().on("click", "#aaa", function(){})는 이벤트 핸들러를 등록하는 구문입니다. 각 부분의 의미는 다음과 같습니다:
- $() : JQuery의 선택자 함수로, HTML 요소를 선택하는 역할을 합니다.
- .on("click", "#aaa", function(){}) : 선택된 요소에 클릭 이벤트를 등록하는 메소드입니다.
- "click" : 이벤트 유형을 나타냅니다. 여기서는 클릭 이벤트를 처리하도록 지정했습니다.
- "#aaa" : 이벤트 핸들러가 적용될 대상을 나타냅니다. 여기서는 ID가 "aaa"인 요소에 클릭 이벤트 핸들러가 적용됩니다.
- function(){} : 클릭 이벤트가 발생했을 때 실행될 콜백 함수를 정의합니다. 이 함수에는 클릭 이벤트에 대한 처리 로직이 들어갑니다.
    - #은 id를 선택하겠다는 선택자르 나타내는 것, 없다면, 태그 이름이나 클래스를 나타내는 것
- 이 구조의 의미는 "ID가 'aaa'인 요소를 클릭했을 때, 해당 요소에 대한 처리를 수행하는 이벤트 핸들러를 등록한다"입니다. 이러한 방식으로 JQuery를 사용하면 특정 이벤트가 발생했을 때 특정 요소에 대한 동작을 정의할 수 있습니다.

### 참고자료
- [JQuery란](https://www.elancer.co.kr/blog/view?seq=176)
- [JQuery기초](https://velog.io/@bi-sz/jQuery-%EA%B8%B0%EB%B3%B8)

## 에디터에서 작성한 내용 가져오기
- ed_wr_content.outputBodyHTML() 와 같이 outputBodyHTML()를 사용하면 가져올 수 있음

## 데이터 폼 사용하기
- 아래와 같이 사용하면, 폼 태그 안쪽에 값들을 name을 key로 가져옴
```js
data : $("#myInsertForm").serialize(),
```
- 별도의 조작이 필요하다면 아래와 같이 따로 정의를 해주는 것
```js
    data : {
        boardTitle : boardTitle,
        boardContent : boardContent,
        boardId : 1,
        userId : "admin",
        userName : "총관리자",
        userIp : "192.168.50.195"
    }
```

## $(function(){})
- == $(document).ready(function(){})
- 여기 저기 jQuery를 이용한 사이트의 코딩을 보면, $(function(){}); 이라고도 많이 사용하는데
- $(document).ready(function(){});와 동일한 의미입니다.
- **$(document).ready(function(){});** 이것이 **jQuery를 사용하기 위한 기본 문법**입니다.
- 정확히는 DOM(Document Object Model) 객체가 생성되어 준비되는 시점에서 호출된다는 의미입니다.
- JS와 비교하자면 document.onload()... 와 거의 비슷하다고 생각하면 되고, html 문서가 로딩이 되면...이라는 느낌으로 이해하시면 됩니다.
    - [참고 window.onload VS $(document).ready](https://m.blog.naver.com/u3478/60134222468)
        - window.onload : 체 페이지의 모든 외부리소스와 이미지가 브라우저에 불리워진 이후에 작동, 외부 링크나 파일을 인클루드 했을 때 해당 스크립트가 존재한다면, 하나만 작동함
        - $(document).ready : 외부 리소스 및 이미지와는 상관없이 DOM데이터만 로드가 완료되면 바로 실행이 되는 함수
        ```js
        <script type="text/javascript">
        window.onload=function() {
        alert("ccc");
        }
        $(document).ready(function() {
        alert("aaa");
        });
        $(document).ready(function() {
        alert("bbb");
        }
        </script>
        // 실행순서 : aaa->bbb->ccc
        ```
```js
$(function(){})
```

### [DOM 객체](https://www.codestates.com/blog/content/dom-javascript)
- 문서 객체 모델, 즉 DOM은 웹 페이지(HTML이나 XML 문서)의 콘텐츠 및 구조, 그리고 스타일 요소를 구조화 시켜 표현하여 프로그래밍 언어가 해당 문서에 접근하여 읽고 조작할 수 있도록 API를 제공하는 일종의 인터페이스입니다. 즉 자바스크립트 같은 스크립팅 언어가 쉽게 웹 페이지에 접근하여 조작할 수 있게끔 연결시켜주는 역할을 담당합니다.
![Dom Object](https://i0.wp.com/blog.codestates.com/wp-content/uploads/2022/12/%EB%AC%B8%EC%84%9C-%EA%B0%9D%EC%B2%B4-%EB%AA%A8%EB%8D%B8-DOM-%EA%B3%BC-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-JavaScript.jpg?resize=768%2C489&ssl=1)
- Document가 최상위 노드
- 순서대로 Document - Element - Text - attribute 계층
- 노드란 DOM에서 정보를 저장하는 계층적 단위
### 참고자료
- [문서 객체 모델 DOM 과 자바스크립트 JavaScriptㅣ생성 방식 및 접근 방법 ](https://www.codestates.com/blog/content/dom-javascript)
- [window.onload 와 $(document).ready 의 차이점??](https://m.blog.naver.com/u3478/60134222468)


# JQuery 기본 문법







### 참고자료
- [📚 jQuery 기본 문법 $() 정리](https://inpa.tistory.com/entry/jQuery-%F0%9F%93%9A-%EA%B8%B0%EB%B3%B8-%EB%AC%B8%EB%B2%95-%EC%A0%95%EB%A6%AC)

# ajax
- https://scoring.tistory.com/entry/AJAX%EB%9E%80-JQuery%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-AJAX%EC%82%AC%EC%9A%A9%EB%B2%95


# 팝업관련
```js
function excelUploadPage() {
	
	$.ajax({
		 type: "post",
		  url: "board/excelUpload",
	 dataType: "html", 
	     data: $("#myForm").serialize(),
	  success: function(data) {
		
		 $('#insertHere').html(data);	
			
		 $('#insertPopup').bPopup({
				modalClose : false,
				opacity : 0.7
				});
		 },
		error : function(data) {
			alert("오류가 발생하였습니다.\n관리자에게 문의하세요.");
		}		
	});	
}
```
- `dataType : html` -> 응답 방식(return값을)을 html로 받겠다.
- `.html` : 받아온 html파일의 첫번째 해당하는 값들을 가져오겠다.
    - [블로그, 제이쿼리 html 내용 가져오기, 변경하기 (JQuery html()](https://itstudy402.tistory.com/53)
    - [공식문서](https://api.jquery.com/html/)
- `.bPopup`
    - JQUERY POPUP PLUGIN
    - 여러 옵션을 주고 편하게 팝업을 띄울 수 있는 녀석
    - [jQuery.bPopup.js](https://dinbror.dk/bpopup/)