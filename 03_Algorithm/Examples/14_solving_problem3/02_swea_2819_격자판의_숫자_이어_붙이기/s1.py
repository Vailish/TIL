# 2819. 격자판의 숫자 이어 붙이기 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&problemTitle=2819&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

# 걸린시간 11:00
import sys
sys.stdin = open('input.txt')


# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y, d, temp):
    temp += str(arr[x][y])

    if d == 6:
        if len(temp) == 7:
            result.add(temp)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, d + 1, temp)
    return


def solution():
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0, '')
    return len(result)


for case in range(1, 1 + int(input())):
    arr = [list(map(int, input().split())) for _ in range(4)]
    result = set()
    print(f'#{case} {solution()}')
