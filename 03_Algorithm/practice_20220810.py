# selection sort
def select(arr, k):  # k번째 까지 작은 원소들을 찾아 배열의 앞쪽으로 이동, k번째 반환
    for i in range(0, k):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[i]:
                minInex = j
                arr[minIndex], arr[i] = arr[i], arr[minIndex]
    return arr[k-1]

a = [6, 2, 4, 5, 1]
print(select(a, 4))