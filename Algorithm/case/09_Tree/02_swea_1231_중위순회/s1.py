# 1231. [S/W 문제해결 기본] 9일차 - 중위순회 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD&categoryId=AV140YnqAIECFAYD&categoryType=CODE&problemTitle=1231&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&&&&&&&&&&

# inorder, 중위순회 방식
# 완전 이진트리일때 인데... 놓쳣다...

def inorder(v):
    global answer
    if v <= N:
        inorder( v * 2)     # 왼쪽 서브트리의 루트로 이동
        answer += tree[v]
        inorder( v * 2 + 1) # 오른쪽 서브트리의 루트로 이동

T = 10
for tc in range(1, T+1):
    N = int(input())        # 정점 개수
    tree = [0] * (N+1)      # 완전이진트리
    for _ in range(N):
        arr = input().split()
        tree[int(arr[0])] = arr[1]
    answer = ''
    inorder(1)      # 완전이진트리의 루트부터 순회
    print(f'#{tc} {answer}')







# def inorder(n):
#     inorder(ch1[n])
#     print(dic.get(n), end="")
#     inorder(ch2[n])


# for case in range(1, 11):
#     v = 8  # 정점 수
#     e = v - 1  # 간선 갯수
#     # pop한다음에 append해서 간선 정보를 따로 정리하자.
#     data = input()
#     dic = {}
#     edges = []
#     num = data.pop(0)
#     dic[num] = data.pop(0)
    
#     while data:
#         edges.append((int(num), int(data.pop(0))))

#     ch1 = [0] * (v + 1)
#     ch2 = [0] * (v + 1)

#     for i in range(e):
#         p, c = edges[i][0], edges[i][1]

#         if ch1[p] == 0:
#             ch1[p] = c
#         else:
#             ch2[p] = c
    
#     inorder(1)
#     print()