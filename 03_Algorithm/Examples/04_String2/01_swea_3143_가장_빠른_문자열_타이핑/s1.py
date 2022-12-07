# 3143. 가장 빠른 문자열 타이핑 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV_65wkqsb4DFAWS

for case in range(1, int(input()) + 1):
    A, B = input().split()
    # A안에 B를 !로 바꿔주기
    A = A.replace(B, '!')
    print(f'#{case} {len(A)}')
