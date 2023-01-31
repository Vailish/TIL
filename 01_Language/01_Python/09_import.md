### random
- random.random() : 0 ~ 1 사이 랜덤 실수를 반환
- random.uniform(1, 10) : 2개의 숫자 사이의 랜덤 실수를 반환(2번째 인자 포함X)
- random.randint(1, 10) : 2개의 숫자 사이의 랜덤 정수를 반환(2번째 인자도 범위에 포함)
- random.randrange(0, 101, 2) : start ~ stop 사이의 정수 중에서 하나를 랜덤하게 반환(stop포함X)
  - randrange(start, stop, step)
- random.choice('abcdefg') : 랜덤의 요소를 반환합니다.
- random.sample([1, 2, 3, 4, 5], 3) : 랜덤하게 여러개의 원소를 선택합니다.  # [4, 1, 5]
- shuffle(items) : 원소의 순서를 랜덤하게 바꿉니다.
- https://dales.link/bm4 : details

### request
- pip에 requests 설치 요청하면 쉽게 깔아서 사용할 수 있음.
- https://pythonblog.co.kr/coding/10/

# Collections
## Counter
- 리스트를 딕셔너리 형태로 숫자를 세어준다.
- update를 사용하여 추가 요소를 더해줄 수 있다.
- most_common을 사용하여 최다 요소 순으로(개수까지 정해서) 반환 받을 수 있다.
- items를 통해서 요소값 오름차순으로 정렬시켜서 리스트로 받을 수 있다.
```python
from collections import Counter


lst = [1, 2, 3, 4, 5, 2, 3, 3, 4, 4, 4, 5, 6, 7,]
my_counter = Counter(lst)
print(my_counter)
# Counter({4: 4, 3: 3, 2: 2, 5: 2, 1: 1, 6: 1, 7: 1})

add_lst = [1, 2, 3, 4, 5, 10]
my_counter.update(add_lst)
print(my_counter)
# Counter({4: 5, 3: 4, 2: 3, 5: 3, 1: 2, 6: 1, 7: 1, 10: 1})

print(my_counter.most_common())
# [(4, 5), (3, 4), (2, 3), (5, 3), (1, 2), (6, 1), (7, 1), (10, 1)]

print(my_counter.most_common(n=3))
# [(4, 5), (3, 4), (2, 3)]

print(my_counter.items())
# dict_items([(1, 2), (2, 3), (3, 4), (4, 5), (5, 3), (6, 1), (7, 1), (10, 1)])
```