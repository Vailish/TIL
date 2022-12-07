# 8차시 6일차 - 노드의 거리
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


def bfs(start, end, depth):
    visited[start] = True
    queue = [(start, depth)]

    while queue:
        v, d = queue.pop(0)
        for next_v in graph[v]:  # v정점에서 이동 가능한 모든 노선에 대하여
            if not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, d + 1))

                if next_v == end:
                    return d + 1  # 1을 더해주는 이유는  next_v를 기준으로 식이 짜여져 있기 때문에
                    # 당시 변수의 기준은 depth를 포함 도착 전 이라서 1을 더해줘야 목적지의 깊이가 나오게 됨.
    return 0


T = int(input())  # T = testcase
for case in range(1, T + 1):
    V, E = map(int, input().split())  # V = node의 수(정점), E 간선개수
    edges = [list(map(int, input().split())) for _ in range(E)]  # edges = 간선정보
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    S, G = map(int, input().split())

    # 인접 리스트 만들기
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    print(f'#{case} {bfs(S, G, 0)}')
