# 1224. [S/W 문제해결 기본] 6일차 - 계산기3 D4
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14tDX6AFgCFAYD&categoryId=AV14tDX6AFgCFAYD&categoryType=CODE&problemTitle=1224&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

for case in range(1, 11):
    # 후위 표기식으로 변경
    length = int(input())
    word = input()
    stack = []
    idx = ''

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
                # print(stack, idx, sep='#')
                stack.pop()

        else:
            idx += token
    while stack:
        idx += stack.pop()

    # 계산
    for char in idx:
        if char in '*/+-':
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
        else:
            stack.append(int(char))
    print(f'#{case} {stack[-1]}')
