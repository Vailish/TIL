### 컨테이너
 - 컨테이너 : 여러 개의 값(데이터)을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음.
   - ex) List
   - cf) pandas array : 숫자만 가능 // 변수 : 한 개의 데이터 저장
 - 순서가 있는 데이터 (Ordered) vs 순서가 없는 데이터(Unordered)
   - 순서가 있다(저장순서) != 정렬되어있다
   - 순서가 없는 데이터 : 관계, 팔로우 같은 내용
 - 컨테이너
   - 시퀀스형(sequence, 순서가 있는) : ex) a[1]
     - 리스트 - 가변형
     - 튜플 - 불변형
     - 레인지 - 불변형
     - *문자열* - 불변형
   - 비시퀀스형(non-sequence)
     - 세트 - 가변형
     - 딕셔너리 - 가변형
   - ex) 여러개를 담아야 하고, 수정이 가능하고, 순서가 있다면 -> list로 하면 됨. 이런식으로 무엇을 쓸지 정하기 위해 이걸 정하는게 중요함
   - 가변형 VS 불변형 : 내부의 값의 수정여부 ex) a[0] = 2와 같은 방식

#### 리스트(List)
 - 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
 - [] or list(), 제일 앞부터 **0**, 1, 2 번
 - 파이썬에서는 어떠한 자료형도 저장 가능(리스트안에 리스트도 가능) -> 이러한 유형성 때문에 가장 흔히 사용
 - 가변형 : 생성 이후 내용변경 가능
 - 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
   - ex)list[4], list[2:5:3]
 - type() : 자료형(class)를 확인할 수 있음.
 - 문자열 불변
   - list_d = [1, 2, 3, ['aaaa', 'bbbbbb', 'cccccc']]
     b->z로 바꾸는건 안됨 why? 문자열, 바꾸려면 bbbbbb를 통째로 변경해야함

##### 이차원 리스트
- 이차원 리스트는 리스트를 원소로 가지는 리스트일 뿐이다. <- 행렬이다
- pprint() <- 예쁘게 출력해줌(가독성 있게) : 2차원 list나 dictionary 등
ex)
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0][2]) # 2

matrix = [
[1, 2, 3]
[4, 5, 6]
[7, 8, 9] 
]

matirx = [
  [1, 2, 3, 4] #행 우선 순회
  [5, 6, 7, 8]
  [9, 0, 1, 2]
  #열 우선 순회
]

# 이중 for문을 이용한 행 우선 순회
for i in range(3): #행
  for j in range(4): #열
    print(matrix[i][j], end=" ")
  print()
'''
1 2 3 4
5 6 7 8
9 0 1 2
'''
# 열 우선 순회인 경우 (i와 j만 바꾸면돠미)
'''
1 5 9
2 6 0
3 7 1
4 8 2
'''

#이 상태에서 다 더하면 됨, 모든 수의 합.
matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
total = sum(map(sum, matrix))
#sum([4, 4, 4]) -> 12
#sum 대신에 max와 min을 써서 최대랑 최소도 정해줄 수 있음

