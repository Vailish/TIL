# 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

def bfs(x, y):
    visited[x][y] = 1
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                if maze[nx][ny] == 3:
                    return visited[nx][ny] - 1 - 1  # 출발, 도착 한 개씩 빼주기 why? :
                queue.append((nx, ny))
    return 0


dx = [0, 1, 0, -1]  # 우 하 좌 상
dy = [1, 0, -1, 0]  # 우 하 좌 상

for case in range(1, 1 + int(input())):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    # 시작 점과 끝 점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_x, start_y = i, j

    print(f'#{case} {bfs(start_x, start_y)}')
