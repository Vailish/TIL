1. 객체지향 : 확장성
2. 객체 : 역할, 책임, 협력
3. 4대 : 추상화 캡슐화 다형성 상속

- class : 설계도
- 인스턴스 : 리스트의 객체
- 객체 : 객체

### 객체
- 배틀쉽 예시
  - 역할 : 플레이어
  - 책임 : sea를 깔 책임이 있음
  - 협력 : 요청에따른 응답

### 객체지향의 핵심
- **추상화** : 불필요한 것은 걷어내고, 필요한 것만 보여주는 것 (구조(원리)는 몰라도 사용 가능한 것, ex)스마트폰) - 컴퓨터 공학을 관통하는 개념
- 캡슐화 : 객체간 간섭이 불가 why? 추상화이기 때문(**어떻게 동작을 하든 상관 없이 결과만 받으면 됨**)
  - 캡슐화때문에 객체간 간섭이 불가 == 객체에게 자율성을 부여함 -> 객체.변수로 바꾸지 않음, 인스턴스 메서드에 역할을 주었고 바깥에서 직접 바꾸지 않고 요청만함 : 그럼 그 메서드를 실행하는 건 객체의 책임
  - public
  - protected
  - private
- 다형성 : 결과만 얻으면 되기때문에 다른 객체에게 요청해도 됨(어떤 객체가 와도 상관 없다. 난 결과만 잘 받으면 된다)
- 상속 : 어떤 객체가와도 괜찮다 -> 공통점을 묶어서 줘도 된다.
- 고로, **추상화**로부터 나오는 개념들이다.

```python
a = '123'

b = list(a) # a == 생성자, list() == 클래스함수, b == list의 인스턴스
#역할 == 리스트 #책임 == 리스트를 만들고, 순서를 저장하고, 수정가능한 ... ,협동
b.append(3) # b라는 리스트의 행동(메서드)
print(b)

#파이썬은 모두 객체다 ex) list를 보더라도 mutable sequence라는 클래스를 상속받고 그 위에 contain이라는 클래스를 상속 받은 것이며, 그렇기 때문에 b는 list의 인스턴스가 된다. 따라서 추상화~상속 전부 됨.
```

클래스(추상화 하는 도구) == type(ex)list, 객체를 추상화하는 것)
- 불필요한 세부사항 없애고, 하나로 묶는다 == 이 자체가 추상화의 의미와 같음

### OOP속성
```
class
  클래스변수(클래스속성) - 클래스내 모든 객체가 같이 갖는 값
  def
    인스턴스변수 - 각각 인스턴스마다 따로 갖는 값
```

### namespace 와 function의 scope와 똑같은 개념
- 자기가 속한 구역을 먼저 탐색한 후 점차 넓은 구역으로 나가면서 탐색함.
  - 이런 원리 때문에 오버라이딩(덮어쓰기)를 하면 클래스와 인스턴스를 다르게 해줄 수 있음.

### 메서드
- 인스턴스 메서드
- 클래스 메서드
- 스태틱 메서드

##### 인스턴스 메서드
- 첫 인자는 무조건 self로 하자 : 개발자간 약속 (다른걸로 해도 되긴함)


```python
class Person
  def __init__(self, name):
    self.name = name

    def __str__(self): # 프린트 함수와 관련되 매직 메서드(str로 나와라!) 이걸 넣어주면 return값으로 출력해줌, 없을 시 object at 실제위치 로 나옴
      return self.name
    
    def __add__(self, other): # 프린트에서 + 는 어떻게 표현할 것인가
      return self.name + other.name
    
    def __del__(self):
      print('삭제되었습니다.')

person1 = Person('vailish') # 객체이자 인스턴스
person2 = Person('john')
print(person1) # vailish
print(person1 + person2) # vailishjohn
person3 = person1 # 둘은 같은 주소값
del person1 # del은 객체가 아니라 변수가 객체를 가르키는 참조를 없앤다(포스팃을 떼어낸다. == 객체는 살아있다. 연결점만 있을뿐, 삭제가 안되었기 때문에(가리키는 녀석이 하나 더 있기때문에 삭제를 바로 안함, 1개일 때는 바로 삭제함) 프린트가 먼저 출력됨, 그리고 나서 출력되는 이유는 그냥 프로그램이 끝났기 때문임.)
print(person3.name)

```
del 2개 이상 가르키는 녀석이 있는 경우 다 지워버리려면 어캐해야하나?

