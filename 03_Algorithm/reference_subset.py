# 부분집합의 합
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
cnt = 0
for i in range(1, 1<<N):
    s = 0
    for j in range(N):      # i의 비트로 표시되는 부분집합 원소의 합
        if i & (1<<j):
            s += arr[j]
    if s == 0:
        cnt += 1
        for j in range(N):  # i의 비트로 표시되는 부분집합 원소
            if i & (1 << j):
                print(arr[j], end = ' ')
        print()
print(f'{1<<N} 개의 부분 집합 중 {cnt}개의 부분집합 합이 0')