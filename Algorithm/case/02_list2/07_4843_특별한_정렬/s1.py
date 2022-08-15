T = int(input())
for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(len(arr)-1, 0, -1):  #bubble sort
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    arr_spepcial_sort = []
    for num in range (10):
        if num % 2:  # 짝수
            arr_spepcial_sort.append(arr[int(num/2 -0.5)])  # 1, 3, 5, ... -> 0, 1, 2, ...
        else:  # 홀수
            arr_spepcial_sort.append(arr[int(-num/2 -1)])  # 0, 2, 4, 6 ... -> -1, -2, -3 ...
    print(f'#{case}', end=' ')
    for result in arr_spepcial_sort:
        print(result, end=' ')
    print()
    # print(f'#{case} {arr_spepcial_sort}')
 # f-string 에서 asterisk 사용불가
 # https://stackoverflow.com/questions/55933956/what-does-a-star-asterisk-do-in-f-string

# 카운트함수 trial
# counts = [0] * 100
#     arr_sort = [0] * 100
#     for num in arr:
#         counts[num] += 1

#     for i in range(1, len(counts)):
#         counts[i] += counts[i - 1]
#     for i in range(len(arr_sort) - 1, -1, -1):
#         counts[arr[i]] -= 1
#         arr_sort[counts[arr[i]]] = arr[i]