##### 클래스 메서드
- 모습에서는 @가 있거나 cls가 인자로 들어있거나
- 인스턴스 메서드는 클래스변수(조회만 가능), 인스턴스 변수 둘 다 사용이 가능

```python
class Person
  counts = 0
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def call_name(self):
    return f'CodingGoSu. {self.name} 입니다!'

  @staticmethd #스태틱 메서드 :고정된값 불러올때 쓸거, 어떠한 인스턴스에도 클래스도 영향X (self, cls 둘 다 없음)
  def hello(): <- self 넣을 필요없음
    return '안녕하세요!'

person1 = Person('vailish', 20)
print(person1.call_name())
print(person1.hello())
```
##### 메서드 오버라이딩
- 상속 받을 거긴 한데 조금 변형을 주고 싶다 이럴때 쓰면됨
- 같은 이름으로 만들어주면 만든걸로 사용함



##### 캡슐화
__age로 접근하면 호출 불가라고는 하지만 실제로는 그 앞에 클래스이름을 넣어 이름을 작성을 한것, 즉 그 이름을 다 알게되면 똑같이 호출을 할 수는 있음.
ex) Person__age 이런식

##### getter, setter
- 정보를 직접 뜯지말고 요청 응답하는 방식으로 진행하자 (패러다임이 객체지향이니까)(함수로 만들어서)
```python
class Person:
  counts = 0

  def __init__(self, name, age):
    self.name = name
    self.__age = age
  
  def get_age(self) : #이게 getter 함수를 통해서 응답으로 값을 받음
    return self.__age

  def set_age(self, age): #setter, 함수를 통해서 수정요청, 객체에 자율성부여
    self.__age = age

  @property
  def age(self): # 여기 함수이름 age로 호출하는거임. ex) person1.age()
    return self.__age
  
  #@age.setter
  #def age(self, new_age):
  #  if new_age <= 19:
  # 대충 이런식    

person1 = Person('vailish', 25)
print(person1.get_age())

person1.set_age(30)
print(person1.get_age())

person1.age = 40 #이렇게 하면 안되지만(암묵적) 이렇게 직접적으로 바꿔주면 편하지 않을까?(내부는 그대로 동작하면서 외부적으로 이렇게 쓸 수 있게 해줌) <- property 객체 , property decoration

```

# 기타
* 스태틱메서드
  * 스태틱은 설계도를 지가 가지고있다? ->  이 말은 스태틱 메서드는 클래스와 같은 영역이고, 인스턴스만 별도의 영역이다.

---

# OOP
- 객체지향 프로그래밍(OOP)
  - 객체 지향 프로그래밍이란?
  - OOP 기초
    - 객체 / 인스턴스 / 클래스
    - 클래스
    - 메서드
  - 객체지향의 핵심 개념
    - 추상화
    - 상속
    - 다형성
    - 캡슐화
  - 에러와 예외

### 객체지향 프로그래밍(OOP)
- Object-Oriented Programming, OOP는 컴퓨터 프로그래밍의 패러다임(방법론) 중 하나이다.
  - 객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위, 즉 "객체"들의 모임으로 파악하고자 하는 것이다. 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다.
- 객체지향 프로그래밍(구조중심 <- for확장성>)
  - 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
  - 데이터와 기능(메서드) 분리, 추상화된 구조(인터페이스)
  - ex1) 객체(꾸러미) = 정보 + 행동 (변수+함수) /// 강아지 == 리트리버 + 먹기, 자기
  - ex2) 콘서트 == 가수객체(키+노래,춤), 감독 객체, 관객 객체
