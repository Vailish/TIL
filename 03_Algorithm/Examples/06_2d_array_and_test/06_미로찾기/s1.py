def dfs(x, y):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 0:
            road.append((nx, ny))

            if nx == n - 1 and ny == m - 1:
                print(road)
                break

            dfs(nx, ny)
            road.pop()


n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
road = [(0, 0)]
dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

dfs(0, 0)
