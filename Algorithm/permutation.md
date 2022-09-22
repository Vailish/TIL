# permutation

### 1번
```python
def permutations(arr):
    # 뽑고 싶은 만큼 뽑았다면 출력 및 종료
    if len(arr) == length:
        print(arr)
        return

    for i in range(len(numbers)):
        if not visited[i]:
            # 1) i번째 원소를 뽑는다.
            visited[i] = True
            arr.append(numbers[i])

            # 2) 재귀함수 진행
            permutations(arr)

            # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
            visited[i] = False
            arr.pop()


numbers = [1, 2, 3, 4]
visited = [False] * len(numbers)
length = 2  # 뽑고 싶은 원소의 개수

permutations([])
```

### 2번
```python
def permutations(depth):
    if depth == len(numbers):
        print(numbers)
        return

    for i in range(depth, len(numbers)):
        numbers[depth], numbers[i] = numbers[i], numbers[depth]
        permutations(depth + 1)
        numbers[depth], numbers[i] = numbers[i], numbers[depth]


numbers = [1, 2, 3, 4]

permutations(0)
```

- 얘를 변형해서 사용하려고 보면 result가 텅 비어있음 그 이유는 얕은 복사
- 해결법
  - 1. 값이 들어있는 새로운 객체를 만들면 됨
    - result.append(arr) -> result.append(list(numbers)) or result.append(numbers[:])
    - deepcopy를 사용


