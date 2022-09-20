# 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')

for case in range(1, 1 + int(input())):
    n = float(input())
    result = ''

    while n != 0.0:
        # 13이상 길어지면 overflow출력
        k = len(result) + 1
        if k >= 13:
            result = 'overflow'
            break
        # 그 외에 붙여줌
        else:
            if n >= 2**(-k):
                result += '1'
                n -= 2**(-k)
            else:
                result += '0'
    print(f'#{case} {result}')
