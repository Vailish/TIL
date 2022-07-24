### 제어문
- 제어문
    - 조건문 
    - 반복문
- 파이썬은 기본적으로 위에서 아래로 차례로 명령 수행
- 코드를 선택적으로 실행(분기/조건)하거나 계속하여 실행(반복)하는 제어가 필요함
- 순서도(flowchart)로 표현가능

##### 복수 조건문
- 참/거짓을 판단할 수 있는 조건식
- 형식
  ```python
  if a > 5:
      print('5 초과')
  else:
      print('5 이하')
  print(a)
  ```

##### 복수 조건문
- 동시에가 아니라 하나씩 검사함.
- if 아래에 elif 넣어주면됨.

##### 중첩 조건문
- 조건문에 조건문 중첩
- 형식(들여쓰기 조심)
  ```python
  if 조건:
      #code block
      if 조건:
          #code block
  ```

##### 조건 표현식
- 삼항 연산자(Ternary Operator)로 부르기도 함
- 형식
    - true인 경우 값 if 조건 else false인 경우 값
    - 왼참 if 조건 else 오거
    - ex)
     ```python
    value = num if num >= 0 else -num #절대값을 저장하기 위한 코드
    ```

### 반복문
- 특정 조건을 만족할때까지 같은 동작을 계속 반복하고 싶을 때 사용
- while 문 : 종료조건에 해당하는 코드를 통해 반복문을 종료 시켜야함
- for 문 : 반복가능한 객체를 모두 순회하면 종료 (별도의 종료조건이 필요없음)
- 반복제어 : break, continue, for-else

##### while문
- 조건식이 참인 경우 반복적으로 코드를 실행
- 무한 루프를 하지 않도록 **종료조건**이 반드시 필요
- 형식
  
  ```python
  while 조건:
    #code block
  ```

##### 복합연산자(In-place Operator)
- 연산과 할당을 합쳐 놓은 것
- ex) 반복문을 통해서 개수를 카운트 하는 경우
  ```python
  a = 0
  while a < 5:
    print(a)
    a += 1
  print('끝')
  ```

##### For문
- 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(iterable,반복가능한)의 요소를 모두 순회
    - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요하지 않음
- Iterable
    - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등)
    - 순회형 함수(range, enumerate)
- 형식
    - for 변수명 in literable:
          #code block

###### 문자열(String) 순회
- 형식 1.
    ```python
    for char in chars:
        print(char)
    ```
- 형식 2.
    ```python
    for idx in range(len(chars)):
    print(chars[idx])
    ```

###### 딕셔너리(Dictionary) 순회
- 기본적으로 Key를 순회(key값을 뱉음), Key를 통해 값을 활용
- ex1)
```python
grade = {'john' : 80, 'eric' : 90}
for student in grades:
    print(student)
#john
#eric
```
- ex2)
```python
grade = {'john' : 80, 'eric' : 90}
for student in grades:
    print(student, grades[student])
#john 80
#eric 90
```
- 추가 매서드를 활용한 딕셔너리 순회
  - key() : key로 구성된 결과
  - values() : value로 구성된 결과
  - items() : (key, value)의 튜플로 구성된 결과
  - ex)
    ```python
    grades = {'john' : 80, 'eric' : 90}
    print(grades.keys())
    print(grades.values())
    print(grades.items())
    '''
    dict_keys {['john',]}
    dict_values {[80, 90]}
    dict_items {[('john', 80), ('eric', 90)]}
    '''
    for student, grade in grades.items():
        print(student, grade)
    '''
    john 80
    eric 90
    '''
    ```
    - dictionary는 append가 없는 대신에
    - a['a'] = b <- 이런식으로 만들어 줄 수 있음

##### enumerate 순회
- enumerate()
  - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
    - (index, value) 형태의 tuple로 구성된 열거 객체 반환
- ex1)
```python
members = ['민수', '영희', '철수']
for idx, number in enumerate(members):
    print(idx, number)
'''
0 민수
1 영희
2 철수
'''
```
- ex2)
```python
members = ['민수', '영희', '철수']
enumerate(members) # enumerate at 0x105d3e100
print(list(enumerate(members))) # [(0, '민수'), (1, '영희'), (2, '철수')]
print(list(enumerate(members, start=1))) # [(1, '민수'), (2, '영희'), (3, '철수')]
#start=n n부터 시작
```

###### List Comprehension
- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
- 알고리즘할 때 많이 쓰임!
- 형식
  [code for 변수 in iterable]
  [code for 변수 in iterable if 조건식]
- ex)
```python
cubic_list = []
for number in range(1, 4):
    cubic_list.append(number ** 3)
print(cubic_list)
#[1, 8, 27]

cubic_list = [number ** 3 for number in range(1, 4)]
print(cubic_list)
#[1, 8, 27]

a = []
for i in range(5):
    a.append(i)
print(a)
#[0, 1, 2, 3, 4]

a = [a for i in range(5) if a % 2 == 1]
#흠... 다시해보자
```

###### Dictionary Comprehension
- 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
- 형식
  - {key : value for 변수 in iterable} 
  - {key : value for 변수 in iterable if 조건식} 
- ex)
```python
cubic_dict = {}

for number in range(1, 4):
    cubic_dict[number] = number ** 3
print(cubic_dict)
# {1: 1, 2: 8, 3: 27}

cubic_dict = {number: number ** 3 for number in range(1, 4)}
print(cubic_dict)
# {1: 1, 2: 8, 3: 27}
```

##### 반복문 제어
- break <- 파토
  - 반복문을 종료
```python
n = 0
while True :
    if n == 3:
        break
    print(n)
    n += 1
```
- continue <- 지나가유~
  - continue 이후 코드 블록은 수행하지 않고, 다음 반복을 수행
    - 다음번꺼 넣음 ex) range(5) 인데 1수행시 continue를 만나면, 1은 이후 스킵, 2를 넣어서 실행
    - ex)
```python
a = 0
while a < 5:
    if a == 3:
        continue
    print(a)
    a += 1
#이런식으로 쓰는데 이 코드에서는 3에서 무한루프가 됨. 여튼 3을 피하고싶다 이럴때 쓰면 됨
```
- for-else
  - 끝까지 반복문을 실행한 이후에 else문 실행
  - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음(break는 if문 자체를 끝내버림), 끝까지 돌았으면 else 출력.
  - ex)
```python
for a in range(5):
    print(a)
    if a == 3:
        break
else:
    print("모두 다 돌았습니다.")
'''
0
1
2
3
'''
```
 
- pass
  - 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용)
  - 반복문 아니어도 사용 가능
  - ex)

# 응용, 문제풀이 팁
- a를 모두 제거하라!
```python
word = list(input())
k = 0
for n in range(len(word)):
    if word[n] == 'a':
        k = k + 1
while k != 0:
    word.remove('a')
    k = k - 1

print(''.join(word))
```