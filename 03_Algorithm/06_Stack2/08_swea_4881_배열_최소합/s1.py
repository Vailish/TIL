# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 순열로 뽑아서 최소값 구하면 됨!
import sys
sys.stdin = open('input.txt')


from itertools import permutations


def solution():
    result = 1000000
    M = list(range(N))
    for values in permutations(M, N):
        tmp = 0
        for n in range(N):
            tmp += arr[n][values[n]]
        if result > tmp:
            result = tmp
    return result


for case in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{case}', solution())
