### 함수
- 함수를 쓰는 이유
  - Decomposition(분해)
    - 기능 단위로 쪼개서(분해해서) 재사용하기 편하게 사용!
    - 간결하고, 이해하기 쉽다!
  - Abstraction(추상화)
    - 복잡한 내용은 모르더라도 사용할 수 있도록(ex) 스마트폰 원리는 몰라도 잘씀)
    - 재사용성과 가독성, 생산성
  - 함수 = 미니프로그램, 프로그램이 갖는 저장과 처리 둘다 갖고있다.
    - 프로그램 : input(input()) -> .py(프로그램) -> output(print())
    - 함수 : input(파라미터) ->  -> output(return)
      - 함수를 사용할때 실제 입력값 Argument
        - ex) def function(**ham**) : ham parameter
      - 함수를 선언할때 입력값 parameter -> 함수 안에서만 사용가능]
        - ex) function(**'spam'**) : 'spam' argument



- len([1, 2, 3])
- sum([1, 2, 3])
- input() -> 문자열로 받는다, 한 줄로 받는다.
- range(시작점, 끝점-1 , *간격*)
- 
###### input() vs sys.stdin.readline() 
- 공통점 : 입력함수로 서로 같은 위치에 사용하면 됨.
- 차이점
  -  input()
     - 기본적으로 문자열을 입력받는 것으로 처리.
     - method로써 바로 사용가능
  -  sys.stdin.readline()
     - 한 줄에 여러 입력값을 받을 수 있음.
     - 내장되어 있지 않기 때문에 **import sys**를 이용하여 불러서 사용가능.
     - 개행문자(줄바꿈, "\n")을 포함하고 있어 **형태를 바꿔주거나**(ex)int), 개행을 삭제해줘야(**rstrip()**) 공백없이 출력이 가능.
- 굳이 sys.stdin.readline()을 사용하는 이유
  - input에 비해 **속도가 매우 빨라**, *알고리즘 문제를 풀때*, 시간초과 에러가 나오는 경우 해결하기 위해 사용함.(입력값을 수 백, 수 천개를 받을 때 유용함.)
- ex)
```python
# 1 
# 2 를 입력해주면
a = input()
import sys
b = sys.stdin.readline()
print(a, b, a, b)
#1 2
# 1 2

#여기서 b에 개행(줄바꿈, '\n')이 들어 있음을 알 수 있음!
#이를 없애주려면 형을 바꿔주거나(int),  .rstrip()를 붙여주면 됨!

b = int(sys.stdin.readline()) #int를 이용한 개행제거
print(a, b, a, b)
#1 2 1 2
b = sys.stdin.readline().rstip() #rstip()를 이용한 개행제거
print(a, b, a, b)
#1 2 1 2
```
- 또한 input()과 마찬가지로 split(), int() 등등 사용이 가능함.
- ex)
```python
#1 2를 입력해주면
a, b = map(int, input().split())
print(a, b)
#1 2
import sys
c, d = map(int, sys.stdin.readline().split())
#1 2
```

##### 함수 기초
- 함수의 종류
  - 내장 함수 <-파이썬 개발자가 만듦
    - 파이썬에 기본적으로 포함된 함수(설치X) <-버전마다 바뀔 수 있음
  - 외장함수 <- 다른 개발자
    - import 문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
  - 사용자 정의 함수
    - 직접 사용자가 만드는 함수
- 함수의 정의
  - 특정한 기능을 하는 코드의 조각(묶음) 
- 함수의 기본 구조
  - 선언과 호출(생성, 사용 define & call)
  - 입력(Input) <- 재료
  - 문서화(Docstring) <- 함수에대한 주석, 설명
  - 범위(Scope)
  - 결과값(Output) <- 레시피, 함수 식, return

###### 선언과 로출
- def키워드로 선언
- Fuction body(실행될 코드 블록) 작성
  - Docstring은 함수 body 앞에 선택적 작성 가능 <- 설명서쓸지 여부결정
    - 작성 시에는 반드시 첫 번째 문장에 문자열 ''''''
- 함수는 parameter를 넘겨줄 수 있음 <- print **()** <- 이게 파라미터
- 함수는 동작 후에 return을 통해 결과값 전달

##### 함수의 결과값(Output)
- void function
  - 명시적인 return 값이 없는 경우, None(다른곳에서는 void라고함)을 반환하고 종료 : 반환값이 없는 함수 =  None, void
  - ex) print <- 정확히 말하면 return None이 생략되어 있는 것. 그래서 void 함수를 print하게되면 None을 반환함
- value returning fuction
  - 함수 실행 후, return문을 통해 값 반환
  - return을 하게되면(return을 만나는 순간, 아래는 실행 안됨), 값 반환 후 함수 바로 종료
