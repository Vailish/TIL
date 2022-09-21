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

def bfs(x, y):
    visited[x][y] = 1  # 시작지점 방문처리
    






for case in range(1, 1+int(input())):
    N, M, R, C, L = map(int, input().split())  # N = 세로, M = 가로, (R, C) = 시작지점, l = 시간
    field = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]  # visited : 탈주범이 갈 수 있는 곳
    print(f'#{case} {bfs(R, C)}')  # bfs결과 값으로 탈주범이 위치할 수 있는 장소의 개수
