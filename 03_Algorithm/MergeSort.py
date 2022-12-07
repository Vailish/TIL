def merge(left, right):
    merged_arr = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged_arr.append(right[j])
            j += 1
        else:
            merged_arr.append(left[i])
            i += 1
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def merge_sort(arr):
    # 종료조건
    if len(arr) <= 1:
        return arr

    middle = len(arr)//2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    return merge(left_arr, right_arr)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
