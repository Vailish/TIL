요즘에는 Float는 잘 안씀(IE, 1996 internet explorer에서 많이 썻음)
요즘에는 Flexbox(2012)를 많이씀

# CSS
### Float

### Flexbox
- CSS Flexible Box Layout <- ie 부분지원
- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
  - cf) z-index : 위아래로 배치하는거 여러개의 레이아웃 생각하면 됨
- 꼬챙이!! main, justify / 나머지는 수직

### bootstrap

1rem = 16px
bootstrap의 장점 선택자를 안봐도됨! 클래스 먹여서 하기때문
빈거 넣을때 #많이씀
만들때 a.text-decoration-none 과 같이써서 하자 <- 클래스랑 헷갈리는 상황 자동완성이 막아줌!
### Flexbox
- float, absolute : 둥둥 떠다니는 애들, 여러개를 딱딱 맞추기 힘듦(수치를 많이써야함) ->Flex box등장!
- flex container : 부모 (꼬치 넣는 상자)
- main axis : 꼬치방향, 메인축
- cross axiss : 꼬치와 수직방향, 교차축
- CSS속성을 이용해서 적용
- 부모 -> 자식 까지만 적용, 자손은 적용 X (상속이 안되기 때문에 자손에게도 하려면 그 위에도 Flex 줘야함)

- Flexbox - 속성 적용
  - 부모 컨테이너 <- display: flex;
  - 자식 아이템

- 부모 컨테이너에 적용
  - flex-direction: row <- 기본 가로
  - flex-direction: row-reverse <- 가로 오른쪽에서부터(언어에 따라서)
  - flex-direction: column <- 세로
  - flex-direction: column-reverse <- 세로 아래서부터

  - flex-wrap: nowrap <- default, 크기를 줄여서 채워넣음
  - flex-wrap: wrap <- 끝에 넘어가면 다음줄로 넘어감
  - flex-wrap: wrap-reverse <- 끝에 넘어가면 아래줄에서 윗줄로 넘어감


  - content : 여러개, items : 한 개
    - ex) alighn-items : 한 줄, align-content : 여러줄
    - cf) justify-items, justify-self : 무시당함 <- align으로 할 수 있기 때문에 공식문서에서도 인정 안해줌
  - justify-content : 메인축 기준
  - justify-content: flex-start
  - justify-content: flex-end
  - justify-content: flex-center
  - justify-content: flex-space-between <- 양쪽 붙이고 가운데(공간)를 균등하게 가져가는 것
  - justify-content: flex-space-evenly <- 아이템 기준으로 시작과 끝지점부터 그리고 아이템간 공간의 크기가 균등
  - justify-content: flex-space-around <- 아이템 기준으로 양쪽 공간이 균등

  - align-items : 교차축 기준
  - align-items: flex-start
  - align-items: flex-end
  - align-items: flex-center
  - align-items: flex-space-between <- 양쪽 붙이고 가운데(공간)를 균등하게 가져가는 것
  - align-items: flex-space-evenly <- 아이템 기준으로 시작과 끝지점부터 그리고 아이템간 공간의 크기가 균등
  - align-items: flex-space-around <- 아이템 기준으로 양쪽 공간이 균등
  - align-items: baseline
align-content : 교차축(메인 축의 수직) 기준

 - flex-grow : 공백을 다 먹음
   - flex-grow: 1;
   - flex-grow: 2; -> 1:2의 비율로 공백 먹고, 미 선언시 0이 default값임

- 자식 아이템에 적용 <- 개체 하나하나적용
  - 자식에 적용하기 때문에 style 안에 넣어줘야함 ex) style="align-self: center"
  - align-self: center
  - align-self: flex-start
  - align-self: flex-end
  - align-self: flex-center

  - order: 1
  - order: 2
  - order: 3
    - 이런식으로 처리를 하면 쓴 방식대로 보여주긴 하지만, 보여주기만 저렇게 할 뿐, 코딩할 때는 의미가 없음.

- 개발자 도구 사용법  
  - 코드에서 + 버튼 눌러서 다양한 스타일 적용가능
  - https://v-firstweb.netlify.app

- 배포 - 네이버같이 들어갈 수 있는 이유는 배포 했기때문에 - netlify 에서 무료로 배포 가능