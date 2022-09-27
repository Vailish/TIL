def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
