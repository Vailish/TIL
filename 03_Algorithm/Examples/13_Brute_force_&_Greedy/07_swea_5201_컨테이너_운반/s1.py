#  5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')


def solution():
    # 큰거를 한도 큰 녀석에게 넣어주기
    # 예외처리
    if min(weights) > max(trucks):
        return 0
    weights.sort(reverse=True)
    trucks.sort(reverse=True)
    for i in range(N):
        # 트럭에 넣기
        for j in range(M):
            if load[j] == 0 and trucks[j] >= load[j] + weights[i] and trucks[j] != 0:
                load[j] += weights[i]
                break

    return sum(load)


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N 컨테이너 수, M 트럭 수
    weights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    load = [0] * M
    print(f'#{case} {solution()}')
