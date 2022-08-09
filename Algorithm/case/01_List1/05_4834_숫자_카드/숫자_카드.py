# max 사용하지 않고 풀기

T = int(input())
for case in range(1, T + 1):
    N = int(input())  # 무 쓸모
    lst = [0] * 10
    numbers = input()  # 0으로 시작할 수 있으므로 문자열로 받음
    for ai in numbers:  # 문자열 받기
        lst[int(ai)] += 1
    frq = 0
    frq_num = 0
    for num in range(10):
        if lst[num] >= frq:  # 중복이면 제일 큰 수를 배치하기 위해 = 를 넣음
            frq_num = num
            frq = lst[num]
    print(f'#{case} {frq_num} {frq}')
