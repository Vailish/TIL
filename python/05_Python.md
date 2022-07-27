# 파이썬이란?
### 파이썬을 배워야 하는 이유
1. 알고리즘 코딩 테스트에 유리 (but 대회 준비는 빠른 C로)) - C++에이어 사용률 2위
2. 구현 코딩 테스트에 유리
   - 유용한 라이브러리 중 최소한만 사용해 개발 할 수 있어 가장 유리한 언어
3. 가장 인기 많은 언어 (전세계적으로)
   - AI 개발, 데이터 분석, 웹프로그래밍, 업무 자동화 등 활용
4. 배우기 쉽다. - 타 언어보다 문법 간결&유연함. 비교적 쉽게 마스터 -> 프로그래밍 사고에 집중가능

### 파이썬의 특징
- **인터프리터** 언어 : 통역하듯이 1줄씩 변환 (<->Compiler(C))
  - cf) .exe : 이미 다 되어있어서 필요없음!
- **객체 지향** 프로그래밍(Object Oriented Programing) <-> 절차지향 프로그래밍(C)
  - 현대 프로그래밍의 기본적인 설계 방법론
  - 파이썬은 객체 지향 언어이며, 모든 것이 객체로 구현

### 파이썬 개발 환경 종류
- IDE(intergrated Development environment)
  - ex) Visual Studio code(범용), Pycharm(python전용)
- Jupyter Notebook
  - 문법 학습을 위한 최적의 도구
- IDLE (Intergrated Development and Learning Environment)
- 코딩 : 수업시간에 목적에 따른 사용도구
    - 파이썬 : Jupyter notebook & Visual Studio Code
    - 웹 : Visual Studio Code
    - 알고리즘 : Pycharm

### 코드 작성법
- 코드 스타일 가이드
  - 코드를 어떻게 작성할지에 대한 가이드라인
  - Python에서 제안하는 스타일가이드(강의에서 사용)
    - **PEP8**(https://www.python.org/dev/peps/pep-0008/)
  - 각 회사별로 가이드가 있음.
    - ex) google(https://google.github.io/styleguide/pyguide.html)
- **가독성(Readability)**을 위해서라도 스타일 가이드를 지키자.
- 공학, 기술 -> 문제해결 -> 요구사항++ -> 프로그램++ -> 개발자 ++ : 따라서 **확장성**이 중요함. -> 확장성을 위해서는 **Style Guide***가 중요!
- Space Sensitive
  - 문장구분 들여쓰기(indentation) : 4칸 or 1tab
- 주석(Comment)
  - 코드에 대한 설명, 소통(협업)을 위해서 필요.(for 개발자)
  - 잘 달린 주석 : 그 어떤 정보보다 유용(주석은 프로그램 속도에 영향안미침)
  - 좋은 주석 다는 습관 중요!, 무분별한 사용은 자제!
  - ex) # : 한줄 /  # or """ : 여러줄
  - 클린코드 : 주석을 달고싶으면 다시한번 봐라 - 변수이름 선언 등으로 주석을 굳이 안달아도 된다! <- 코드가 깔끔하면 보면 알 수 있다.

### 파이썬 프로그램 구성 단위      
- 식별자(identifier)
  - 프로그램이 실행되는 동안 다양한 값을 가질 수 있는 이름
    - ex) 변수, 함수, 클래스, etc
  - 예약어 : 명령어
    - ex) def, print, type, etc..
- 리터럴(literal)
  - 읽혀지는 대로 쓰여있는 값 그 자체
    - '초콜릿'
- 표현식(Expression)
  - 새로운 데이터 값을 생성하거나 계산하는 코드 조각
    - ex) 5 * 20 <- Expression
  - 문장(Statement)
    - 특정한 작업을 수행하는 코드 전체
    - 파이썬이 실행 가능한 최소한의 코드 단위 <- 한 줄 이라고 생각하면 됨
    - ex) print(5 * 20) <- Statement, 모든 표현식은 문장이다.
- 패키지(Package)
  - 프로그램과 모듈 묶음
    - 프로그램 : 실행하기 위한 것
    - 모듈 : 다른 프로그램에서 불러와 사용하기 위한 것
- 라이브러리(Library)
  - 패키지 모음