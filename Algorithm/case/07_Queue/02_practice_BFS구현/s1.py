### bfs : 구현에 있어서 dfs와 매우 유사
### graph를 만드는데 까지는 똑같지만, queue를 사용해서 while문 돌리는게 차이점이다.

def bfs(v):
    visited[v] = True
    queue = [v]

    # 큐가 빌 때까지 반복
    while queue:
        v = queue.pop(0)  # 현재 정점
        for next_v in graph[v]: # 현재 정점과 인접한 모든 정점에 대해
            if not visited[next_v]:  # 아직 방문하지 않았다면
                visited[next_v] = True  # 인접 정점 방문처리
                queue.append(next_v)  # 인접 정점을 큐에 삽입
                print(next_v, end=' ')


# 사용할 변수 입력
n, m = map(int, input().split())  # 정점, 간선 개수
edges = list(map(int, input().split()))  # 간선 정보
graph = [[] for _ in range(n+1)]  # n + 1 인 이유는 정점 번호가 1부터 시작이기 때문
visited = [False] * (n + 1)  # 방문 처리 리스트 -> n + 1인 이유는 정점 번호가 1번부터 시작하기 때문

# 인접 리스트 만들기(graph 완성시키기)
for i in range(0, len(edges), 2):
    v1, v2 = edges[i], edges[i+1]
    # v1, v2를 양방향으로 넣는 이유는 무방향(양방향)이기 때문
    graph[v1].append(v2)
    graph[v2].append(v1)

bfs(1)  # 시작 정점을 1로 탐색 시작
