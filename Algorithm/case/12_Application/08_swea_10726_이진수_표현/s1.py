# 10726. 이진수 표현 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXRSXf_a9qsDFAXS&categoryId=AXRSXf_a9qsDFAXS&categoryType=CODE&problemTitle=10726&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import sys
sys.stdin = open('input.txt')

for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    binary_number = bin(M)[2:]
    if len(binary_number) >= N and '0' not in binary_number[len(binary_number)-N:]:
        print(f'#{case} ON')
    else:
        print(f'#{case} OFF')
