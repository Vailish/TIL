# 2161. 카드1
# https://www.acmicpc.net/problem/2161

# deque으로 풀기!

from collections import deque

queue = deque(range(1, 1 + int(input())))

while queue:
    print(queue.popleft(), end=' ')
    if not queue:
        break
    queue.append(queue.popleft())