- print 함수와 return의 차이점
  - print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용), 반환X = 결과가 없다
  - 데이터 처리를 위해서는 return 사용
  - REPL(Read-Eval-Print Loop) 환경(jupyter notebook)에서는 작성된 코드 리턴값을 보여주므로 같은 걸로 착각할 수 있다.
- 두 개 이상의 값 반환
  - return은 한 개만 반환함
  - return x - y, x * y -> 이런식으로 튜플로 묶어서 반환하는 방법이 있다.

##### 함수의 입력(Input)
- Parameter : 함수 정의시 함수 내부에서 사용되는 변수
  - 
- Argument : 함수 호출시 넣어주는 값
  - 필수 Argument : 반드시 전달되어야하는 Argument
  - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값 전달
- Positional Arguments : 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨 - 특별한 사항이 없으면 이게 default값
  - def add(x, y) -> add(x, y) : 순서대로
  - ex)
    ```python
    def add(x, y):
    return x + y

    add(x=2, y=5) #<- keyword argument 자리 바껴도 상관없음
    add(2, y=5) #<- 인자랑 키워드 인자랑 같이 쓸 수 있지만 같이 쓸 경우에는 무조건 인자부터 넣고 키워드 인자를 써야함.
    add(x=2, 5) #<-이건 오류남, 새치기하는 순간 순서가 망가져서 지정은 뒤에부터(앞에서 하려면 전부다 지정)
    ```
- Default Arguments Values
  - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
    - 정의된 것 보다 더 적은 개수의 argument들로 호출될 수 있음.
  - ex) def add(x, **y=0**) -> add(2)로 하더라도 자동으로 add(x, y=0)으로 넣음
- 정해지지 않은 여러개의 Arguments
  - 애스터리스크(Asterisk) 혹은 언패킹 연산자라고 불리는 *덕분
- 가변인자(*args)
  - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
  - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용
    - ex)
```python
def add(*args):
  for arg in args:
    print(arg)
#add(2)
#add(2, 3, 4, 5) 둘 다 가능
``` 
- 패킹 / 언패킹
  - 패킹 <- 묶는 것
    - 여러 개의 데이터를 묶어서 변수에 할당하는 것
  - 언패킹 <- 푸는 것
    - 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
- Asterisk(*)와 가변 인자
  - *는 스퀸스 언패킹 연산자라고도 불리며, 말 그대로 시퀀스를 풀어 헤치는 연산자 
    - 주로 튜플이나 리스트를 언패킹하는데 사용
    - *를 사용하여 가변 인자를 만들 수 있음 <- 파이썬만 갖는 독특한 방식
  - 그냥쓰면 list, 묶어주면? tuple
- 가변 키워드 인자
- 가변 인자 & 가변키워드
  - 너무 많이쓰면 다른사람이 보기에 이해하기 힘들 수 있음.
  - ex)
```python
numbers = (1, 2, 3, 4, 5) # 패킹
print(numbers) # (1, 2, 3, 4, 5)

a, b, c, d, e = numbers # 언패킹
print(a, b, c, d, e) # 1 2 3 4 5

values = [1, 2, 3, 4, 5]
print(*values) # = print(1, 2, 3, 4, 5) 별표가 없다면 ([1, 2, 3, 4, 5])가됨
#언패킹 -> 1, 2, 3, 4, 5 argument의 언패킹 *사용 cf) 패킹은 parameter

values = [1, 2, 3, 4, 5]
print(*values, sep="\n") #for문 안쓰고도 할 수 있음

'''
1
2
3
4
5
'''

def add2(*args): #parameter의 패킹 *사용, 보낼때 갯수 상관없이 여러개 입력해도 튜플 형식으로 만들어줌
    for arg in args:
        print(arg)

add2(2, 3, 4, 5)

def print_family_name(father, mother, *pets): #*pets 자리에 여러개가 입력해도 괜찮음
  print(f'아버지 : {father}')
  print(f'어머니 : {mother}'
  print('반려동물들..')
  for name in pets:
    print(f'반려동물:{name}')

print_family_name('아부지', '어무이', '멍멍이', '냥냥이')
'''
아버지 : 아부지
어머니 : 어무이
반려동물들..
반려동물: 멍멍이
반려동물: 냥냥이
'''
```
- 가변 키워드 인자(**kwargs)
  - 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
  - **kwargs는 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현
  - ex)
