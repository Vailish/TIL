# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
import sys
sys.stdin = open('input.txt')


for case in range(1, 1 + int(input())):
    N = int(input())  # N = 신청서
    time = []
    for _ in range(N):
        value = list(map(int, input().split()))
        time.append(value)
    time = sorted(time, key=lambda x: x[1])

    # 끝나는 시간을 기준으로 붙여주되, 시작시간으로 검증 해보기
    result = [time[0]]
    for t in time[1:]:
        if result[len(result)-1][1] <= t[0]:
            result.append(t)

    print(f'#{case} {len(result)}')
