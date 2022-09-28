import sys
sys.stdin = open('input.txt')


def bfs(n):
    visited = [False] * (v+1)
    visited[n] = True
    print(n, end=' ')
    queue = [n]
    while queue:
        x = queue.pop(0)
        for next_v in graph[x]:
            if not visited[next_v]:
                print(next_v, end=' ')
                visited[next_v] = True
                queue.append(next_v)


edges = list(map(int, input().split()))
v = 7
graph = [[] for _ in range(v+1)]
for i in range(0, len(edges), 2):
    v1, v2 = edges[i], edges[i+1]
    graph[v1].append(v2)
    graph[v2].append(v1)
bfs(1)
print()