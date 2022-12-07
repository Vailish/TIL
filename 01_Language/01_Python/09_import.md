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