# 1954. 달팽이 숫자 D2
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq&categoryId=AV5PobmqAPoDFAUq&categoryType=CODE&problemTitle=1954&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

test_case = int(input())
dx = [1, 0, -1, 0]  # 우, 하, 좌, 상
dy = [0, -1, 0, 1]  # 우, 하, 좌, 상
for t in range(1, test_case + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    x, y = 0, 0
    direction = 0
    # 행렬 생성
    # while문을 써서 끝까지 델타이동시킴
    # 범위 초과거나 0이 아닌 숫자가 존재하면, 방향을 틀음
    # 이런식으로 N**2까지 진행하면 끝!

    for i in range(1, N * N + 1):
        arr[x][y] = i
        # 다음 위치 이동
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 안에 있나 & 이미 숫자가 있나
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    print(f'#{t}')
    for line in arr:
        print(*line)

# 이중 for 문으로도 해결가능


# test_case = int(input())
# dx = [1, 0, -1, 0]  # 우, 하, 좌, 상
# dy = [0, -1, 0, 1]  # 우, 하, 좌, 상
# for t in range(1, test_case + 1):
#     N = int(input())
#     # 행렬 생성
#     # while문을 써서 끝까지 델타이동시킴
#     # 범위 초과거나 0이 아닌 숫자가 존재하면, 방향을 틀음
#     # 이런식으로 N**2까지 진행하면 끝!

#     arr = [[0] * N for _ in range(N)]
#     x, y = 0, 0  # 출발 위치
#     direction = 0  # 출발 방향 0 == 오른쪽
#     nx = x + dx[direction]
#     ny = y + dy[direction]
