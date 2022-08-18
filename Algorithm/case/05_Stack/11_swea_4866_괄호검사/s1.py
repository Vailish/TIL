# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

for case in range(1, 1 + int(input())):
    line = input()

    # 괄호만 남긴 idx 만들기
    idx = ''
    for word in line:
        if word in ['(', ')', '{', '}']:
            idx += word
    # 스택 기본 세팅
    stack = []
    stack_size = len(idx)
    top = -1

    stack.append(idx[0])
    top += 1

    # 검사
    for i in range(1, len(idx)):
        if top == -1:  # stack이 비어있을때
            top += 1
            stack.append(idx[i])

        elif stack[top] == '(' and idx[i] == ')' or stack[top] == '{' and idx[i] == '}':
            stack.pop()
            top -= 1
        else:
            top += 1
            stack.append(idx[i])
    if top == -1:
        print(f'#{case} 1')
    else:
        print(f'#{case} 0')
