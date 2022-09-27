import sys
sys.stdin = open('input.txt')


def find_root(n):
    for num in range(1, n+1):
        if tree[num][2] == 0:
            return num


def pre_order(n):
    if n:
        print(n, end=' ')
        pre_order(tree[n][0])
        pre_order(tree[n][1])


def in_order(n):
    if n:
        in_order(tree[n][0])
        print(n, end=' ')
        in_order(tree[n][1])


def post_order(n):
    if n:
        post_order(tree[n][0])
        post_order(tree[n][1])
        print(n, end=' ')


V, E = map(int, input().split())  # V = 노드 수, E = 간선 수
edges = list(map(int, input().split()))

tree = [[0, 0, 0] for _ in range(V+1)]  # tree = [[자식1, 자식2, 부모]]

# tree 채우기
for n in range(0, len(edges), 2):
    parent = edges[n]
    child = edges[n+1]
    if tree[parent][0] == 0:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2] = parent
print(tree)
root = find_root(V)
print(root)
print('전위 순회 :', end=' ')
pre_order(root)
print()
print('중위 순회 :', end=' ')
in_order(root)
print()
print('후위 순회 :', end=' ')
post_order(root)
print()
