# 1226. [S/W 문제해결 기본] 7일차 - 미로1 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD

# import sys
# sys.stdin = open('input.txt')


def bfs(s):
    x, y = s
    visited[x][y] = True
    queue = [s]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if maze[nx][ny] == 3:
                return 1

            elif 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and maze[nx][ny]==0:
                visited[nx][ny] = True
                queue.append((nx, ny))
            # print(queue)
    return 0


for _ in range(10):
    case = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    # 델타검색 방향설정
    dx = [0, 1, 0, -1]  # 우 하 좌 상
    dy = [1, 0, -1, 0]

    # 시작점 찾기
    bk = False
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                s = i, j
                bk = True
                break
        if bk:  # 불필요한 연산 제거
            break

    print(f'#{case} {bfs(s)}')
