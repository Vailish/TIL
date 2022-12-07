# 1238. [S/W 문제해결 기본] 10일차 - Contact D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD

def bfs(n):
    visited[n] = True
    d = 0
    queue = [(n, d)]
    result = []
    while queue:
        x, d = queue.pop(0)
        for next_v in graph[x]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, d + 1))
                result.append((next_v, d + 1))

    result = sorted(result, key=lambda x: (x[1], x[0]), reverse=True)
    return result[0]


for case in range(1, 11):
    num, s = map(int, input().split())  # num = 데이터의 길이, s = 시작점
    data = list(map(int, input().split()))
    visited = [False] * 101
    graph = [[0] for _ in range(101)]

    # graph 만들기
    for i in range(0, num, 2):
        v1, v2 = data[i], data[i+1]
        graph[v1].append(v2)

    print(f'#{case} {bfs(s)[0]}')












# # bfs로 풀면될듯
#
# def bfs(s, graph):
#     visited[s] = True
#     queue = [(index_list.index(s), 0)]
#     result = [(0, 0)]  # result = depth, idx(next_v)
#
#     while queue:
#         x, d = queue.pop(0)
#         # print(graph[x])
#         for next_v in graph[x]:
#             if not visited[next_v]:
#                 visited[next_v] = True
#                 if result[0][0] > d:  # d를 비교해서 높으면 바꿔주기
#                     result[0][0] = d
#                     result[0][1] = next_v
#                 queue.append((next_v, d + 1))
#
#     return index_list.index(result[0][1])
#
#
# def sol(v, s):
#     graph = [[] for _ in range(v + 1)]
#     # 그래프 채워넣기
#     index_lst = []
#     for n in range(0, v, 2):
#         val_1, val_2 = data[n], data[n+1]
#         index_lst.append(val_1)
#         graph[index_lst.index(val_1)].append(val_2)
#     print(graph)
#     return bfs(s, graph)
#
#
# for case in range(1, 11):
#     v, s = map(int, input().split())  # v = 정점의 수, s = 시작점
#     data = list(map(int, input().split()))
#     result = []
#     # 새로운 인덱스 리스트 작성
#     index_list = list(set(data))  # 각 정점의 값과 번호
#     # {2, 3, 5, 6, 7, ...}
#     visited = [0] * len(index_list)
#     print(f'{case} {sol(v, s)}')
