'''
[입력]
6 4
5 6
4 5
3 4
1 3

[출력]
1 2 1 1 1 1
[0, 1, 2, 1, 3, 4, 5]
'''

n, m = map(int(input().split()))  # 정점, 간선(Union 횟수) 개수
parent = list(range(n+1))

for _ in range(m):
    x, y = map(int, input().split())
    x_root, y_root = find_set(x), find_set(y)  # find

    # Union
    if x_root != y_root:  # 서로소일 때
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root

# 출력
for i in range(1, n+1):
    print(find_set(i), end=' ')

print()
print(parent)