- 객체지향 프로그래밍이 필요한 이유
  - 추상화 : 현실 세계를 프로그램 설계에 반영(복잡한거 숨기고 필요한거만 드러냄)
- 객체지향의 장/단점
  - 장점
    - 클래스 단위로 모듈화시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
    - **필요한 부분만 수정하기 쉽기 때문에 프로그램의 유지보수가 쉬움**
  - 단점
    - 설계 시 많은 노력과 시간이 필요함
      - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
    - 실행 속도가 상대적으로 느림 (사람이 편하면 컴퓨터가 힘듦)
      - 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름
        - 리모컨 과같은 작은 칩들은 객체지향이 힘듦

##### VS 절차지향 프로그래밍
- 절차를 중심으로 쭉 길 따라 가듯이 만듦.(기능중심)
  - 이 방법시 중간에 하나를 변경하면(동작 하나를 바꾸면), 전반적으로 변경 해줘야함
    - 또한, computer1_attack, computer2_attack ... 이런식으로 **변수가 많아지면(프로그램이 커지면)**, 다 써줘야하기때문에 매우 복잡해짐 -> 클래스(ex)class Computer)로 만들어 주면(인스턴스로 들어가기 때문에, 인스턴스만 만들면 다른 속성은 써줄 필요가 없기때문에) 간단히(깔끔히) 처리 가능함.
  - 이러한 문제를 해결하기 위해 객체지향 프로그램이 등장하기 시작함. : 객체만 변경해주면 됨.
- Global data
  - function1
    - function3
      - function4
  - function2
    - function3
    - function4
  - function5
- 기본적으로 알고리즘 풀이하듯 위에서 아래로 순차적으로 작동하게끔 만드는 패러다임

### OOP 기초

##### 객체(컴퓨터 과학)
- 컴퓨터 과학에서 객체 또는 오브젝트(object)는 **클래에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것**으로 프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미하며, 변수, 자료구조, 함수 또는 메서드가 될 수 있다.
- 객체 = **속성**과 **행동**으로 구성된 모든 것
  - ex) 가수 이찬혁
    - 속성(정보, 변수) : 직업==가수, 생년월일 == 1996년 9월 12일, 국적==대한민국
    - 행동(동작, 함수-메서드) : 랩하기()==어느새부터 힙합은 안 멋져~, 댄스()==두둠칫~~둠칫~, make_some_noise == 워어어우어~
    - 이찬혁.랩하기(), 이찬혁.직업 = 가수 이런식으로
    - 클래스(설계도) == 가수, 객체(실제 사례) == 이찬혁
      - 보통 가수, 평균적인 가수는 머리속에만 존재, 실제로는 예시에서만 존재
      - 클래스 == 강아지, 객체 == 리트리버, 시츄 ...
- 객체 vs 인스턴스
  - 인스턴스 : 클래스로 만든 객체 (특정 타입의/클래스의 인스턴스)
  - 객체 vs 인스턴스
    - 이찬혁은 객체다(O), 이찬혁은 인스턴스다(X), 이찬혁은 가수의 인스턴스다(O)
    - 클래스(가수, 타입(list))와 객체(실제 사례)
      - 클래스를 만든다 == 타입을 만든다
  - 객체(object)는 특정 타입의 인스턴스(instance)이다
    - 123, 900, 5는 모두 int의 인스턴스
    - 'hello', 'bye'는 모두 string의 인스턴스
- 파이썬은 모든 것이 **객체(object)**
  - 파이썬의 모든 것엔 속성과 행동이 존재
  - ex1) [3, 2, 1].sort() <- 리스트.정렬(), 객체.행동()
  - ex2) "banana".upper() <- 문자열.대문자로(), 객체.행동() (문자열 정보 : iterable, for문 돌 수 있음, etc)
  - [1, 2, 3], [1],[],['hi'] 모두 리스트 타입(클래스)의 객체
  - '', 'hi', '파이썬' 모두 문자열 타입(클래스)의 객체
