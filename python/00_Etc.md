# int vs //

int(3/2)  # 1
int(-3/2)  # -1
3//2  # 1
-3//2  # -2

// -> 내림(floor)
int -> 소수점 이하 **버림**


# iterator vs generator
### iterator
- iterator는 값을 가진게 아니라 객체를 들고있다가 for 문을 통해서 불러낼시 계산하고 값을 잃어버림
  - 그렇기 때문에 for문을 돌린다음에 출력해서 값을 보면 빈 리스트가 나오게됨
  - 뽑아내면 사라짐

### generator
- generator는 iterator의 부분집합
```python
a = [i for i in range(100000)]
a = (i for i in range(100000))  # tuple이 아니라 generator 오브젝트가 나옴
# 용량의 경우 리스트로 되어있으면 리스트가 늘어남에따라 엄청 커지지만
# 제너레이터의 경우는 똑같음. 메모리초과 되는 데 한 번만 돌리면 된다면 generator를 써주는 것이 답이 될 수 있음
```
그럼 왜 굳이 iterator로 하냐, 그 이유는 값을 다 안들고 있어도 되기때문에 메모리 적재를 안하기 떄문에 메모리도 적게 먹고 속도도 빠르다/.