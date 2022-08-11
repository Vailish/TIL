T = int(input())
for case in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # 조건에 맞는 부분집합을 구해서 len이랑, sum을 사용해서 구하면 될듯
    n = len(A)
    lst = []
    count = 0
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp += [A[j]]
        lst.append(temp)
    for factor in lst:
        if sum(factor) == K and len(factor) == N:
            count += 1
    print(f'#{case} {count}')