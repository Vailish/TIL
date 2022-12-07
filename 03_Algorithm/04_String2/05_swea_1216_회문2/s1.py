# 1216. [S/W 문제해결 기본] 3일차 - 회문2 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=1216&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1


for _ in range(10):
    case = int(input())
    # 가로 검사를 위한 arr 만들기
    arr = [input() for _ in range(100)]

    # 세로 검사를 위한 i j가 바뀐 arr_2 만들기
    arr_2 = []
    for i in range(100):
        temp = ''
        for j in range(100):
            temp += arr[j][i]
        arr_2.append(temp)

    result = 0
    for i in range(100):
        # 한 i(한 줄)당 검사
        for num in range(1, 101):  # num = 회문 길이
            for j in range(100 - num + 1):
                # 한 회문길이당 범위 검사
                word = arr[i][j:j+num]  # 가로 검사
                word_2 = arr_2[i][j:j+num]  # 세로 검사
                if word == word[::-1] or word_2 == word_2[::-1]:
                    if result < num:
                        result = num
                    break
    print(f'#{case} {result}')

    # 검사
    # stop = False
    # if not stop:
    #     for i in range(100):
    #         if not stop:
    #             for num in range(100, 2, -1):  # num = 회문 길이
    #                 if not stop:
    #                     for j in range(100 - num):
    #                         word = arr[i][j:j+num]
    #                         word_2 = arr_2[i][j:j+num]
    #                         if word == word[::-1]:
    #                             print(f'#{case} {num}')
    #                             stop = True
    #                             break
    #                         if word_2 == word_2[::-1]:
    #                             print(f'#{case} {num}')
    #                             stop = True
    #                             break
