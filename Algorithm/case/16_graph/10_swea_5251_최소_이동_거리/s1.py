# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리 D4
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# dijkstra 사용
import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop


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
    N, E = map(int, input().split())  # N = 마지막 연결번호, E = 도로개수
    graph = [[] for _ in range(N+1)]
    INF = 9999999999
    distance = [INF] * (N+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))
    dijkstra(0)
    print(f'#{case}', distance[-1])
