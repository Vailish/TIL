# 1953. [모의 SW 역량테스트] 탈주범 검거
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq

import sys
sys.stdin = open('input.txt')

# bfs

# 터널 구조물 정보
idx = {
    '1': [[-1, 1, 0, 0], [0, 0, -1, 1]],  # dx, dy : 상, 하, 좌, 우
    '2': [[-1, 1], [0, 0]],  # 상, 하
    '3': [[0, 0], [-1, 1]],  # 좌, 우
    '4': [[-1, 0], [0, 1]],  # 상, 우
    '5': [[1, 0], [0, 1]],  # 하, 우
    '6': [[1, 0], [0, -1]],  # 하, 좌
    '7': [[-1, 0], [0, -1]]  # 상, 좌
}

def bfs(x, y, t):
    visited[x][y] = 1  # 시작지점 방문처리
    queue = [(x, y, t)]
    cnt = 0

    while queue:
        x, y, t = queue.pop(0)
        cnt += 1
        if t == 1:
            break
        # 현 위치 구조물 정보 확인
        [dx, dy] = idx.get(str(field[x][y]))
        # delta search
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            # 기본조건
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and field[nx][ny] != 0:
                # 연결여부 확인
                # idx.get(str(field[nx][ny])여기의 방향이 - 붙은 방향이 있는지 검사
                dx_1, dy_1 = idx.get(str(field[nx][ny]))
                if -dx[i] in dx_1 and -dy[i] in dy_1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, t - 1))

    # visited의 합 구하기
    # result = 0
    # for lst in visited:
    #     result += sum(lst)
    return cnt


for case in range(1, 1+int(input())):
    N, M, R, C, L = map(int, input().split())  # N = 세로, M = 가로, (R, C) = 시작지점, L = 시간
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]  # visited : 탈주범이 갈 수 있는 곳
    print(f'#{case} {bfs(R, C, L)}')  # bfs결과 값으로 탈주범이 위치할 수 있는 장소의 개수

#
# direction = [
#     [0, 'n', 0],
#     ['w', 0, 'e'],
#     [0, 's', 0]
# ]
#
# # 연결 관계
# connection = {
#     '1': {'n': [1, 2, 3, 4, 5, 6, 7],
#           's': [1, 2, 3, 4, 5, 6, 7],
#           'w': [1, 2, 3, 4, 5, 6, 7],
#           'e': [1, 2, 3, 4, 5, 6, 7],
#           },  # 다 연결
#     '2': {'n': [1, 2, 5, 6],
#           's': [1, 2, 4, 7],
#           'w': [],
#           'e': [],
#           },
#     '3': {'n': [],
#           's': [],
#           'w': [1, 3, 4, 5],
#           'e': [1, 3, 6, 7],
#           },
#     '4': {'n': [1, 2, 5, 6],
#           's': [],
#           'w': [],
#           'e': [1, 3, 6, 7],
#           },
#     '5': {'n': [],
#           's': [1, 2, 4, 7],
#           'w': [],
#           'e': [1, 3, 6, 7],
#           },
#     '6': {'n': [],
#           's': [1, 2, 3, 4, 5, 6, 7],
#           'w': [1, 3, 4, 5],
#           'e': [],
#           },
# }