- 객체(object)의 특징
  - 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?
  - 속성(attribute) : 어떤 상태(데이터)를 가지는가?
  - 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
  - python의 객체와 클래스 : 객체(Object) = 속성(Attribute) + 기능(Method)

##### 객체와 클래스 문법
- 클래스와 인스턴스  
  - 클래스 정의   : class MyClass: <- F보통 M이 대문자(첫자 대문자)
  - 인스턴스 생성 : my_instance = MyClass()
  - 메서드 호출   : my_instance.my_method()
  - 속성          : my_instance.my_attribute
  - 파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스
  - 클래스 : 객체들의 분류 / 설계도(class)
  - 인스턴스 : 하나하나의 실체 / 예(instance)
  - ex)
```python
class Person: #정의
    pass
print(type(Person)) # <class 'type'>

person1 = person() # 사례

print(isinstance(person1, person)) # True
print(type(person1)) # <class '__main__.person'>
```
- 객체 비교하기
  - ==
    - 동등한(equal)
    - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
  - is
    - 동일한(identical)
    - 두 변수가 동일한 객체를 가리키는 경우 True
  - ex)
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b, a is b) # True(생긴게) False(동일주소, 온전히 동일)


a = [1, 2, 3]
b = a

print(a == b, a is b) # Ture True
```

### OOP 속성
- 속성(데이터, 정보, 상태) -> 변수
  - 특정 대ㅔ이터 타입/클래스의 객체들이 가지게 될 상테/데이터를 의미
  - 클래스 변수 / 인스턴스 변수 가 존재
  - ex)
```python
class Person:
    blood_color = 'red' # 클래스 변수 #같이 쓰는 변수
    population = 100 # 클래스 변수

    def __init__(self, name):
        self.'지민' = '지민' # 인스턴스 변수 # 인스턴스마다 따로 쓰는 변수 / name = '지민'
person1 = Person('지민')
print(person1.name) #'지민
```
- 인스턴스 변수
  - 인스턴스 변수란?
    - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
    - 각 인스턴스들의 고유한 변수
  - 생성자 메서드(__init__)에서 self.<name>으로 정의
  - 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당
  - ex)
```python
class Person:
    
    def __init__(self, name): #인스턴스 변수 정의 # 쓸때는 self는 자동으로 들어감. 하지만 정의할 때는 문법상 필수
        self.name = name
    
    #def __init__(self,name, mbti) 예시
    #    self.mbti = mbti
    #    self.mbti

 john = Person('john') # 인스턴스 변수 접근 및 할당
 print(john.name) # john
 john.name = 'John Kim' # 인스턴스 변수 접근 및 할당
 print(john.name) #John Kim
```
- 클래스 변수
  - 클래스 변수
    - 한 클래스의 모든 인스턴스가 공유하는 값을 의미
    - 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
    - ex) 특정 사이트의 User 수 등은 클래스 변수를 사용해야 함
  - 클래스 선언 내부에서 정의
  - <classname>.<name>으로 접근 및 할당
  - 클래스 변수 : 공용 /// 인스턴스 변수 : 각자 개인용
    - 인스타그램 유저수 정보 : 클래스 변수로 만들어야함
      - **공용이니까, 공통** ex) 사람피는 누구에게 물어봐도 붉은색
      - iterable : class 변수
      - 공통임? O -> 클래스변수, X -> 인스턴스 변수
  - ex)
```python
Class Circle():
    pi = 3.14 # 클래스 변수 정의

    def __init__(self, r): # 생성자
        self.r = r # 인스턴스 변수
c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi) # 3.14 # 인스턴스 -> 클래스 변수
print(c1.pi) # 3.14
print(c2.pi) # 3.14

Circle.pi = 5 # 클래스 변경 함수
print(Circle.pi) # 5
print(c1.pi) # 5
print(c2.pi) # 5

#인스턴스로도 클래스 변수 조회가 가능(LEGB Rule처럼)
```
  - 클래스 변수 활용(사용자 수 계산하기)
    - 사용자가 몇명인지 확인하고 싶다면?
      - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정하면 됨.
      - ex)
```python
class Person:
  count = 0
  # 인스턴트 변수 설정
  def __init__(self, name):
      self.name = name
      Person.count += 1
  