```

#### 튜플(tuple)
- 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
- 리스트와의 차이점 : 생성 후, 담고 있는 값 변경이 불가(불변 자료형)
- (), tuple()
- 튜플은 수정 불가능한(immutable) 시퀀스로 인덱스로 접근 가능
- 값에 대한 접근은 tuple[i]
- ex1) 단일 : tuple_a = (1,) / 복수 : tuple_b = (1, 2, 3,)
- ex2) a = (2)
       print(a, type(a)) # 2, <class 'integer'> <-그래서 (a,) 이렇게 써줘야함
- ex3)
  a = 1,
  
  print(a) # (1,) <- 튜플 복수도 같이 나옴
- 튜플 대입
- ex)
- x, y = 1, 2
- print(x, y) = # 1 2
- 실제로는 tuple로 처리 (x, y) = (1, 2) 이런식으로
  -  시스템 내부적으로 tuple을 많이 씀

#### Range
- 숫자의 시퀀스를 나타내기 위해 사용
- 주로 반복문과 함께 사용됨
- ex) print(range(0, 4)) #[0, 1, 2, 3]
- range로 출력하면 range그대로나옴, 그래서 확인하려면 list로 형 변환해서 확인해야함.
- range(n) : 0 ~ n-1까지
- range(n, m) : n ~ m-1까지, n부터 m칸 가!, n이상 m미만
- range(n, m, s) : n부터 m-1까지 s만큼 증가시키며 숫자의 시퀀스
  - ex) print(list(range(1, 5, 2))) # [1, 3]
  - s = -1, -2 <-역순

#### 슬라이싱 연산자
- 인덱스와 콜론을 사용하여 문자열의 특정부분만 잘라낼 수 있음
- 리스트 : print([1, 2, 3, 4][1:4]) # [2, 3, 4] <- 1이상 4미만
- range : print(range(10)[5:8]) # range(5, 8)
- 문자열 : print('abcd'[:3]) # abc 
- 튜플 : print((1, 2, 3, 5)[0:4:2]) # [1, 3] <- 3번째는 간격!
- [5:2:-1] 이런식으로도 가능!

#### 집합(Set)
- 중복되는 요소가 없이 순서에 상관없는 데이터들의 묶음
  - 중복X -> 중복된 원소는 하나만 저장 (중복 제거용으로 사용하기 좋음, 단 순서가 중요한경우 비적합)
  - 순서X -> 인덱스를 이용한 접근 불가 ex) {}[2] : 불가
- 수학의 집합연산 가능, 여집합은 별도로 없음
  - | : 합, (파이프라인)
  - & : 교집합
  - \- : 차집합 (A-B의 경우 A만 있는것)
  - ^ : 대칭 차집합 (A^B의 경우 합집합에서 교집합을 뺀것)
- 가변자료형(mutable) : 담고 있는 요소 삽입 변경, 삭제 가능
  - {}, set() : 단, 빈 set를 만들기 위해서는 set()만 써야함
    - ex)
    ```python
      blank = {}

      print(type(blank)) # <class 'dict'>

      blank = set()

      print(type(blank)) # <class 'set'>
    ```

#### 딕셔너리(Dictionary)
- 키-값(key-value) 쌍으로 이루어진 자료형(python3.7부터 ordered(정확히는 순서보정정도), 이하 버전은 unordered)
- key : 변경 불가한 데이터(immutable)만 활용가능
  - ex) string, integer, float, boolean, tuple, range
- value : 모든 데이터 가능
- {}, dict() <- key를 통해 value에 접근
  - dict_a = dict('a'='apple') X -> dict(a='apple') 이런식으로 규칙을 지켜줘야함.
- ex) ['a' : 'apple, 'list' : [1, 2, 3]]
- key로 부를때, dic_key[a]이런식으로함, ()가 아닌[]임
  - dic.get()로 불러와도 됨, 차이점은 key 가 없더라도 default 값으로 none이 들어있어서 오류 안나게 할 수 있으며
  - (key값, none)에서 none 자리를 바꿔주면 key가 없을 시 반환값을 바꿀 수 있음.
- ex) list 안에 dictionary 안에 dictionary 
```python
air_info = [{'name' : 'A', 'capital' : True, 'air_status' : {'O2' : 3, 'CO2' : 2}}, {'name' : 'B', 'capital' : False, 'air_status' : {'O2' : 5, 'CO2' : 3}}]
print(air_info)
```


#### 형 변환(Typecasting)
- 파이썬에서 데이터 형태는 서로 변환 가능
  - ex) 숫자 -> 문자, 문자 -> 숫자
- **암시적 형 변환(Implicit)** <- 파이썬의 유연함
  - 파이썬이 내부적으로 자료형을 반환하는 경우(사용자의 의도X)
  - bool
    - ex) print(True + 3) #4
  - Numeric type(int, float)
    - ex) print(3 + 5.0) #8.0
- **명시적 형 변환(Explicit)**
  - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환
  - str, float => int
  - 형식에 맞는 문자열만 정수, 실수로 변환가능
    - ex1) print(int('3') + 4) #7
    - ex2) print(int('3.5') + 5) #ValueError <- 3.5는 정수가 아니므로
    - ex3) print(float('3/4') + 5.3) #ValueError <- 컴퓨터는 분수를 문자열로 보기때문에 불가함.
    - ex4) a=str([1, 2, 3])
           print(a[0], a[1], a[2]) # [1, <-주의
    - 문자열로는 모두 가능하다
      - int, float, list, tuple, dict -> str
      - **input()**을 사용시 입력값은 어떠한 값을 입력해도 **문자열로 저장**됨! -> 계산필요시 바꿔줘야함
        - ex) map(int, input().split())
          - map : 각 칸마다 함수를(int) 적용
          - input(a) : a가 출력되고 그 옆에 입력하게끔 나옴.

#### Container 관련 method
##### sort

- 기능 : 정렬
- 형식 : list_type.sort()
- 정렬 : default 오름차순, sort(reverse=True)시 내림차순
- 기타 : 단독으로 쓰자, 본체를 바꾸는 형식이기에 None이 나오는듯 다른 것과 함께쓰면 오류가 많음.
- sort vs sorted
    - sort()
      - 본체 정렬
    - sorted(정렬할 데이터, key 파라미터, reverse 파라미터) - 뒤는 하나 or 둘 생략가능
      - 본체가 아닌 **새로운 정렬된 리스트**를 만들어 반환
      - key 파라미터는 정렬의 기준값
- https://blockdmask.tistory.com/466