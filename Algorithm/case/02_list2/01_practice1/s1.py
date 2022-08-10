tc = int(input())
for case in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0 # 각 절대값의 합의 합
    
    # 요소 하나를 이중 for 문을 통해서 꺼낸 뒤에, 네 방향 모두을 각각 절대값 차를 구함.
    # 구할 때, 조건문을 넣어서 없는 곳은 패스 하는 식으로 진행. 0과 5를 경계로
    # 구한 값을 누적으로 더해줌.
    for i in range(N):
        for j in range(N):
            arr[i][j]
            #우측
            if j < N-1:
                if arr[i][j] - arr[i][j+1] >= 0:
                    result += arr[i][j] - arr[i][j+1]
                else:
                    result -= arr[i][j] - arr[i][j+1]
            #하측
            if i < N-1:
                if arr[i][j] - arr[i+1][j] >= 0:
                    result += arr[i][j] - arr[i+1][j]
                else:
                    result -= arr[i][j] - arr[i+1][j]
            #좌측
            if j > 0:
                if arr[i][j] - arr[i][j-1] >= 0:
                    result += arr[i][j] - arr[i][j-1]
                else:
                    result -= arr[i][j] - arr[i][j-1]
            #상측
            if i > 0:
                if arr[i][j] - arr[i-1][j] >= 0:
                    result += arr[i][j] - arr[i-1][j]
                else:
                    result -= arr[i][j] - arr[i-1][j]
    print(f'#{case} {result}')