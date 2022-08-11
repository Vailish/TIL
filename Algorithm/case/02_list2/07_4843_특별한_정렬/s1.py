T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    counts = [0] * 101
    arr_sort = [0] * 101
    for num in arr:
        counts[num] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]
    for i in range(len(arr_sort) - 1, -1, -1):
        counts[arr[i]] -= 1
        arr_sort[counts[arr[i]]] = arr[i]
    print(arr_sort)
