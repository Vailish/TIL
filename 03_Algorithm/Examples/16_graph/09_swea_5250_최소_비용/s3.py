from heapq import heappush, heappop


def dijkstra(start):
    distance[start] = 0
    heap = [(0, start, field[0][0])]

    while heap:
        min_dist, min_node, high = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        for dist, next_node in graph[min_node]:
            up = 1
            if high < dist:
                up += dist - high
            new_dist = min_dist + up
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node, field[next_node // N][next_node % N]))


for case in range(1, 1 + int(input())):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    graph = [[] for _ in range(N ** 2)]
    INF = 999999
    distance = [INF] * N ** 2

    for i in range(N ** 2):
        if i - N >= 0:
            graph[i].append((field[(i - N) // N][(i - N) % N], i - N))
        if i % N != 0:
            graph[i].append((field[(i - 1) // N][(i - 1) % N], i - 1))
        if (i + 1) % N != 0:
            graph[i].append((field[(i + 1) // N][(i + 1) % N], i + 1))
        if i + N < N ** 2:
            graph[i].append((field[(i + N) // N][(i + N) % N], i + N))
    dijkstra(0)
    print(f'#{case}', distance[-1])