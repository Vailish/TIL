import sys

sys.stdin = open("input.txt")

T = int(input())
for case in range(1, T + 1):
    num = int(input())  # 쓸모없음
    N = list(map(int, input().split()))
    Max_num = 0
    Min_num = 1000001
    for ai in N:  # 각각 기준 ai와 비교하여 최대값과 최소값을 구해줌
        if ai > Max_num:
            Max_num = ai
        if ai < Min_num:
            Min_num = ai
    print(f'#{case} {Max_num - Min_num}')
