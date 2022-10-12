# 2105. [모의 SW 역량테스트] 디저트 카페
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu&categoryId=AV5VwAr6APYDFAWu&categoryType=CODE&problemTitle=2105&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

import sys
sys.stdin = open('input.txt')

# delta
dr = [-1, -1, 1, 1]  # 좌상 우상 우하 좌하
dc = [-1, 1, 1, -1]


def dfs(r, c, path, direction):
    global result
    # 종료 조건
    if r == i and c == j and direction == 3 and len(path) > 2:  # 한 칸 이동 후 복귀 경우 제외
        if result < len(path):
            result = len(path)
        return

    # 조건 검색
    if 0 <= r < N and 0 <= c < N and field[r][c] not in path:  # 어차피 방향은 고정되어 있으니 값만 확인
        new_path = path + [field[r][c]]

        # 델타 이동
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 더 전진 할 수 있으면 더 전진
        dfs(nr, nc, new_path, direction)

        # 더 전진 할 수 없다면 방향 변경
        if direction < 3:
            nr = r + dr[direction+1]
            nc = c + dc[direction+1]

            dfs(nr, nc, new_path, direction+1)


for case in range(1, 1 + int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    result = -1  # result = 최대 디저트 값
    for i in range(N):
        for j in range(N):
            dfs(i, j, [], 0)

    print(f'#{case}', result)


# from collections import deque
#
#
# # 우상, 우하, 좌상, 좌하
# dx = [-1, 1, -1, 1]
# dy = [1, 1, -1, -1]
#
#
# def solution():
#     result = [-1]
#     for i in range(N):
#         for j in range(N):
#             x, y = i, j
#
#             # delta search
#             for dir_one in range(4):
#                 nx = x + dx[dir_one]
#                 ny = y + dy[dir_one]
#                 queue = deque((nx, ny, 0))
#                 cnt_one = 0
#                 path_one = deque()
#                 path_one.append((x, y, cnt_one))
#                 while 0 <= nx < N and 0 <= ny < N:
#                     nx, ny, cnt_one = queue.popleft()
#                     cnt_one += 1
#                     path_one.append((nx, ny, cnt_one))
#                     nx += dx[dir_one]
#                     ny += dx[dir_one]
#
#                 for k in range(len(path_one)):
#                     x, y, cnt_one = path_one.popleft()
#                     for dir_two in range(4):
#                         nx = x + dx[dir_two]
#                         ny = y + dy[dir_two]
#                         cnt_two = 0
#                         queue = deque((nx, ny, cnt_two))
#                         path_two = deque()
#                         path_two.append((nx, ny, cnt_two))
#
#                         if (dx[dir_two], dy[dir_two]) not in [(dx[dir_one], dy[dir_one]), (-dx[dir_one], -dy[dir_one])]:
#                             while 0 <= nx < N and 0 <= ny < N:
#                                 nx, ny, cnt_two = queue.popleft()
#                                 cnt_two += 1
#                                 path_two.append((nx, ny, cnt_two))
#                                 nx += dx[dir_two]
#                                 ny += dy[dir_two]
#                                 print('ㅇㅅㅇ', (nx, ny), dx[dir_two], dy[dir_two])
#
#                             # 반 왔으니 나머지는 자동으로 결정 됨
#                             path_two.popleft()
#                             print('*')
#
#     return max(result)
#
#
# for case in range(1, 1 + int(input())):
#     N = int(input())
#     field = [list(map(int, input().split()))]
#     visited = [[False] * N for _ in range(N)]
#     print(f'#{case}', solution())
