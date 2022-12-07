# 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')
from collections import deque


def solution():
    stack = deque([(1, 0)])  # 위치, 이동횟수
    while stack:
        location, turn = stack.popleft()
        for n in range(1, recharger[location] + 1):
            if location + n >= len(recharger):
                return turn
            else:
                stack.append((location + n, turn + 1))
    return -1


for case in range(1, 1 + int(input())):
    recharger = list(map(int, input().split()))  # 도착0, 시작1, 도착 len(recharger)
    print(f'#{case}', solution())
