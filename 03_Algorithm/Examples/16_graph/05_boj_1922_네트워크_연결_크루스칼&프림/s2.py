# heap으로 풀기
import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop


def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]  # heap은 앞의 원소 기준으로 정렬함
    cost = 0

    while heap:
        min_dist, min_node = heappop(heap)
        if visited[min_node]:
            continue

        visited[min_node] = True
        cost += min_dist

        # 인접 정점에 대해 가중치와 정점 정보를 힙에 삽입
        for next_node, w in graph[min_node]:
            if not visited[next_node]:
                heappush(heap, (w, next_node))



n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))
