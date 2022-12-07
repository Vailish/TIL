# 1223. [S/W 문제해결 기본] 6일차 - 계산기2 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14nnAaAFACFAYD&

for case in range(1, 11):
    length = int(input())
    word = input()
    idx = ''
    stack = []

    for token in word:
        if token in '*/+-()':
            if not stack or token == '(':
                stack.append(token)

            elif token in '*/':
                while stack and stack[-1] in '*/':
                    idx += stack.pop()
                stack.append(token)

            elif token in '+-':
                while stack and stack[-1] != '(':
                    idx += stack.pop()
                stack.append(token)

            elif token == ')':
                while stack and stack[-1] != '(':
                    idx += stack.pop()
                stack.pop()

        else:
            idx += token

    while stack:
        idx += stack.pop()

    for char in idx:
        if not char in '*/+-':
            stack.append(int(char))

        else:
            x = stack.pop()
            y = stack.pop()
            if char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)
            elif char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)

    print(f'#{case} {stack[-1]}')
