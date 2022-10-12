# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD

import sys
sys.stdin = open('input.txt')


def solution(n):
    global max_value
    if n == chance:
        tmp = int(''.join(numbers))
        if max_value < tmp:
            max_value = tmp

    else:  # 재귀
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                temp = int(''.join(numbers))
                if (n, temp) not in check:
                    check.add((n, temp))
                    solution(n+1)
                # 확인 다 했으면 원복
                numbers[i], numbers[j] = numbers[j], numbers[i]


for case in range(1, 1 + int(input())):
    numbers, chance = input().split()
    numbers = list(numbers)
    chance = int(chance)
    check = set()  # 중복 확인
    max_value = 0
    solution(0)
    print(f'#{case}', max_value)











# 너무 오래걸려서 실패
# from itertools import combinations
# from collections import deque
#
#
# def solution():
#     result = set()
#     queue = []
#     for x, y in combinations(range(len(numbers)), 2):
#         arr = numbers[:]
#         arr[x], arr[y] = arr[y], arr[x]
#         queue.append((arr, 1))
#
#         while queue:
#             arr, cnt = queue.pop(0)
#
#             for i, j in combinations(range(len(numbers)), 2):
#                 arr[i], arr[j] = arr[j], arr[i]
#
#                 if cnt == chance - 1:
#                     result.add(arr)
#                 else:
#                     queue.append((arr, cnt + 1))
#
#
#     return max(result)
#
#
# for case in range(1, 1 + int(input())):
#     nums, chance = map(int, input().split())
#     numbers = []
#     for number in str(nums):
#         numbers.append(int(number))
#     print(f'#{case}', solution())
