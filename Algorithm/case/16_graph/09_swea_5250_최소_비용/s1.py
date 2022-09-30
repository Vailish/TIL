# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 다익스트라 노드를 좌표로 풀기
import sys
sys.stdin = open('input.txt')


from heapq import heappush, heappop


def dijkstra(x, y):
    distance[x][y] = 0
    heap = [(0, x, y)]

    while heap:
        min_dist, x, y = heappop(heap)

        if min_dist > distance[x][y]:
            continue

        for i in range(4):
            nx = x + [-1, 1, 0, 0][i]  # 상 하 좌 우
            ny = y + [0, 0, -1, 1][i]

            if 0 <= nx < N and 0 <= ny < N:
                dist = field[nx][ny] - field[x][y] + 1 if field[nx][ny] > field[x][y] else 1
                new_dist = min_dist + dist
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    heappush(heap, (new_dist, nx, ny))


for case in range(1, 1 + int(input())):
    N = int(input())  # N = 표의 가로길이, 정점의 수
    field = [list(map(int, input().split())) for _ in range(N)]  # 높이가 담긴 2차원 배열
    INF = 100000
    distance = [[INF] * N for _ in range(N)]
    dijkstra(0, 0)

    print(f'#{case}', distance[-1][-1])
