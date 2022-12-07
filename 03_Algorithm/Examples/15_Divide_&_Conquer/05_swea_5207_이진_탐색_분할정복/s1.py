# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 2시 시작
import sys

sys.stdin = open('input.txt')


def binary_search(left, right, way):  # 0은 시작점, 그 뒤로는 l, r
    global cnt

    if left > right:
        return

    middle = (left + right) // 2

    if A[middle] == B[m]:  # 아래 첫회일때 리턴이 있기 때문에, 그 전에 처음 m = 값일 때를 앞에서 처리해줘야함
        cnt += 1
        return

    if way == 0:  # 첫 번째 일때
        binary_search(left, middle - 1, 'l')
        binary_search(middle + 1, right, 'r')
        return

    if A[middle] == B[m]:  # 같은 값일 때
        cnt += 1
        print(m)
        return
    elif A[middle] > B[m]:
        if way == 'l':
            return
        binary_search(left, middle - 1, 'l')
        return
    else:
        if way == 'r':
            return
        binary_search(middle + 1, right, 'r')
        return


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    for m in range(M):
        binary_search(0, N - 1, 0)
    print(f'#{case}', cnt)

# # 하나씩 뽑아서 확인해본다
# def binary_search(target):
#     left = 0
#     right = len(A) - 1
#     middle = len(A) // 2
#
#     if A[-1] < target:
#         return False
#
#     while middle != left and middle != right:
#         if A[middle] > target:
#             right = middle
#             middle = (left + right) // 2
#         elif A[middle] < target:
#             left = middle
#             middle = (left + right) // 2
#         else:  # A[middle] == target
#             return True
#
#     return False
#
#
# for case in range(1, 1 + int(input())):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     result = 0
#     for num in B:
#         print(num, binary_search(num))
#         if binary_search(num) == True:
#             result += 1
#
#     print(f'#{case}', result)
