# input() vs sys.stdin.readline()
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