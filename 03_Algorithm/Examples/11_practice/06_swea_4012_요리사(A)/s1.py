# 4012. [모의 SW 역량테스트] 요리사
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWIeUtVakTMDFAVH

# 소요시간 150m

import sys
sys.stdin = open('input.txt')

from itertools import combinations


def solution(n):
    # n개의 숫자에서 n/2개를 뽑고 (부분집합)
    result = []
    numbers = list(i for i in range(n))
    for numbers_a in combinations(numbers, n//2):
        numbers_b = list(set(numbers) - set(numbers_a))
        numbers_a = list(numbers_a)
        # 나온 숫자들로 두 개를 뽑아 순열을 돌고
        tmp_a = 0
        for i, j in combinations(numbers_a, 2):
            # 그 값들을 배열에 넣어서 값들을 전부 더한다.
            tmp_a += S[i][j] + S[j][i]
        # 반대(B)의 요리도 같은 방식으로 진행한다.
        tmp_b = 0
        for x, y in combinations(numbers_b, 2):
            tmp_b += S[x][y] + S[y][x]
        # A와 B의 차를 구한다
        result.append(abs(tmp_a - tmp_b))
    return min(result)


for case in range(1, 1 + int(input())):
    N = int(input())  # N = 식재료 수
    S = [list(map(int, input().split())) for _ in range(N)]  # S
    print(f'#{case} {solution(N)}')

    # 이런 방식이 아니라 N개를 반으로 나눠서 반은 A 반은 B에 쓰는것
    # lst = list(x for x in range(n))
    # result = []
    # for a in combinations(lst, 2):
    #     for b1, b2 in combinations(lst, 2):
    #         if b1 not in a or b2 not in a:
    #             a1, a2 = a
    #             print(a1, a2, b1, b2)
    #             result.append(abs((S[a1][a2] + S[a2][a1]) - (S[b1][b2] + S[b2][b1])))
    # print(result)
    # return min(result)


# 재료 중첩사용 제거 못해서 실패
# def solution(n):
#     taste = []
#     # for 문을 다 돌면서 시너지의 합들을 전부 taste에 넣어줌
#     for i in range(n):
#         for j in range(n):
#             if i > j:
#                 taste.append(S[i][j] + S[j][i])
#     print(taste)
#     # 그냥 계산하는게 아니라 사용하면 사용한 요소는 제외 시키고 남은 애들과 차를 구해야하는듯
#     # 두 원소의 차의 최소값
#     result = []
#     for data1, data2 in combinations(taste, 2):
#         temp = abs(data1 - data2)
#         if temp == 0:
#             return 0
#         result.append(temp)
#     return min(result)
#
#
# for case in range(1, 1 + int(input())):
#     N = int(input())  # N = 식재료 수
#     S = [list(map(int, input().split())) for _ in range(N)]
#     print(f'#{case} {solution(N)}')