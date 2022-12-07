import sys
sys.stdin = open('input.txt')


def dfs(n):
    visited[n] = True
    print(n, end=' ')
    for next_v in graph[n]:
        if not visited[next_v]:
            dfs(next_v)


edges = list(map(int, input().split()))
v = 7 # v = 정점의 수

visited = [False] * (v+1)
graph = [[] for _ in range(v+1)]
# graph 채우기
for i in range(0, len(edges), 2):
    d1, d2 = edges[i], edges[i+1]
    graph[d1].append(d2)
    graph[d2].append(d1)
dfs(1)
print()
