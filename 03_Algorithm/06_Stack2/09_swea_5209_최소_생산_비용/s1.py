# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')

def dfs(depth, path, sum_num):
    global min_num
    # end condition
    if depth == N:
        min_num = min(min_num, sum_num)
        return

    # backtracking
    if sum_num > min_num:
        return

    for i in range(N):
        if i not in path:
            dfs(depth+1, path + [i], sum_num + arr[depth-1][i])


for case in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = 99 * 15 + 1
    dfs(0, [], 0)  # (depth, path, sum_num)
    print(f'#{case}', min_num)
