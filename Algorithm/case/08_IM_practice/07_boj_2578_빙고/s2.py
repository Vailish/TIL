def Bingo(call):
    row_cnt = [0,0,0,0,0]
    col_cnt = [0,0,0,0,0]
    l_cnt = [0,0]
    cnt = 0
    result = 0
    stop = 0
    while cnt < 3:
        for c in call:
            result += 1
            i, j = my_dict[c]
            row_cnt[i] += 1    # mi행의 cnt값을 +1해준다
            col_cnt[j] += 1    # mj열의 cnt값을 +1해준다
            if i+j == 4:       # 역대각 처리
                l_cnt[1] += 1
                if l_cnt[1] == 5:
                    cnt += 1
                    l_cnt[1] = 0
            # 대각 처리
            elif i == j:
                l_cnt[0] += 1
                if l_cnt[0] == 5:
                    cnt += 1
                    l_cnt[0] = 0

            # i,j가 현재 위치일것
            if 5 in row_cnt:
                cnt += 1
                row_cnt[i] = 0
            if 5 in col_cnt:
                cnt += 1
                col_cnt[j] = 0
            if cnt >= 3:
                stop = 1
                break
        if stop:
            break
    print(result)


arr = [list(map(int,input().split())) for _ in range(5)]


my_dict = {}
for i in range(len(arr)):
    for j in range(len(arr)):
        my_dict[arr[i][j]] = (i, j)

call = []
for i in range(5):
    call.extend(list(map(int,input().split())))
Bingo(call)