person1 = Person('아이유')
person2 = Person('이찬혁')
```
  - 클래스 변수와 인스턴스 변수
    - 클래스 변수를 변경할 때는 항상 클래스.클래스변수 형식으로 변경
      - 클래스 변수 변경 해주면 문제해결 가능(인스턴스에서 건드리지 마라) , 클래스 변수를 바꾸고 싶으면 클래스.클래스변수를 인스턴스 변수를 바꾸고 싶으면 인스턴스.인스턴스변수
    - 클래 인스턴스 변수x -> 클래스 변수를 가져옴 : 이부분이 어려움 글로벌변수 찾아가는거랑 비슷함
    - ex)

```python
Class Circle():
    pi = 3.14 # 클래스 변수 정의

    def __init__(self, r):
        self.r = r #인스턴스 변수

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi) # 3.14 # 인스턴스 -> 클래스 변수
print(c1.pi) # 3.14
print(c2.pi) # 3.14

Circle.pi = 5 # 클래스 변경 함수
print(Circle.pi) # 5
print(c1.pi) # 5
print(c2.pi) # 5

c2.pi =5 #인스턴스 변수 변경
print(Circle.pi) # 3.14 (클래스 변수)
print(c1.pi) # 3.14 (클래스 변수)
print(c2.pi) # 5 (새로운 인스턴스 변수가 생성됨)
```

### OOP 기초
##### 메서드    
- 메서드
  - 클래스 안에 있는 함수
  - 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)
```python
#p43 코드
class Person:
  
  def talk(self):
    print('안녕')

  def eat(self, food):
    print(f'{food}를 냠냠')

person1 = person()
person1.talk() # 안녕
person1.eat('피자') # 피자를 냠냠
person1.eat('치킨') # 치킨을 냠냠
```

##### 인스턴스 메서드 (self가 있으면!)
- 메서드 종류(Python Methods)
  - 인스턴스 메서드(Instance Methods)
    - 인스턴스 (변수는 아니지만 변수와 같은것) 처리
    - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
    - 클래스 내부에 정의되는 메서드의 기본
    - 호출 시, 첫번째 인자로 인스턴스 자기자신(self)이 전달됨 : 자동
    - ex)
```python
class MyClass:
    def instance_method(self, arg1, ...): #self가 있으면 instance만 있어도 됨

my_instance = MyClass()
my_instance.instance_method(...)
```
    - self
      - 인스턴스 자기자신
      - 파이썬에서 인스턴스 메서드 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
        - 매개변수 이름으로 self를 첫 번째 인자로 정의
        - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙
    -  생성자(constructor) 메서드
       -  인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
       -  인스턴스 변수들의 초기값을 설정
          -  인스턴스 생성
          -  __init__메서드 자동 호출
          - ex)
```python
class Person

    def __init__(self):
        print('인스턴스가 생성되었습니다.')


person1 = person() # 인스턴스가 생성되었습니다.

class Person:

    def __init__ (self, name):
        print(f'인스턴스가 생성되었습니다. {name}')

person1 = person('지민') # 인스턴스가 생성되었습니다. 지민
```
    - 매직 메서드
      - Double underscore(던더, __)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 혹은 매직 메서드라고 불림
      - 특정 상황에 자동으로 불리는 메서드
      - ex) ex) pirnt를 바꾸고 싶으면 __str__(self) 를 바꾸면됨
        - __str__(self) : print, __len(self)__, __repr__(self)
        - __It__(self, other), __le__(self, other), __eq__(self, other) : ==
        - __gt__(self, other), __ge__(self, other), __ne__(self, other)
      - 예시
        - 객체의 특수 조작행위를 지정(함수, 연산자 등)
          - __str__ : 해당 객체의 출력 형태를 지정
            - 프린트 함수를 호출할 때, 자동으로 호출
            - 어떤 인스턴스를 출력하면 __str__의 return 값이 출력
          - __gt__ : 부등호 연산자(>, greater than)
    - 소멸자(destructor) 메서드
      - 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드
      - ex)
```python
class Person: @51~52코드

