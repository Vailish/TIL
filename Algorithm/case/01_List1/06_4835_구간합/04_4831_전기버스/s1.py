# sum, max, min, sort 사용하지 말고 하기

T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    # 인접한 M개의 행 더한 값 끼리 비교하기(최대와 최소 구하기)
    max_num = 0
    min_num = 10000 * M  # M개만큼 더하니까 최소값도 그 만큼 올려야함
    for num in range(N - M + 1):  # N, M의 관계를 설정해서 for문 범위 구하는데 힘들엇음;
        sum_data = 0
        # M개가 들어가야지...
        for m in range(M):
            sum_data += data[num + m]
        if sum_data > max_num:
            max_num = sum_data
        if sum_data < min_num:
            min_num = sum_data
    print(f'#{case} {max_num - min_num}')

# -------------------------------
# sliding window
# 처음 한 번만 더하고 그 뒤는 for문을 이용해서 좌측 빼고 우측을 더하는 식으로 계산하는 방법
