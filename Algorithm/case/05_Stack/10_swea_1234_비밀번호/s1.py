# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14_DEKAJcCFAYD&categoryId=AV14_DEKAJcCFAYD&categoryType=CODE&problemTitle=1234&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

# stack을 사용해서 풉시다~
# 14:00

for case in range(1, 11):
    N, nums = input().split()  # N = 문자열 길이, nums = 문자열
    N = int(N)
    stack = []
    top = -1

    stack.append(nums[0])
    top += 1

    # 검사
    for i in range(1, N):
        if top == -1:  # 스택이 비어있는 경우
            top += 1
            stack.append(nums[i])
        elif stack[top] == nums[i]:  # 같은 숫자가 연속 될 경우
            stack.pop()
            top -= 1
        else:
            top += 1
            stack.append(nums[i])
    print(f'#{case} {"".join(stack)}')