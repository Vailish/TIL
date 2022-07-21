# 기초 문법
### 변수(Variable)
 - 변수 = 데이터를 담는 상자
   - ex1) a = 4 <- a는 **공간**
   - ex2) a = a + 4 <- a라는 공간에 넣어라
     - 그러므로 a + 1 = 5 이런 코드는 허용하지 않음!
 - 데이터를 저장하기 위해 사용
 - 변수사용 -> 복잡한 값들을 쉽게 사용할 수 있음(추상화)
   - 추상화 : 내부의 원리를 잘 몰라도 쓸 수 있는것(복잡한 것은 숨기고 필요한 것만 드러낸다.)
   - ex) print(3000 * 2 + 3500 * 3 + 4000 * 5)
   - 추상화(변수를 사용해야 하는 이유)
     - 일일이 값을 넣는 것이 불편함
     - 코드를 알아보기 힘듦(3000이 어떤것에 대한 3000인지 모름)
     - 고치기 어려운코드(숫자가 변경된다면?)
     - ex) mocha_price = 3000

 - 데이터 저장 -> 처리 : 프로그래밍의 기본원리
   - 변수를 먼저 배우는 이유(데이터를 저장하는 방법)
   - 변수, for : 데이터 1개 / 자료형 : 데이터 여러개

#### 변수의 할당
- 변수는 할당 연산자(=)을 통해 값을 할당(assignment)
- ex) mocha_price = 3000

#### 각 변수의 값을 바꿔서 저장하기
- 방법1 : 임시변수 활용 (일반적인 언어들의 방법)
```Python
x, y = 10, 20

tmp = x

x = y

y = tmp

print(x, y) #20, 10
```

- 방법2 : Pythonic!
```Python
  x, y = 10, 20 <- 다른언어는 애초에 이렇게 쓰는게 안됨, 튜플처리 해줘야함

  y, x = x, y

  print(x, y) # 20, 10
```
#### 식별자(이름)
- 변수 이름 규칙
  - 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성
  - 첫 글자에 숫자 올 수 없음
  - 길이 제한X, 대소문자를 구별
  - Keywords는 예약어(reserved words)로 사용할 수 없음
    - ex) False, if, del, as, None, etc : 이미 등록된 것
  - 내장 함수나 모듈 등의 이름X (다른 곳에서 쓰는 이름X) : 동작하지 않음, 덮어 씌여버리니까.

---

### 연산자
- 산술 연산자 : +, -, *, /, //(몫), **(거듭제곱)
- 연산자 우선순위 : 수학과 같음

---

### 자료형(Datatype)
- 사용할 수 있는 데이터의 종류
- 다양한 종류의 값(data)
- Data Type
  - Boolean Type : 참 거짓
  - Numeric Type : 숫자
    - Int (integer, 정수)
    - Float (부동소수점, 실수, floationg point number)
    - Complex (복소수, complex number)
  - String Type : 문자

#### 진수표현
- 2진수(binary) : 0b
- 8진수(octal) : 0o
- 16진수(hexadecimal) : 0x

#### 부동소수점 - 실수 연산시 주의할 점
- ex)
  3.2 - 3.1 = 0.10000000000000009
  1.2 - 1.1 = 0.00999999999999987
  연산의 결과가 0.1이 아니다!
- 컴퓨터는 2진수, 사람은 10진법을 사용 
- 컴퓨터는 0.1은 2진수로 표현 : 무한반복 -> 사람이 사용하는 10진법의 근사값만 표시 -> 여기서 나오는 문제 : 부동소수점 문제라고함
- 해결법 : math 모듈 활용, abs(절대값), isclose(3.5버전이상 사용가능)
  - 방법1) print(abs(a - b) <= 1e-10) # True가 나오면 두 실수는 값이 같을 만큼 충분히 작다.

    방법2)
    ```python 
    import math
    print(math.isclose(a, b)) #True가 나오면 두 실수는 값이 같을 만큼 충분히 작다.(Python 3.5이상)
    ```
    
---

### 문자열 자료형
- 모든 문자는 str타입
- '', "" (묶을 때 동일 문장부호)
- PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지
- 중첩 따옴표
  - ' "" ', " '' "
- 삼중 따옴표(Triple Quotes)
  - ''' '''
- Escape sequence
  - \n : 줄바꿈, *개행*이라고 부름
  - \t : 탭
  - \r : 캐리지 리턴(커서를 제일 앞으로)
  - \0 : Null
  - \\ : \
  - \' : '
  - \" : "
  - \+a : a(쓰고싶은 기호 출력할때 사용)

#### 문자열 연산
- 덧셈 : 문자열연결(String Concatenation)
  - ex) hello + World = helloWorld
- 곱셈
- & - formatting(예전에 사용)
  - ex)
    ```python 
      name = 'Kim'
      print('hello, %s' % name) #Hello, Kim
    ```
- String Interpolation(문자열을 변수와 활용하여 만드는 법 python3.6+)
  - f-string
  - ex)
    ```python
    print(f'hello.{name}! 성적은{score}')
    print(f'오늘은{today:%y}년 {today:%m}월 {today:%d}일')
    print(f'원주율은 {pi:.3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
    ```

#### None
- 파이썬 자료형 중 하나
- 값이 없음을 표현하기 위해 None 타입이 존재
- 반환값이 없는 함수에서 사용하기도 함(ex) print)

#### Boolean(불리형)
- 논리 자료형으로 참과 거짓
- True or False 값을 가짐
- 비교/논리 연산에서 활용됨(주로 조건문, 값을 비교)
  - 수학의 등호와 부등호와 동일개념, 결과 True/False 값을 리턴
- ex1) 비교연산자 : <, <=, >, >=, ==, !=, is, is not
- ex2) 3.0 == 3 >>> True <- 언어에 따라 결과가 달라지기도함 (java랑 python이랑 java script랑 다 철학이 달르기 때문)
- 논리 연산자
  - 여러 가지 조건이 있을 때
    - 모든 조건을 만족하거나(And), 여러 조건 중 하나만 만족해도 될때(or)
    - ex1) 논리연산자 : A and B, A or B, Not : True를 False로 False를 True로
    - ex2)
      hour = 23
      
      status = 'sleepy'
      
      print(hour >= 22 and status == 'sleepy') #True
- Falsy : False는 아니지만 False로 취급 되는 다양한 값
  - ex) 0, 0.0, (), {}, None, ""(빈 문자열)
- 논리 연산자도 우선순위가 존재
  - not, and, or 순으로 우선순위가 높음!(수학의 곱하기 더하기같은 느낌으로 보면 됨)
    - ex) print(not True) # False
- 논리 연산자의 단축 평가
  - 결과가 확실한 경우, 두번째 값은 확인하지 않고 첫번째 값 반환
    - ex1) and 연산에서 첫번째 값이 False인 경우 모조건 False => 첫번째 값 반환
    - ex2) or 연산에서 첫번째 값이 True인 경우 무조건 True => True
    - ex3)
      a = 5 and 4
      print(a) #4
      print(0 and True) #0
      print(3 and 5) #5
      평가해서 True False 값은 따지지만, 나와있는 거에 따라서 숫자냐 True False냐가 갈림
