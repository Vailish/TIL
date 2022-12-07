# 재귀를 이용한 깊이우선탐색(DFS)

def dfs(v):
    visited[v] = True  # 현재 정점 방문 처리
    print(v, end=' ')

    for next_v in graph[v]:  # 현재 정점과 인접한 모든 정점에 대해
        if not visited[next_v]:  # 아직 방문하지 않았다면
            dfs(next_v)  # 인접 정점 방문하기

            # ex) 왜 v위치에서 graph v냐
            # v1과 v2를 설정해 주는 과정에서 들어갔기때문? 그럼 graph[1]이 아니라 graph[0]이 1과 연결되는 리스트 아님?


n, m = map(int, input().split())  # 정점, 간선 개수
edges = list(map(int, input().split()))  # 간선 정보
graph = [[] for _ in range(n + 1)]  # 그래프 -> n + 1인 이유는 정점 번호가 1번부터이기 때문
visited = [False] * (n + 1)  # 방문 처리 리스트 -> n + 1인 이유는 정점 번호가 1번부터이기 때문

# 인접 그래프 만들기 (graph 완성시키기 why? -> 이걸 바탕으로 이동방향을 선택할 수 있음.)
for i in range(0, len(edges), 2):
    v1, v2 = edges[i], edges[i + 1]  # 인접한 두 정점
    # v1, v2를 양방향으로 넣는 이유는, 화살표가 없는 무방향 그래프이기 때문
    graph[v1].append(v2)  # 1번(리스트)에 넣어라
    graph[v2].append(v1)  # 2번(리스트)에 넣어라 결론은 서로 넣어주는것

dfs(1)  # 시작 정점을 1로 탐색 시작