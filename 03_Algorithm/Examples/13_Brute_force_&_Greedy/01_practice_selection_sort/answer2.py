# 재귀를 이용

def selection_sort(i):
    # 종료 조건(마지막 원소일 때)
    if i == len(numbers) - 1:
        return

    min_index = i  # 바꿀 부분

    # i 이후에 최소값 인덱스찾기
    for j in range(i+1, len(numbers)):
        if numbers[min_index] > numbers[j]:
            min_index = j

    numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
    selection_sort(i + 1)  # 재귀호출

numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(0)  # 0번째 원소부터 정렬 시작
print(numbers)
