'''
Tree
정점 번호 V = 1~(E+1)
간선 수 
부모-자식 순
4
1 2 1 3 3 4 3 5
'''
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i

def preorder(n):  # 전위순회
    if n:  # 마지막 정점 번호를 벗어나지 않으면
        print(n)  # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):  # 중위순회
    if n:
        inorder(ch1[n])
        print(n)  # visit(n)
        inorder(ch2[n])

def postorder(n):  # 후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)  # visit(n)


E = int(input()) # E 간선의 갯수
arr = list(map(int, input().split()))
V = E + 1  # 0은 버리고 안쓸거기 떄문에 +1을 해줘야함
# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
# 자식을 인덱스로 부모 번호 저장
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
print(root)



# root = 1
# preorder(root)
# inorder(root)
# postorder(root)