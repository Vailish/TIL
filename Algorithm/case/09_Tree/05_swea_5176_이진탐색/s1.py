# 5176. [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')


def pre_order(n):
    global cnt
    if n <= N:
        pre_order(2*n)
        tree[n][2] = cnt
        cnt += 1
        pre_order(2*n+1)


for case in range(1, 1 + int(input())):
    N = int(input())  # N = 정점의 수
    tree = [[0] * 3 for _ in range(N+1)]  # [[0 ,0 , 0], [자식1, 자식2, 값]]
    # tree 채우기
    cnt = 1
    pre_order(1)
    print(f'#{case}', tree[1][2], tree[N//2][2])
