# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# A와 B의 로직이 반복되고 있네요! 함수를 통해서 하나로 만들면 깔끔하지 않을까요?
# 풀이 - 함수

def BSA(P, Pa, cnt): # 함수 정의
    # 기본값 세팅
    l = 1  # l = 왼쪽 기준끝
    r = P  # r = 오른쪽 기준끝
    c = int((l+r)/2)  # 중간값
    cnt = 0
    while 1:
        if c < Pa:
            l = c
            c = int((l+r) / 2)
            cnt += 1
        elif c > Pa:
            r = c
            c = int((l + r) / 2)
            cnt += 1
        else:
            cnt += 1
            break
    return cnt

T = int(input())
for case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    
    countA = 0
    countB = 0
    countA = BSA(P, Pa, countA)
    countB = BSA(P, Pb, countB)

    if countA > countB:
        print(f'#{case} B')
    elif countA < countB:
        print(f'#{case} A')
    else:
        print(f'#{case} 0')
