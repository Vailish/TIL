# 바이러스 실버3
# https://www.acmicpc.net/problem/2606

def bfs(start):
    visited = [False] * (n + 1)
    visited[start] = True
    queue = [start]
    total = 0  # 결과 값

    while queue:
        node = queue.pop(0)
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
                total += 1
    return total


n = int(input())  # 정점 수
m = int(input())  # 간선 수
graph = [[] for _ in range(n+1)]

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(1))