```
  - 클래스 메서드(Class Methods) : 클래스 처리
    - 클래스 메서드
      - 클래스가 사용할 메서드
      - @classmethod 데코레이터를 사용하여 정의
      - 호출 시, 첫번째 인자로 클래스(cls)가 전달됨
      - ex)
```python
class Person:
    @55
```
    - 데코레이터 (@, 모자쓴다고 생각하면 됨)
       - 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
       - @ 데코레이터(함수명) 형태로 함수 위에 작성
       - 순서대로 적용되기 때문에 작성 순서 중요
       - 쓰는이유 : 꾸며주는 얘를 함수로 만들고 쓰면 나중에 갯수가 많아졌을 때나 수정할 때 편리함. <- 얘만 바꾸면됨
         - 얘도 불편해서 데코레이터가 나옴
       - 데코레이터 사용 예시 
         - ex) 데코레이터 없이 함수 꾸미기
```python
@@57
```
    - 클래스 메서드와 인스턴스 메서드
      - 클래스 메서드 -> 클래스 변수 사용
      - 인스턴스 메서드 -> 인스턴스 변수 사용
      - 그렇다면 인스턴스 변수, 클래스 변수 모두 사용하고 싶다면?
        - 클래스는 인스턴스 변수 사용이 불가능
        - 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용이 가능
      - 스태택 메서드
        - 스태틱 메서드
          - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드
        - 언제 사용하는가?
          - 속성을 다루지 않고 단지 기능(행동)만을 하는 메서드를 정의 할 때, 사용
          - ex)
```python
@@@62
class Person:
    count = 0 # 클래스 변수
    def __init__(self, name): #인스턴스 변수 설정
        
```
    - 인스턴스와 클래스 간의 이름 공간(namespace)
      - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
      - 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
      - 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색
```python
@@65

print(p1.name) # unknown #클래스변수 문법은 같은데 결과가 다름
print(p2.name) # Kim #인스턴스변수
```
  - 정적 메서드(Static Methods) : 나머지(클래스와 인스턴스와 상관 없은 것들)

### 메서드 정리
@68
- 메서드 정리
  - 인스턴스 메서드
    - 호출한 인스턴스를 의미하는 **self** 매개 변수를 통해 인스턴스를 조작
  - 클래스 메서드
    - 클래스를 의미하는 **cls** 매개 변수를 통해 클래스 조작
  - 스태틱 메서드
    - 클래스 변수나 인스턴스 변수를 **사용하지 않는 경우**에 사용
      - 객체 상태나 클래스 상태를 수정할 수 없음
    - ex) add_age(1980) ---(+1)> 1981 이런 식으로 간단한거 하거나 만들고 싶으면 쓰라고 만들어 놓은 것
  - ex)
```python
class MyClass:

  def method(self): #self대신 다른거 써도되긴함, 하지만 개발자들끼리의 약속, self쓰자 (이와 같이 강제되지는 않지만 약속적인 부분이 많음)
    return 'instance method', self

    @classmethod #개발자가 클래스 메소드를 만들어 놓은걸 쓰면됨
    def classmethod(cls):
        return 'class method', cls
    
    @staticmethod
    def staticmethod():
        return 'static method'

# 인스턴스 메서드를 호출한 결과
obj = MyClass()

print(obj.method()) # ('instance method', <__main__.MyClass at 0x185~~~>)
print(MyClass.method(obj)) # 위와 같음 <- 권장되는 방법은 아님(되긴 된다) 위의 방법으로 하자>

# 클래스 자체에서 각 메서드를 호출하는 경우
# - 인스턴스 메서드는 호출할 수 없음
print(Myclass.classmethod()) #('class method', __main__MyClass)
print(Myclass.staticmethod()) # static method
MyClass.method() # method() missing 1 required positional argument : 'self'

