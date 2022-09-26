# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')


# post_order(후위 순회)
def post_order(node):
    if node <= N:
        child_value_1 = post_order(node*2)  # 여기서는 연결만 해주고
        child_value_2 = post_order(node*2 + 1)
        return child_value_1 + child_value_2 + tree[node][2]  # 여기 tree[node][2]가 반환하면서 값을 보여준다.
    return 0


for case in range(1, 1 + int(input())):
    N, M, L = map(int, input().split())  # N : 노드의 개수, M : 리프노드의 개수, L : 출력 노드 번호(본인과 자손의 합)
    tree = [[0] * 3 for _ in range(N + 1)]
    leaf_node_value = [list(map(int, input().split())) for _ in range(M)]

    # tree 채우기 [[0, 0, 0], [자식1, 자식2, 값]]
    for i in range(M):
        a, b = leaf_node_value[i]
        tree[a][2] = b

    print(f'#{case} {post_order(L)}')
