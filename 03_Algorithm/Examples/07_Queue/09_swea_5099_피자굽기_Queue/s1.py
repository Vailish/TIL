# 5099. [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    # 치즈의 양
    cheese = [[a, b] for [a, b] in enumerate(list(map(int, input().split())), start=1)]
    queue = []

    # 화로 안에 피자 가득 넣기
    for idx in range(N):
        queue.append(cheese.pop(0))

    # 피자 굽기
    while len(queue) > 1:
        queue[0][1] = queue[0][1] // 2

        if queue[0][1] == 0:
            queue.pop(0)
            if len(cheese) > 0:
                queue.append(cheese.pop(0))
        else:
            queue.append(queue.pop(0))
    print(f'#{case} {queue[0][0]}')
