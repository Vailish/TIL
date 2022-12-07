def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i  # 정렬할 부분 초기화

        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(numbers)
print(numbers)
