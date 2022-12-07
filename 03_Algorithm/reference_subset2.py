# 부분합2
def f(i, N, s):
    global cnt
    if i == N:
        if s == 0 and sum(bit) != 0:
            cnt += 1
            for j in range(N):
                if bit[j]:
                    print(arr[j], end = ' ')
            print()
    else:
        bit[i] = 0
        f(i+1, N, s)
        bit[i] = 1
        f(i+1, N, s + arr[i])

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N
cnt = 0
f(0, N, 0)
print(cnt)