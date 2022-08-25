# 2161. 카드1
# https://www.acmicpc.net/problem/2161

queue = list(range(1, 1 + int(input())))

while queue:
    print(queue.pop(0), end=' ')
    if not queue:
        break
    queue.append(queue.pop(0))
