# 1859. 백만 장자 프로젝트 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

# 2h, 앞으로는 변수 변경할 때 하나하나 확인 좀 잘하자..., 그리고 메모리도 신경써봐야할듯..
import sys
sys.stdin = open('input.txt')


for case in range(1, 1 + int(input())):
    days = int(input())  # 총 기간
    info = list(map(int, input().split()))  # 각 날 별 매매가

    # 최대값 찾고, 최대값 기준으로 앞부분 처리 후 삭제, 반복(마지막 자리가 최대값이 될때까지)
    # 최대값 = 최대값 * 개수 - 해당지점까지 총합
    revenue = 0  # 수익
    max_price = max(info)
    while True:
        max_price = max(info)
        if max_price == info[-1]:
            revenue += max_price * len(info) - sum(info)
            break
        elif max_price == info[0]: # 최고가가 제일 앞에(역리스트에서는 제일 뒤)
            del info[0]
        else:
            max_prince = max(info)
            max_point = info.index(max_price)
            revenue += max_price * len(info[:max_point]) - sum(info[:max_point])
            del info[:max_point]

    print(f'#{case} {revenue}')


# runtime error
#
# for case in range(1, 1 + int(input())):
#     days = int(input())  # 총 기간
#     info = list(map(int, input().split()))  # 각 날 별 매매가

#     # index를 위해서 수열을 뒤집어서 배치, 최대값 찾고, 최대값 기준으로 앞부분 처리 후 삭제, 반복(마지막 자리가 최대값이 될때까지)
#     # 최대값 = 최대값 * 개수 - 해당지점까지 총합
#     info_reverse = info[::-1]
#     revenue = 0  # 수익
#     max_price = max(info_reverse)
#     while True:
#         max_price = max(info_reverse)
#         if max_price == info_reverse[0]:
#             revenue += max_price * len(info_reverse) - sum(info_reverse)
#             break
#         elif max_price == info_reverse[-1]: # 최고가가 제일 앞에(역리스트에서는 제일 뒤)
#             del info_reverse[-1]
#         else:
#             max_prince = max(info_reverse)
#             max_point = info_reverse.index(max_price)
#             revenue += max_price * len(info_reverse[max_point:]) - sum(info_reverse[max_point:])
#             del info_reverse[max_point:]

#     print(f'#{case} {revenue}')