# 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


for case in range(1, int(input())+1):
    N, M = list(map(int, input().split()))  # M = 회문길이, N = 배열길이

    # 단어판 arr 생성
    arr = []
    for num in range(N):
        arr.append(input())
    # for num in range(N):
    arr_2 = []
    temp = ''
    for j in range(N):
        for i in range(N):
            temp += arr[i][j]
        arr_2.append(temp)
        temp = ''

    for i in range(N):
        for j in range(N-M+1):
            cnt = 0
            word = arr[i][j:j+M]
            if word == word[::-1]:
                print(f'#{case} {word}')
            word = arr_2[i][j:j+M]
            if word == word[::-1]:
                print(f'#{case} {word}')

# for case in range(1, int(input())+1):
#     N, M = list(map(int, input().split()))  # M = 회문길이, N = 배열길이
#
#     # 단어판 arr 생성
#     arr = []
#     for num in range(N):
#         arr.append(input())
#     # for num in range(N):
#     arr_2 = []
#     temp = ''
#     for j in range(N):
#         for i in range(N):
#             temp += arr[i][j]
#         arr_2.append(temp)
#         temp = ''
#             가로 검사
            # for num in range(M//2):
            #     if arr[i][j+num] == arr[i][j+M-1-num]:  # range 안에 안쓰고, M을 바로 써줫으니까 -1을 해줘야함!
            #         cnt += 1  # 0 1 2 3 4 5 6 7 8 9 10 11 12
            # if cnt == M//2:
            #     result = word
            #     print(f'#{case} {result}')
            #
            # # 세로 검사
            # cnt = 0
            # word = arr_2[i][j:j+M]
            # for num in range(M // 2):
            #     if arr_2[i][j + num] == arr_2[i][j + M-1 - num]:  # range 안에 안쓰고, M을 바로 써줫으니까 -1을 해줘야함!
            #         cnt += 1
            # if cnt == M // 2:
            #     result = word
            #     print(f'#{case} {result}')