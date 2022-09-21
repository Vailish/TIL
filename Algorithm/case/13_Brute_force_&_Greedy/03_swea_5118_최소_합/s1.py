import sys
sys.stdin = open('input.txt')

# bfs
# 경로 검색이고, 최대값을 구하는 방법이기 때문에 bfs를 선택
# 방법은 이동시 visited에 움직인 누적 수를 기록하고, 다시 기록해야할 경우에는
# 조건을 걸어서 더 작은 수를 기록하여 갱신하게 한다면, 그 지점까지 도착하는 최소값은
# 최종 갱신한 값이 될 것이다. 이처럼 계속해서 끝까지 내려간다면,
# 원하는 목적지에 도달했을 때, 최소값을 구할 수 있게 된다.

dx = [0, 1]  # 우, 하
dy = [1, 0]  # 우, 하


def bfs(x, y):
    visited = [[100] * N for _ in range(N)]  # 최소값을 구하려면 큰 값이 들어가야 방해가 안됨
    visited[x][y] = field[x][y]
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
                                              # 새로갈점(기존값) >= 새로 비교할 값 최소값이니까
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] >= visited[x][y] + field[nx][ny]:
                visited[nx][ny] = visited[x][y] + field[nx][ny]
                queue.append((nx, ny))

    return visited[N-1][N-1]


for case in range(1, 1 + int(input())):
    N = int(input())  # 한 변의 길이
    field = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{case} {bfs(0,0)}')
