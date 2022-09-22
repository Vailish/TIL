# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD

import sys
sys.stdin = open('input.txt')


for case in range(1, 1 + int(input())):
    numbers, chance = map(int, input().split())
    search(chance)
    result = 0
    print(f'#{case} {result}')
