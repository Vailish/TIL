# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산 D4
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


import sys
sys.stdin = open('input.txt')
from collections import deque


def caculator(idx, num):
    if idx == '+1':
        return num + 1
    elif idx == '-1':
        return num - 1
    elif idx == '*2':
        return num * 2
    else:  # n == '-10'
        return num - 10


def bfs(num, target):
    only_one = set()  # 백트래킹용
    queue = deque([])
    t = 0
    queue.append((num, t))
    while queue:
        num, t = queue.popleft()

        if num == target:
            return t

        for i in range(4):
            x = ['-1', '+1', '-10', '*2'][i]
            new_num = caculator(x, num)

            if 0 <= new_num <= 1000000 and new_num not in only_one:
                only_one.add(new_num)
                queue.append((new_num, t+1))


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N 숫자를 M 숫자로
    print(f'#{case}', bfs(N, M))
