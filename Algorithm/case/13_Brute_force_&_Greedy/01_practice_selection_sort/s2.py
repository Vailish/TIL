def selection_sort(i):
    # 종료조건
    if i == len(numbers) - 1:
        return

    # 이번에 정렬할 곳
    min_index = i

    for j in range(i+1, len(numbers)):
        if numbers[min_index] > numbers[j]:
            min_index = j

    numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
    selection_sort(i+1)


numbers = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]
selection_sort(0)
print(numbers)
