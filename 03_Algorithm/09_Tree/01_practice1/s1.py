# 직접 구현하기
def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:
            return i


def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


V = int(input())
E = V - 1
arr = list(map(int, input().split()))
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
par = [0] * (V + 1)

for i in range(E):
    p, c = arr[2*i], arr[2*i +1]

    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p


root = find_root(V)
preorder(root)