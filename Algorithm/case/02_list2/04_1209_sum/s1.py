# 1209. [S/W 문제해결 기본] 2일차 - Sum D-3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=1209&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

for t in range(1, 11):
    case = int(input())
    arr = [list(map(int, input().split()))for _ in range(100)]
    print(arr)
    line_sum = 0
    line_max = 0

    for num in range(100):  # 대각선1
        line_max += arr[num][num]
    if line_max < line_sum:
        line_max = line_sum
    print(line_max)
    for num in range(100):  # 대각선2
        line_max += arr[num][-num-1]
    if line_max < line_sum:
        line_max = line_sum
    print(line_max)
    for i in range(100):  # 가로
        line_sum = 0
        for j in range(100):
            line_sum += arr[i][j]
        if line_max < line_sum:
            line_max = line_sum
    print(line_max)
    for j in range(100):  # 세로
        line_sum = 0
        for i in range(100):
            line_sum += arr[i][j]
        if line_max < line_sum:
            line_max = line_sum
    print(f'#{case} {line_max}')
