# 5688. 세제곱근을 찾아라 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXVyCaKugQDFAUo

def solution(n):
    length = 10**int(18/3) + 1  # N 조건식
    for i in range(1, length):
        if i**3 == n:
            return f'#{case} {i}'
    return f'#{case} -1'


for case in range(1, 1 + int(input())):
    print(solution(int(input())))
