# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 풀이 - 전개

T = int(input())
for case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    lf = 1  # lf = 왼쪽 기준끝
    k = P  # k = 오른쪽 기준끝
    c = int((lf+k)/2)  # 중간값
    countA = 0
    countB = 0
    while 1:
        if c < Pa:
            lf = c
            c = int((lf+k) / 2)
            countA += 1
        elif c > Pa:
            k = c
            c = int((lf + k) / 2)
            countA += 1
        else:
            countA += 1
            break
    lf = 1
    k = P
    c = int((lf+k)/2)
    while 1:
        if c < Pb:
            lf = c
            c = int((lf+k) / 2)
            countB += 1
        elif c > Pb:
            k = c
            c = int((lf + k) / 2)
            countB += 1
        else:
            countB += 1
            break
    if countA > countB:
        print(f'#{case} B')
    elif countA < countB:
        print(f'#{case} A')
    else:
        print(f'#{case} 0')
