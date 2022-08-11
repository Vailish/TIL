def counting_sort(original, k):
    counter = [0] * (k + 1)

    # 1. counter에 original 원소의 빈도수 담기
    for i in original:  # original = [0, 4, 1, 3, 1, 2, 4, 1]
        counter[i] += 1

    # 2. 누적(counter 업데이트)
    for i in range(1, len(counter)):  # counter = [1, 3, 1 ,1 ,2] -> [1, 4, 5, 6, 8] 누적값
        counter[i] += counter[i - 1]

    # 3. result 생성
    result = [-1] * len(original)
    print(result)
    # 4. result에 정렬하기(counter를 참조)
    # Stable 안정정렬의 이유로 뒤에서부터 처리하는 것(들어온 순서대로 정렬하기 위해서 같은 1이 1이 아니기 떄문에)
    for i in range(len(original) - 1, -1, -1):  # [0, 1, 1, 1, 2, 3, 4, 4]
        counter[original[i]] -= 1  # 썼으니까 빼자
        result[counter[original[i]]] = original[i]

    return result


a = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(a, 5))  # [0, 1, 1, 1, 2, 3, 4, 4]
