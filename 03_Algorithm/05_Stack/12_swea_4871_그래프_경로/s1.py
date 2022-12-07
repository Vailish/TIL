# 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# DFS를 활용하여 가는 경로를 찾는 함수를 만든 뒤
# 시작점을 넣어서, 가는 경로에 도착지점이 있는지 여부를 확인하여 출력

def dfs(v):
    visited[v] = 1
    result.append(v)

    for next_v in graph[v]:
        if visited[next_v] == 0:
            dfs(next_v)


for case in range(1, 1 + int(input())):
    n, m = map(int, input().split())  # n = 정점(노드), m = 간선 수
    result = []  # 도착 정점
    visited = [0] * (n+1)  # 방문 확인 list
    graph = [[] for _ in range(n+1)]
    #
    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    S, G = map(int, input().split())  # S = 시작점,  G = 끝점
    dfs(S)

    if G in result:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')
