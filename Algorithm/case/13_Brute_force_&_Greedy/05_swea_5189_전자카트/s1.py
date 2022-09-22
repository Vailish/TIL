# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')
from itertools import permutations


def solution():  # 시작점 (0,0) 종료점 (0,0)
    result = []
    for path in permutations(node, N-1):
        queue = [0]
        temp = 0
        # 1 2

        for point in path:
            start = queue.pop(0)
            temp += arr[start][point]
            queue.append(point)
        start = queue.pop(0)
        temp += arr[start][0]
        result.append(temp)

    return min(result)


for case in range(1, 1 + int(input())):
    N = int(input())  # 배열 한 변의 길이
    node = [i for i in range(1, N)]
    visited = [False] * N
    arr = [list(map(int, input().split())) for _ in range(N)]  # 전력 소비량
    print(f'#{case} {solution()}')
