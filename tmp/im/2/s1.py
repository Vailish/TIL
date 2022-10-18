# 정사각형 판정 D3
# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AYNvZzWKWCYDFAUs&contestProbId=AX8BAN1qTwoDFARO&probBoxId=AYOi82QqVVsDFAXj&type=PROBLEM&problemBoxTitle=1005&problemBoxCnt=4

import sys
sys.stdin = open('input.txt')


def solution():
    cnt_A = 0
    cnt_B = 0
    tmp = set()
    for i in range(N):
        switch_A = False
        switch_B = False
        switch_count_A = 0
        switch_count_B = 0
        for j in range(N):
            if field[i][j] == '#':
                switch_A = True
            else:
                switch_A = False
                if cnt_A != 0:
                    tmp.add(cnt_A)
                    cnt_A = 0

            if switch_A:
                cnt_A += 1

            # 세로 검사

            if field[j][i] == '#':
                switch_B = True
            else:
                switch_B = False
                if cnt_B != 0:
                    tmp.add(cnt_B)
                    cnt_B = 0

            if switch_B:
                cnt_B += 1




        print(switch_count_A, switch_count_B)
        if switch_count_A != 1 and switch_count_B != 1:
            return 'no'

    if len(tmp) == 1:
        return 'yes'
    return 'no'


for case in range(1, 1+int(input())):
    N = int(input())
    field = list(input() for _ in range(N))
    print('#' + str(case), solution())
