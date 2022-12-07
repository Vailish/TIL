# 5097. [파이썬 S/W 문제해결 기본] 6일차 - 회전 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    for _ in range(M):
        queue.append(queue.pop(0))
    print(f'#{case} {queue.pop(0)}')
