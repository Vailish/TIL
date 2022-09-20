# 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')

for case in range(1, 1 + int(input())):
    N, data = input().split()
    data_10 = int(data, 16)
    # 2진수로 변환 후 삭제된 0 채워넣기
    data_2 = bin(data_10)[2:]
    data_2 = '0'*(int(N)*4 - len(data_2)) + data_2

    print(f'#{case} {data_2}')
