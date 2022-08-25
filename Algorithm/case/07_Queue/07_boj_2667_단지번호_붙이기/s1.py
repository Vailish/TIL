# 단지번호붙이기 실버1
# https://www.acmicpc.net/problem/2667

# bfs 사용해서 풀어보기
def bfs(x, y):
    visited[x][y] = True
    queue = [(x, y)]
    total = 1  # 집 수

    while queue:
        x, y = queue.pop(0)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                total += 1
    return total


N = int(input())  # N = 지도의 크기
graph = [list(map(int, input())) for _ in range(N)]
# graph = [list(int(num) for num in input()) for _ in range(N)]
print(graph)

visited = [[False] * N for _ in range(N)]
result = []

dx = [0, 1, 0, -1]  # 우 하 좌 상
dy = [1, 0, -1, 0]  # 우 하 좌 상

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            result.append(bfs(i, j))
print(len(result))
for idx in sorted(result):
    print(idx)
