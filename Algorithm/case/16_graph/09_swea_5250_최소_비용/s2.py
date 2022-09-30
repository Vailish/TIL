# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 다익스트라 + 각 칸을 노드로 보고 풀기 : 실패/시간초과
# 좌표로 풀기 1번
import sys
sys.stdin = open('input.txt')


from heapq import heappush, heappop


def find_high(n):
    for a in range(N):
        for b in range(N):
            if n == N * a + b:
                return field[a][b]


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        for dist, next_node in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))


for case in range(1, 1 + int(input())):
    N = int(input())  # N = 표의 가로길이, 정점의 수
    field = [list(map(int, input().split())) for _ in range(N)]
    graph = [[] for _ in range(N**2)]
    INF = 1000
    distance = [INF] * N**2

    # 정점배열 만들기
    idx = []
    temp = []
    for i in range(N**2):
        temp.append(i)
        if len(temp) == N:
            idx.append(temp)
            temp = []

    # graph 채워넣기 - 델타검색을 통해서

    for i in range(N):
        for j in range(N):
            w_base = find_high(idx[i][j])
            for direction in range(4):
                nx = i + [-1, 1, 0, 0][direction]  # 상 하 좌 우
                ny = j + [0, 0, -1, 1][direction]

                if 0 <= nx < N and 0 <= ny < N:  # 구해야할 녀석이 (s, e, w)
                    graph[idx[i][j]].append(
                        (find_high(idx[nx][ny]) - w_base + 1 if find_high(idx[nx][ny]) > w_base else 1, idx[nx][ny])
                    )
    dijkstra(0)
    print(distance)
    print(f'#{case}', distance[-1])


    # 범위 정해주기가 너무힘듦
    # graph를 채워 넣자
    # 그 정보를 바탕으로 그래프의 무게 정보를 얻는다!

    # cnt = 0
    # for n in range(N**2):
    #     w_base = find_high(n)
    #     cnt % N
    #     for m in range(4):
    #         next = [n-1, n+1, n-4, n+4][m]  # 모서리에서 나가는 거 잡아야됨
    #         if 0 <= next < N**2:
    #             graph[n].append((find_high(next) - w_base + 1 if find_high(next) > w_base else 1, next))
