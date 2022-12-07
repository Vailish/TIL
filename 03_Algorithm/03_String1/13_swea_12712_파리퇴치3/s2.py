# + 모양 델타검색
dx1 = [0, 1, 0, -1] # 우 하 좌 상
dy1 = [1, 0, -1, 0] # 우 하 좌 상

# x 모양 델타검색
dx2 = [1, -1, -1, 1] # 우하 좌하 좌상 우상
dy2 = [-1, -1, 1, 1] # 우하 좌하 좌상 우상

for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for i in range(N):
        for j in range(N):
            # + 모양
            kill1 = arr[i][j]
            for k in range(4):
                for z in range(1, M):
                    ni = i + dx1[k] * z
                    nj = j + dy2[k] * z
                    if 0 <= ni < N and 0 <= nj < N:
                        kill1 += arr[ni][nj]
            if max_kill < kill1:
                max_kill = kill1

            kill2 = arr[i][j]
            for di, dj in [[1,1], [1,-1], [-1,-1], [-1,1]]:
                for z in range(1, M):
                    ni, nj = i+di*z, j+dj*z
                    if 0 <= ni < N and 0 <= nj < N:
                        kill2 += arr[ni][nj]
            if max_kill < kill2:
                max_kill = kill2

    print(f'#{case} {max_kill}')