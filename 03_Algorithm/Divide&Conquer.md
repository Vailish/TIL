# 분할정복
1. 퀵정렬
2. 병합정렬
3. 이진탐색

### 병합정렬
A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
M = [1, 2, 3, 4, 5, 6, 7, 8]
- 각각 최소한으로 쪼갠 뒤에
- 쪼갠 순서 반대로 병합해서 합쳐주는 방법
  - 합칠 때, 앞에 꺼부터 비교하면서 붙여주고, 한 쪽이 남으면 그대로 붙이기
- O(nlogn) : logn = 반씩 쪼갬
- 속도는 빠르긴 하지만 추가적으로 메모리를 많이 사용함.
```python
# 병합 정렬

def merge(left, right):
    merged_arr = []
    i, j = 0, 0  # 왼쪽, 오른쪽 리스트 각각의 인덱스

    while i < len(left) and j < len(right):
        # 왼쪽 리스트의 원소가 작거나 같으면 삽입
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        # 오른쪽 리스트의 원소가 작으면 삽입
        else:
            merged_arr.append(right[j])
            j += 1

    # 왼쪽과 오른쪽 리스트 중 하나라도 원소를 모두 소모하면, 남은 리스트의 원소를 모두 삽입
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def merge_sort(arr):
    # 더 이상 분할할 수 없는 경우(종료 조건)
    if len(arr) <= 1:
        return arr

    # 1. 리스트를 분할하여 각각 정렬
    middle = len(arr) // 2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    # 2. 정렬된 두 리스트를 병합
    return merge(left_arr, right_arr)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 퀵정렬
- O(nlogn)
- 분할정복, pivot(피벗)
- Quick 정렬의 단점
  - O(n**2) 일 수 가 있음
  - 기본적으로 pivot이 가운데 값이라고 생각하고 진행하기 떄문에 nlogn이 되는 건데, 운이 나빠서 계속 사이드 값만 뽑게되면 n**2이 될 수 있다.

```python
# 퀵정렬 - 1) 호어 방식

def partition(arr, left, right):
    pivot = arr[left]  # 가장 왼쪽 원소를 피벗으로 지정
    i, j = left, right

    while i <= j:
        # 1. 피벗보다 큰 값이 나올 때까지 i + 1
        while i <= j and arr[i] <= pivot:
            i += 1

        # 2. 피벗보다 작은 값이 나올 때까지 j - 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        # 3. 피벗보다 작은 값은 왼쪽으로, 큰 값은 오른쪽으로 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]  # i > j가 되면 피벗과 j 위치 원소 교환 (피벗을 가운데로 옮기는 작업)

    return j


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)  # 피벗을 기준으로 왼쪽, 오른쪽을 나누는 가운데 위치 구하기
        quick_sort(arr, left, middle - 1)  # 왼쪽 퀵정렬
        quick_sort(arr, middle + 1, right)  # 오른쪽 퀵정렬


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
```

```python
# 퀵정렬 - 2) 로무토 방식

def partition(arr, left, right):
    pivot = arr[right]  # 가장 오른쪽 원소를 피벗으로 지정
    i, j = left - 1, left

    while j < right:
        if pivot > arr[j]:
            i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle - 1)
        quick_sort(arr, middle + 1, right)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(numbers, 0, len(numbers) - 1)
print(numbers)
```

```python
# 퀵정렬 - 3) 파이썬스러운 방식 but 메모리 더 많이 씀

def quick_sort(arr):
    # 더 이상 분할할 수 없는 경우(종료 조건)
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 가장 왼쪽 원소를 피벗으로 지정
    arr = arr[1:]  # 피벗 제외하여 새로운 리스트 생성

    left_arr = [i for i in arr if i <= pivot]  # 피벗보다 작거나 같은 원소는 왼쪽으로 분할
    right_arr = [j for j in arr if j > pivot]  # 피벗보다 큰 원소는 오른쪽으로 분할

    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


numbers = [3, 2, 4, 6, 9, 1, 8, 7, 5]
print(quick_sort(numbers))
```