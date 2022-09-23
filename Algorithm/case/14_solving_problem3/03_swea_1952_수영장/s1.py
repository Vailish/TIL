# 1952. [모의 SW 역량테스트] 수영장
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpFQaAQMDFAUq&categoryId=AV5PpFQaAQMDFAUq&categoryType=CODE&problemTitle=1952&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

# 1:55
import sys
sys.stdin = open('input.txt')

def solution():
    result = []
    n = price[1]//price[0]  # n = 달과 1일 가격 비율
    m = price[2]

    # 연간회원권
    result.append(price[3])

    # 분기를 사용하는 경우
    temp = [0, 0, 0]  # 분기, 달, 일
    for i in range(0, 12):
        sum(plan[i:i+3]) != 0
        temp[0] += 1




    # 분기를 사용하지 않는 경우
    tmp = 0
    for k in range(12):
        if plan[k] > n:
            tmp += price[1]
        else:
            tmp += plan[k] * price[0]
    result.append(tmp)

    return min(result)


for case in range(1, 1 + int(input())):
    # 이용가격[일, 달, 분기, 년]
    price = list(map(int, input().split()))
    # 3개월권을 위해 추가
    plan = list(map(int, input().split())) + [0, 0]
    print(f'#{case} {solution()}')
