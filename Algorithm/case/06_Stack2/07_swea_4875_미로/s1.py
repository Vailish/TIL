# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')


def dfs(r, c):
    global result
    visited[r][c] = True

    for direction in range(4):
        nr = r + [-1, 1, 0, 0][direction]  # 상 하 좌 우
        nc = c + [0, 0, -1, 1][direction]

        if (nr, nc) == (destination_x, destination_y):
            result = True

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and maze[nr][nc] == 0:
            visited[nr][nc] = True
            dfs(nr, nc)
            visited[nr][nc] = False


for case in range(1, 1 + int(input())):
    N = int(input())
    result = 0
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 시작점, 도착점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x = i
                start_y = j
            if maze[i][j] == 3:
                destination_x = i
                destination_y = j

    dfs(start_x, start_y)
    print(f'#{case}', 1 if result else 0)
