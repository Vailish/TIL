# 1210. [S/W 문제해결 기본] 2일차 - Ladder1 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh

import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    case = int(input())
    field = [[0] + list(map(int, input().split())) + [0] for _ in range(100)] # 좌 우에 오류 방지용 0 삽입

    for i in range(102):  # 시작점의 y 구하기
        if field[99][i] == 2:  # field[99].index(2) 로 구해도 됨.
            start_y = i

    x = 99
    y = start_y
    # 사다리 올라가기

    while True:
        if x == 0:  # 도착했을 때
            break
        elif field[x][y-1] == 1 and y != 0:  # 좌로 탐색
            while field[x][y-1] and y != 0:
                y -= 1
            x -= 1
        elif field[x][y+1] == 1 and y != 100:  # 우로 탐색
            while field[x][y+1] and y != 100:
                y += 1
            x -= 1
        else:  # 위로 올라가기
            x -= 1
    print(f'#{case} {y-1}')  # 예외처리한 것 원복
# 거꾸로 올라간다.
# 시작점 = start
# 현 위치 = x, y
# 검사 위치 = x, y - 1 : 좌 / x, y + 1 : 우
# 반복---
# 좌 우에 1이 보이면, 그 쪽으로 쭉이동한다.
# 없으면 위로 쭉 올라간다
# ---
# x = 0인 시점에 y의 값을 출력
