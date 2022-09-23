# 2105. [모의 SW 역량테스트] 디저트 카페
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu&categoryId=AV5VwAr6APYDFAWu&categoryType=CODE&problemTitle=2105&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

# 우상, 우하, 좌상, 좌하
dx = [-1, 1, -1, 1]
dy = [1, 1, -1, -1]


def dfs(x, y, lst):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and field[nx][ny] not in lst:
            dfs(nx, ny, lst.append(field[nx][ny]))
            visited[nx][ny] = False
            lst.pop()


def solution():
    lst = []
    for i in range(N):
        for j in range(N):
            dfs(i, j, lst)

    return


for case in range(1, 1 + int(input())):
    N = int(input())
    field = [list(map(int, input().split()))]
    visited = [[False] * N for _ in range(N)]
    print(f'#{case} {solution()}')
