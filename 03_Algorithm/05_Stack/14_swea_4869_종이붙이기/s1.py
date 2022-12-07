# 4869. [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

memo = [0, 1, 3]
for case in range(1, 1 + int(input())):
    n = int(int(input()) / 10)
    while True:
        if len(memo) - 1 < n:
            for num in range(n+1):
                if len(memo) == num:
                    memo.append(memo[num-2]*2 + memo[num-1])
        else:
            print(f'#{case} {memo[n]}')
            break
