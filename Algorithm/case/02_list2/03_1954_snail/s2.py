# 1954_달팽이_숫자

# import sys

# sys.stdin = open('input.txt')

# 1. 델타값 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for t in range(1, int(input()) + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    x, y = 0, 0  # 출발 위치
    direction = 0  # 처음 출발 방향 오른쪽

    for i in range(1, n * n + 1):
        snail[x][y] = i
        # 다음 위치 이동
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 안에 있어? & 이미 숫자 없어?
        if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
            x = nx  # 이동 하자!
            y = nx
        else:
            # 방향을 바꿔서 다시 이동하자!
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    print(f'#{t}')

    # 1. 언패킹 출력
    for line in snail:
        print(*line)

    # 2. 이중 for문 출력
    # for i in range(n):
    #     for j in range(n):
    #         print(snail[i][j], end=' ')
    #     print()
    
    # 3. join을 이용한 출력 (비권장)
    # print(f'#{t}', '\n'.join(' '.join(map(str, line)) for line in snail), sep='\n')