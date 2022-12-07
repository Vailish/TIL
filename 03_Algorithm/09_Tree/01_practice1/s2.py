# 다음 2진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오.
# 13 <- 정점의 개수
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

V = int(input())  # 정점 개수, 마지막 정점번호
arr = list(map(int, input().split()))
E = V - 1


def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i

def preorder(n):  # 전위순회
    if n:  # 마지막 정점 번호를 벗어나지 않으면
        print(n, end = ' ')  # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):  # 중위순회
    if n:
        inorder(ch1[n])
        print(n, end = ' ')  # visit(n)
        inorder(ch2[n])

def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end = ' ')  # visit(n)

ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
par = [0] * (V + 1)

# 방법 1
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]

# 방법 2
# for j in range(0, E*2, 2):
#     p, c = arr[j], arr[j+1]

    if ch1[p] == 0:  # 아직 자식이 없으면
        ch1[p] = c  # 자식1로 저장
    else:
        ch2[p] = c
    
    par[c] = p
root = find_root(V)
# print(root)

preorder(root)
print()
inorder(root)
print()
postorder(root)
print()