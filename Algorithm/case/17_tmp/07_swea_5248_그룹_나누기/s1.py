# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


import sys
sys.stdin = open('input.txt')


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


# 집합을 만들어서 서로소집합이면 Union으로 합쳐서
# 대표노드의 개수를 세면 답이다!
for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 정점의 수(인원 수), M = 간선의 수
    parent = list(range(N + 1))
    edges = list(map(int, input().split()))
    for n in range(0, len(edges) - 1, 2):
        x_root, y_root = find_set(edges[n]), find_set(edges[n+1])
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root
    for num in range(1, N+1):        # 써주는 이유는 값들이 들어올 때
        parent[num] = find_set(num)  # 갱신이 안되는 애들이 있기 때문

    print(f'#{case}', len(set(parent)) - 1)
