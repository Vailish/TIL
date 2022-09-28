# 1232. [S/W 문제해결 기본] 9일차 - 사칙연산 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141J8KAIcCFAYD&categoryId=AV141J8KAIcCFAYD&categoryType=CODE&problemTitle=1232&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1


import sys
sys.stdin = open('input.txt')


def caculate(node):  # 후위순위
    if node:
        left = caculate(tree[node][0])
        right = caculate(tree[node][1])
        # 연산자 계산
        if tree[node][2] == '+':
            return left + right
        elif tree[node][2] == '-':
            return left - right
        elif tree[node][2] == '*':
            return left * right
        elif tree[node][2] == '/':
            return int(left / right)
        else:
            return tree[node][2]


for case in range(1, 11):
    N = int(input())  # N = 정점의 수
    result = []
    tree = [[0]*3 for _ in range(N+1)]  # [[child1, child2, value],]
    # 트리 채우기
    for i in range(N):
        a, *b = input().split()
        a = int(a)
        if len(b) == 3:
            tree[a][2] = b[0]
            tree[a][1] = int(b[2])
            tree[a][0] = int(b[1])
        else:
            tree[a][2] = int(*b)

    print(f'#{case}', caculate(1))