#인스턴스는 클래스 메서드와 스태틱 메서드 모두 접근할 수 있음
#되는 이유는 좁은 범위에서 상위 범위로 검색하기때문
print(obj.classmethod()) # ('class method', <class '__main__MyClass'>)
print(MyClass.classmethod()) # ('class method', <class '__main__MyClass'>)
print(obj.staticmehtod()) # static method
```

##### 객체 지향 프로그래밍?
- 객체 <-> 객체 (방법론, 패러다임)
- 정보, 행동
  - 정보 : 클래스변수, 인스턴스변수
  - 행동 : 클래스 메서드, 인스턴스 메서드, 매직메서드

### 객체 지향의 핵심개념
- 객체지향의 핵심 4가지
  - 추상화 : 
    - 현실 세계를 프로그램 설계에 반영 - 복잡한 것은 숨기고, 필요한 것만 들어내기
    - ex)
```python
class Student:
  def __init__(self, name,age, gpa):
    @@@78
```
  - 상속
    - 두 클래스 사이 부모-자식 관계를 정립하는 것
    - 클래스는 상속이 가능함
      - 모든 파이썬 클래스는 object를 상속 받음
    - ex) class ChildClass(ParentClass): #받고싶은거,ParentClass 주세요
             pass
    - 정보, 행동 A(주는 클래스) -> B(받는 클래스) 만든거 아닌데 부모 사용가능
    - 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약조건을 모두 상속 받음
    - 부모클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐
    - ex) 
```python
# 상속 없이 구현하는 경우 1
class Person:
    def __init__(self, name, age):
      self.name = name # 인스턴스 변수
      self.age = age # 인스턴스 변수

    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

s1 = Person('김학생', 23)
s1.talk() # 반갑습니다. 김학생입니다.

p1 = Person('박교수', 49)
p1.talk() # 반갑습니다. 박교수입니다.

s1.gpa = 4.5
p1.department = '컴퓨터공학과'

# 상속 없이 구현하는 경우 2 @82
class Professor:
  def __init__(self, name, age, department):
      self.name = name
      self.age = age

#상속
#상속을 통한 메서드 재사용
class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      self.department = department
    
    def talk(self): #메서드 재활용
        print(f'반갑습니다. {self.name}입니다.')  

        #더 넓은 범위로 탐색
```
      - 상속 관련 함수와 메서드
        - isinstance(object, classinfo) : classinfo의 instance거나 subclass*인 경우 True
          - ex)
```python
@85
```
        - issubclass(class, classinfo)
          - class가 classinfo의 subclass면 True
          - classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사
            - ex)
```python
@@86
```
        - super()
          - 자식클래스에서 부모클래스를 사용하고 싶은 경우
          - ex)
```python
@87
```
    - 상속 정리
      - 파이썬의 모든 클래스는 object로부터 상속됨
      - 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
      - super()를 통해 부모 클래스의 요소를 호출할 수 있음
      - 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
      - 상속관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색
    - 다중 상속
      - 두 개 이상의 클래스를 상속 받는 경우
      - 상속받은 모든 클래스의 요소를 활용 가능함
      - 중복된 속성이나 매서드가 있는 경우 상속 순서에 의해 결정됨
      - ex)
```python
@90
```
  - 다형성
  - 캡슐화

---

### 에러/예외 처리(Error/Exception Handling)
- 디버깅
- 에러와 예외
- 예외 처리
- 예외 발생 시키기

##### 디버깅
- 버그란?

##### 에러와 예외
- 문법 에러(Syntax Error)
- 예외(Exception)




##### 참고예시
```python
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, dog_name, dog_kind): # 객체생성
        self.dog_name = dog_name
        self.dog_kind = dog_kind
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def bark(self):
        print("왈왈")

    def __del__(self):
        Doggy.num_of_dogs -= 1

dog1 = Doggy('malang', 'Golden_Retriever')
dog2 = Doggy('snow', 'Husky')

print(Doggy.num_of_dogs, Doggy.birth_of_dogs)
print(dog1.bark())

del dog1
print(Doggy.num_of_dogs)
```