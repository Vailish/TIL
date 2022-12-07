arr = ['A', 'B', 'C']
N = len(arr)

# 중복순열
for i in range(N):
    for j in range(N):
        for k in range(N):
            print(i, j, k, arr[i], arr[j], arr[k])

# 순열
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             if i==j or j==k or k==i:
#                 continue
#             print(i, j, k, arr[i], arr[j], arr[k])

# 조합
# for i in range(N - 2):
#     for j in range(i + 1, N-1):
#         for k in range(j + 1, N):
#             print(i, j, k, arr[i], arr[j], arr[k])

# N = 5
# arr = [i for i in range(1, N + 1)]
#
# # 3구간 분할 => (0, i), (i, j), (j, N-1)
# for i in range(1, N-2 + 1):
#     for j in range(i + 1, N - 1 + 1):
#         print(arr[0:i], arr[i:j], arr[j:N])
