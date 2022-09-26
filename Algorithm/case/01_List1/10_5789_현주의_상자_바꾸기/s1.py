# 5789. 현주의 상자 바꾸기 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWYygN36Qn8DFAVm
import sys
sys.stdin = open('input.txt')

for case in range(1, 1 + int(input())):
    N, Q = map(int, input().split())  # N = 상자길이, Q = 횟수
    arr = [0] * N  # 상자
    for numb in range(1, Q+1):
        L, R = map(int, input().split())
        for i in range(L-1, R):
            arr[i] = numb
    print(f'#{case}', *arr)
