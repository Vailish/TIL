# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')
from itertools import combinations


def chk(arr):
    # triplet, run 검사
    for data in combinations(sorted(arr), 3):
        # 검사하기
        if data[0] == data[1] == data[2]:
            return 1

        data = list(set(data))
        if len(data) >= 3 and data[0] + 1 == data[1] and data[1] + 1 == data[2]:
            return 1
    return 0


def solution(cards):
    playerA = []
    playerB = []

    # 기본 카드 두 장씩 넣어주기
    for _ in range(2):
        playerA.append(cards.pop(0))
        playerB.append(cards.pop(0))

    # 한 장씩 카드 주기
    for n in range(len(cards)):  # n = 0 2 4 6 ->홀수
        if n % 2 == 0:  # 짝 수, 1, 3, 5, 7, ... playerA가 카드를 받을 때
            playerA.append(cards[n])
            if chk(playerA) >= 1:
                return 1

        # n =1 3 5 7 -> 짝수
        else:  # 홀 수, 0, 2, 4, 6, playerB가 카드를 받을 때
            playerB.append(cards[n])
            if chk(playerB) >= 1:
                return 2
    return 0


for case in range(1, 1 + int(input())):
    cards = list(map(int, input().split()))
    print(f'#{case} {solution(cards)}')
