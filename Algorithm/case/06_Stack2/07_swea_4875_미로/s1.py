# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]  # 상 하 좌 우

def dfs(x, y):
    # 방문처리
    visited[x][y] = True

    # 4방 검사
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and maze[nx][ny] == 0:
            if nx == destination_x and ny == destination_y:
                print(f'#{case} 1')
                break
            dfs(nx, ny)
    print(f'#{case} 0')
    return


for case in range(1, 1 + int(input())):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]
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

    dfs(0, 0)