```python
def family(**kwargs):
  for key, value in kwargs.items():
    print(key,":", value)
family(father='아부지', mother='어무이', baby='아기')
'''
father : 아부지
mother : 어무니
baby : 아기
'''

def print_family_name(father, mother, **pets):
  print("아버지 : ", father)
  print("아버지 : ", father)
  if pets:
    print("반려동물들..")
    for species, name in pets.items():
      print(f'{species} : {name}')
print_family_name('아부지', '어무이', dog='멍멍이', cat='냥냥이')
'''
아버지 : 아부지
어머니 : 어무이
반려동물들..
dog : 멍멍이
cat : 냥냥이
'''

def print_family_name(*parents, **pets):
  print("아버지 : ", parents[0])
  print("어머니 : ", parents[1])
  if pets:
    print("반려동물들..")
    for title, name in pets.items()
      print('{} : {}'.format(title, name))

print_family_name('아부지', '어무이', dog='멍멍이', cat='냥냥이')
'''
아버지 : 아부지
어머니 : 어무이
반려동물들..
dog : 멍멍이
cat : 냥냥이
'''
```

##### 함수의 범위(Scope)
 - 특정 공간, 지역, **방**
 - 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
 - scope
   - global scope : 코드 어디에서든 참조할 수 있는 공간
   - local scope : 함수가 만든 scope. 함수 내부에서만 참조 가능
 - variable
   - global variable : global scope에 정의된 변수
   - local variable : local scope에 정의된 변수
 - 변수 수명주기(lifecyclel)
   - 변수는 각자의 수명주기(lifecyle)가 존재
     - built-in scope <- 파이썬이 존재하는 한 존재
       - 파이썬이 실행된 이후부터 영원히 유지
       - global scope <- 프로그램이 살아있는 한 존재
         - 모듈이 호출된 시점 이후 인터프리터가 끝날 때까지 유지
       - local scope
         - 함수가 호출될 때 생성되고, 함수가 종료(return)될 때까지 유지
 - 이름 검색 규칙(Name Resoultion)
   - 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
   - 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule이라고 부름
     - **L**ocal scope : 지역범위(현재 작업 중인 범위)
     - **E**nclosed scope : 지역 범위 한 단계 위 범위
     - **G**lobal scope : 최상단에 위치한 범위
     - **B**uilt-in-scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든것 ex) print())
     - Built-in Scope <- 파이썬
       - Global scope <- 프로그램
         - Enclosed scope
           - Local scope 
             - 아래서부터 윗단계까지 하나씩 탐색을함 <- 리모컨찾기 대작전
   - 함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음.
   - ex1) print(sum) #<built-in function sum> 이런식으로 검색 가능, 앞에서 sum선언해주면 선언한걸로 나옴 <- LEGB원리에 의하여
   - ex2)
    ```python
    a = 0
    b = 1
    def enclosed()
        a = 10
        c = 3
        def local(c):
            print(a, b, c) # 10 1 300 #local(300)이 들어옴으로 300이 들어감
        local(300)
        print(a, b, c) # 10 1 3
    enclosed()
    print(a, b) # 0 1 #방으로 그려서 하면 보기편함
    ```
    - global
      - parameter을 global로 쓸 수 없다
    - nonlocal
      - 글로벌은 변수를 함수 안에서 밖으로바꿀때
      - nonlocal 함수안에 함수 이럴떄 씀, 이중으로 끼워져 있을때 내 바로 위에녀석을 바꾸고 싶을 때 쓰는거
        - 만약에 바로 위에 없더라도 다음 단계가서 찾고 없으면 그 다음 단계에서 찾는 식으로 한다.
      - global과 nonlocal과 거의 같다.

 - 

##### 함수 응용
- 내장함수(Built-in Functions)
  - 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음
- map
  - 컨테이너 안에 있는 각각의 원소에 앞의 함수를 각각 전부 적용(문자**열**도 가능)
  - map(function, iterable)
    - function에 있어서는 내장함수가 아니고 직접 정의한 함수도 사용가능(lambda도 가능)
  - ex)
```python
map(int,["1". "2","3"]) #1 2 3
map(int,"123") #1 2 3

map(int, input().split)
#map(int, ["1", "2"].split

``` 
  
- filter
  - filter(function, iterable)
  - iterable한 녀석들을 함수에 다 넣어서 True인 것들을 filter object로 반환
  - ex)
```python
def odd(n):
  return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result)) #<filter object at ~> <class 'filter'>
print(list(result)) #[1, 3]
```
- zip
  - zip(*iterables)
  - 세로로 묶는다!
  - ex)
```python
girls = ['jane', 'ashley']
boys = ['justin', 'eric']
pair = zip(girls, boys)
print(pair, type(pair)) #<zip object at ~> <class 'zip'>
print(list(pair)) #[('jane', 'justin), ('ashley', 'eric')]
```
- split
  - 문자열.split(sep = '구분자', maxsplit = 분할횟수) <-sep, maxsplit은 생략가능
    - 구분자를 기준으로 분할횟수만큼 잘라서 리스트로 만든다!
  - ex1)
