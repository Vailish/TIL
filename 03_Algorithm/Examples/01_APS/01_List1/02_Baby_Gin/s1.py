# 0 ~ 9 6장
T = int(input())

for case in range(T):
    numbers = list(map(int,input()))
    counts=[0] * 12
    triplet = 0
    run = 0
    baby_gin = triplet + run
    for num in numbers:
        counts[num] += 1
    if max(counts) >= 3:
        for tri in counts:
            if tri >= 3:
                counts[num] -= 3
                triplet += 1

    for r in range(len(counts)-2):
        if counts[r] >=1 and counts[r+1] >=1 and counts[r+2] >=1 :
            counts[r] -= 1
            counts[r+1] -= 1
            counts[r+2] -= 1
            run += 1

    if baby_gin > 1:
        print(f'#{case} baby-gin 입니다.')
    else:
        print(f'#{case} baby-gin이 아닙니다.')