# 재풀이
import sys
sys.stdin = open('input.txt')


def subtree(x):
    global cnt

    if x:
        subtree(tree[x][0])
        subtree(tree[x][1])
        cnt += 1  # post_order
    return


for case in range(1, 1 + int(input())):
    E, N = map(int, input().split())  # E = 간선의 개수, N = subtree 시작정점
    edges = list(map(int, input().split()))  # edges = 간선
    tree = [[0, 0, 0] for _ in range(E+1+1)]  # 간선의 개수 + 2 = 정점의 수 why? 이진트리
    cnt = 0  # cnt = 하위 노드의 개수
    # tree 만들기
    # tree = [[], [자식1, 자식2, 부모값],...]
    for num in range(0, len(edges), 2):
        # 2 1 2 5 1 6 5 3 6 4
        child = edges[num + 1]
        parent = edges[num]
        if tree[parent][0] == 0:
            tree[parent][0] = child
        else:
            tree[parent][1] = child
        tree[child][2] = parent
    subtree(N)
    print(f'#{case} {cnt}')
