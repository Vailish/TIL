# 틀린 풀이 temp
# global로 인해서 재귀할때마다 돌아감

import sys
sys.stdin = open('../../06_Stack2/07_swea_4875_미로/input.txt')


# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, d):
    global temp
    temp += str(arr[x][y])

    if d == 6:
        if len(temp) == 7:
            result.add(temp)
        temp = ''
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, d + 1)
    return


def solution():
    global temp
    for i in range(4):
        for j in range(4):
            temp = ''
            dfs(i, j, 0)
    print(result)
    return len(result)


for case in range(1, 1 + int(input())):
    arr = [list(map(int, input().split())) for _ in range(4)]
    temp = ''
    result = set()
    print(f'#{case} {solution()}')