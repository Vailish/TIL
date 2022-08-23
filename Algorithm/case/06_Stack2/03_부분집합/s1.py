def powerset(arr, start, total):
    # 가지치기(pruning) - 합이 10 초과하면 더 진행할 필요가 없다.
    if total > 10:
        return

    # 원소의 합이 10이라면 해당
    if total == 10:
        print(arr)
        return

    for i in range(start, len(numbers)):
        # 1) i번째 원소를 뽑는다.
        arr.append(numbers[i])

        # 2) 재귀함수 진행
        powerset(arr, i + 1, total + numbers[i])

        # 3) 재귀함수 종료 후, 뽑았던 i번째 원소 삭제
        arr.pop()


numbers = list(range(1, 11))
powerset([], 0, 0)
