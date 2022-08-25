def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end :
        middle = (start + end)//2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = middle -1
        else:
            start = middle + 1
    return False

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarySearch(a, len(a), 6))