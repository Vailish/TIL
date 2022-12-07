for case in range(1, 1 + int(input())):
    word = input()
    stack = []

    for char in word:
        # 1) 피연산자를 만나면 스택에 push 한다.
        if char not in '*/+-':
            stack.append(int(char))
        # 2) 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고,
        # 연산 결과를 다시 스택에 push 한다.
        else:
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)

        # 3) 수식이 끝나면, 마지막으로 스택을 pop 하여 출력한다.
        print(f'#{case} {stack[-1]}')
