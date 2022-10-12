# 1865. 동철이의 일 분배 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc&categoryId=AV5LuHfqDz8DFAXc&categoryType=CODE&problemTitle=1865&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

import sys
sys.stdin = open('input.txt')

# dfs + backtracking
def dfs(person, rate):
    global result
    # 종료조건
    if person == N:  # 전부 다 돌았다면
        result = max(result, rate)
        return
    # 가지치기(확률 계산에 있어서 이미 확률이 더 작다면 더 커질 가능성0)
    if result >= rate or rate == 0:
        return

    for work in range(N):  # 전부 순회
        if not visited[work]:
            visited[work] = True
            dfs(person + 1, rate * pb[person][work] * 0.01)
            visited[work] = False  # 방문 후 원복


for case in range(1, 1 + int(input())):
    N = int(input())
    visited = [False] * N  # 선택한 일은 다른 사람이 못 가져가므로 일차원
    result = 0
    pb = [list(map(int, input().split())) for _ in range(N)]
    dfs(0, 1)
    print(f'#{case}', '{:.6f}'.format(round(result*100, 6)))
