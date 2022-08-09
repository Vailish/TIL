T = int(input())  # T = 노선 수
for case in range(1, T + 1):
    K, N, M = map(int, input().split())  # N = 종점, M = 충전기 설치 , K = 최대 이동 정류장 수
    result = 0

    # 정류장 생성
    road = [0] * N
    # 충전기 설치
    for recharger in range(N):
        if recharger % (N // K) == 0:  # 시작점이 0이기 때문에 시작점에 충전기는 항상 있음
            road[recharger] += 1
    print(road)

    # # 움직임 list
    # movement = []
    # k = K
    # while K <= N:
    #     movement.append(K)
    #     K += k

    # 도로주행



    print(f'{case} {result}')
