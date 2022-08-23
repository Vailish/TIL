# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

def dfs(x, y):
    visited[x][y] = True  # 방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 0:
            road.append((nx, ny))  # 경로 포함

            if nx == n - 1 and ny == m - 1:
                print(road)
                break

            dfs(nx, ny)  # 이동
            road.pop()

n, m = map(int, input().split())  # n = 행, m = 열
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상 하 좌 우
road = [(0, 0)]  # 출구까지의 경로

dfs(0, 0)  # 0, 0 정점에서 시작