```python
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

coffee = orders.split(',')
print(len(coffee))  # 14잔
coffee.sort(reverse=True)

a = list(set(coffee))
a.sort(reverse=True)
print(a)
```
  - ex2) input에 123 넣는 경우
  - split의 여부에 따라 띄어쓰기 차이가 생김.
```python
a, b, c = map(int, input().split()
#1 2 3
a, b, c = map(int, input())
#123
```

- print
  - print("문자열", sep 옵션, end 옵션)
    - sep 옵션 : 출력할 때 출력 값들 사이에 넣어줄 구분자. dafault = 개행(줄바꿈)
    - end 옵션 : 출력할 떄 출력 값들 사이에 넣어줄 구분자. dafault = 공백(띄어쓰기)
  - 출력하고 싶은 문자열(=데이터)을 출력!
  - ex)
```python
a = 'happy'
b = 'hacking'

print(a, end="@") #default 값은 '\n'
print(b)
#happy@hacking

print(a, b) sep = "\n" #default 값은 ','    
'''
happy
hacking
'''
print(a, b, c) = map(int, input().split())
>>>1 2 3
print(a, b, c, sep='&', end='!')
# 1&2&3!
```
- ascii 아스키 문자 내장함수
  - ord() 문자 -> 숫자
  - chr() 숫자 -> 문자
  - 응용 문제에서 끝까지 간다음에 되돌오게 하려면 나머지를 활용!
    - [0, 1, 2, 3] 에서 돌고 싶으면 4로 나눈 나머지로 하게되면 됨.

- **람다(lambda) 함수**
  - 익명함수, 한 줄로 간단하게 함수를 표현
  - lambda[parameter] : 표현식
  - 특징
    - return문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
    - 일회용으로 쓸때 유용(람다도 선언하고 쓰는 것, 단지 이름이 없을뿐)
  - 장점
    - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
    - def를 사용할 수 없는 곳에서도 사용가능
  - ex)
```python
minus_two = lambda x: x -2 # 변수안에 함수를 넣어서
result = minus_two(5) # 변수를 이용해서 함수를 호출하는 모양으로 사용가능
print(result) # 3
minus_numbers = list(map(lambda x : x-2, [5, 6])) # map 안에 함수인자에 람다함수를 넣어서 사용할 수 있음.
print(minus_numbers) # [3, 4]
```
- **재귀 함수(recursive function)**
  - 재귀함수를 쓰라고 하면, 1) 종료조건, 2)점화식 이렇게 두개 써주면됨.
  - ex)
```python
if n < 2: #1) 종료조건
  return ###

else:
  return ### 2) 점화식, 이런식으로 써주면됨
```
  - 자기 자신을 호출하는 함수로, 자기 자신을 호출하며 점점 깊게 들어감
    - **BASE-CASE(재귀탈출조건)**과 **점화식**으로 이루어짐
  - 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
    - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음(ex)점화식)
      - 점화식(재귀식) : 수열을 식으로 나타낸 것
    - 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
  - 상위 문제를 해결하기 위해, 그 보다 좁은 범위의 하위 문제를 먼저해결
    - a(n+1) = a(n) + k <- a(n+1)(상위문제)을 해결하기위해 a(n)(좁은 범위의 하위 문제)을 먼저 해결 (여기서의 n, n+1은 밑으로 들어감)
  - 모든 재귀 함수는 반복문으로 표현이 가능하다.
    - 무한루프가되니까 종료조건이 필요하다. <- 아니면 무한루프 하다가 오류남, 파이썬에서는 최대 재귀 깊이는 1000으로 제한됨.
    - 그럼 왜 쓰냐? <- 더 직관적이고 비교적 식이 간결하기 때문, 대신 이해하기 비교적 어려움
  - 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
  - ex) factorial
    4! = 4 * 3! = 4 * 3 * 2 * 1
    3! = 3 * 2! = 3 * 2 * 1
    2! = 2 * 1 = 2
    1! = 1

    f(4) = 4 * f(3)
    f(3) = 3 * f(2)
    f(2) = 2 * f(1)
    f(1) = 1 <- base case(끝나는 곳에) 수렴>
  - 반복문 VS 재귀함수
    - 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수 사용
    - 재귀 호출은 변수 사용을 줄여줄 수 있음
    - 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래걸림


### 기타tip
##### palindrome
- 면접에도 자주나옴
- 정석은 앞뒤 문자 하나하나 비교하는것임.
- [::-1]이거는 파이썬스러운 풀이법