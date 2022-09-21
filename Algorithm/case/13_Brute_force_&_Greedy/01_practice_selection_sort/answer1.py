# 반복문 이용

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i  # 비정렬 부분 중 제일 앞으로 초기화

        # 맨 앞 인덱스 + 1 부터 비교하여 최소값 인덱스를 넣어주기
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # 맨 앞 인덱스와 최소값 인덱스를 위치 변경
        arr[i], arr[min_index] = arr[min_index], arr[i]


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(numbers)
print(numbers)
