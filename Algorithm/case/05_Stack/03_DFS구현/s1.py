def dfs(v):
    visited[v] = 1  # 현재 방문 정점(꼭지점) 방문처리
    print(v, end=' ')
    
    for next_v in graph[v]:  # 현재 방문 정점과 연결된 모든 경우의 수 확인
        if visited[next_v] == 0:  # 방문 안했으면
            dfs(next_v)  # 방문해라

n, m = map(int,input().split())  # n = 정점(꼭지점), m = 간선개수(선)

# 인접 리스트 (graph)를 위한 edge, graph의 틀
edges = list(map(int,input().split()))  # 간선정보, 데이터만 담기 (뒤에 합쳐서 만들기 위해)
graph = [[] for _ in range(n+1)]  # 간선정보를 담을 그릇, 0은 편의성을 위해 둠

# 들렀다는 표시를 위한 list
visited = [0] * (n+1) # 0은 편의성을 위해 둠 -> 수를 맞추기 위해 + 1

# 인접 리스트 만들기(graph 완성시키기)
for i in range(0, len(edges), 2):  # edges를 둘씩 묶어서 빼줘야 하기때문에 edges 기준으로 뿌려주기
    v1, v2 = edges[i], edges[i+1]  # 인접한 두 정점(꼭지점)의 연결 여부를 위해
    graph[v1].append(v2)  # append로 붙이는 이유는 이중 리스트이기 때문에, 그 안에 넣으려고
    graph[v2].append(v1)  # 쌍방연결, 서로 연결되어있다. 1을 기준으로 2가 있고 2를 기준으로도 1이 있게끔

dfs(1)  # 시작점