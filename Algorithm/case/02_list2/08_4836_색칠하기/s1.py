# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

for case in range(1, 1 + int(input())):
    # 2 2 4 4 1
    # 3 3 6 6 2
    field = [[0] * 10 for _ in range(10)]
    for paper in range(int(input())):  # 색칠하기
        # (a1, a2) ~ (b1, b2) 까지, c색으로
        a1, a2, b1, b2, c = map(int, input().split())
        for i in range(a2, b2+1):
            for j in range(a1, b1+1):
                if field[i][j] != c:
                    field[i][j] += c
                      # 같은거는 안칠하게끔
    result = 0
    for i in range(10):
        for j in range(10):
            if field[i][j] == 3:
                result += 1
    print(f'#{case} {result}')