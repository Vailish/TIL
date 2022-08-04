# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     a, b = map(int,sys.stdin.readline().split())
#     a = a%10
#     print(a**b%10)

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int,sys.stdin.readline().split())
    A = []
    for num in range(1, 11):
        a1 = a**num%10
        if a1 not in A:
            A.append(a1)
        else:
            break
    b = b % len(A)
    print(A[b])

# T = int(input())
# for tast_case in range(1, T + 1):
#     list_list = [
#         [10, 10],
#         [1, 1],
#         [2, 4, 8, 6],
#         [3, 9, 7, 1],
#         [4, 6],
#         [5, 5],
#         [6, 6],
#         [7, 9, 3, 1],
#         [8, 4, 2, 6],
#         [9, 1],
#     ]
#     A, B = map(int, input().split())
#     A_temp = A % 10
#     print(list_list[A_temp][(B % len(list_list[A_temp])) - 1])