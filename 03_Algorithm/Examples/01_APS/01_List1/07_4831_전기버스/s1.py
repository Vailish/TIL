#https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

T = int(input())  # T = 노선 수
for case in range(1, T + 1):
    K, N, M = map(int, input().split())  # N = 종점, M = 충전기 설치 , K = 최대 이동 정류장 수
    rechargers = list(map(int, input().split())) # rechargers = 충전기 위치정보
    
    # 정류장 생성 0 ~ (N-1) = N개 이고, 끝자리에서 K만큼 더 갈 수 있으므로 오류방지
    road = [0] * (N)  + [1] * K
    for recharger in rechargers: # 충전기 설치
        road[recharger] += 1

    location = 0
    movement = 0
    step = 0
    # 주행
    # 만약 K거리 안에(최대 이동거리) 정류장이 있으면 이동(제일 뒤에 있는곳으로)
    # 만약 K거리 안에 없으면 0을 출력
    while location < N:
        if 1 not in road[location+1 : location + K+1]:
            movement = 1
            break

        # for idx in road[location+1 : location + K+1]:
        #이 아닌 range(K)를 써줘야 location 위치를 잡아주기 편함
        for idx in range(1, K+1): # 이 과정을 통해서 최고 멀리있는 충전소로 이동
            if road[location + idx]:
                step = location + idx
        location = step
        movement += 1
    
        # for idx in road[location+1 : location + K+1]:
        #     if idx:
        #         step = idx
        #     print(f'idx{idx}')
        # location = step
        # movement += 1
        # print(f'location = {location}')
        # break
    print(f'#{case} {movement-1}') #마지막 이동은 충전하지 않으니까 -1