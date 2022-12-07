# 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')


def in_order(node):
    global cnt
    if node != 0:  # 리프노드일때
        in_order(tree[node][0])
        cnt += 1
        print(node, end=" ")
        in_order(tree[node][1])

    return cnt


# 이진트리
for case in range(1, 1 + int(input())):
    E, N = map(int, input().split())  # E = 간선의 개수, N = 루트값
    edges = list(map(int, input().split()))
    V = E + 1  # V = 정점의 수
    tree = [[0] * 3 for _ in range(V + 1)]  # 왼쪽, 오른쪽, 부모
    cnt = 0
    # 자식 채워 넣기
    for i in range(0, len(edges), 2):
        parent, child = edges[i], edges[i+1]

        if tree[parent][0] == 0:
            tree[parent][0] = child

        else:
            tree[parent][1] = child

        tree[child][2] = parent  # 루트를 찾기 위한 정점


    print(f'#{case} {in_order(N)}')
