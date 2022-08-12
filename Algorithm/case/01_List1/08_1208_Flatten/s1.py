for case in range(1, 11):
    dump = int(input())  # 덤프 횟수
    boxes = list(map(int, input().split()))  # 필드?

    t = 0
    while t != dump:
        max_point = 1
        max_location = 0
        min_point = 101
        min_location = 0
        # 최고점과 최저점을 구한다
        for turn in range(100):
            if boxes[turn] > max_point:
                max_point = boxes[turn]
                max_location = turn
            if boxes[turn] < min_point:
                min_point = boxes[turn]
                min_location = turn
        max_point -= 1
        min_point += 1
        boxes[max_location] -= 1
        boxes[min_location] += 1
        t += 1
    # 한 번더 하는 이유는 max_point, max_min의 경우에는
    # 같은 높이가 있는 상태에서도 1을 바로 빼기 때문에
    # 최대값과, 최소값을 다 한 뒤에 한 번 더 구해줘야함!
    for turn in range(100):
        if boxes[turn] > max_point:
            max_point = boxes[turn]
        if boxes[turn] < min_point:
            min_point = boxes[turn]

    print(f'#{case} {max_point - min_point}')
    # 최고점에서 1을 뺀 뒤 최저점에 1을 더한다
    # 최고점과 최저점의 차이를 구한다
### counting 정렬로 풀어 볼 수 도 있음
