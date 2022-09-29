# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리 D4
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 크루스칼로 풀자
import sys
sys.stdin = open('input.txt')


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


for case in range(1, 1 + int(input())):
    V, E = map(int, input().split())  # V = 정점의 수, E = 간선의 수
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((w, n1, n2))

    edges.sort()
    parent = list(range(V + 1))
    counts = 0  # MST의 간선의 개수
    cost = 0    # MST의 가중치의 총합(==최소비용)

    for dist, x, y in edges:
        x_root, y_root = find_set(x), find_set(y)

        if x_root != y_root:
            parent[y_root] = x_root
            cost += dist
            counts += 1

            if counts > V - 1:
                break
    print(f'#{case}', cost)
