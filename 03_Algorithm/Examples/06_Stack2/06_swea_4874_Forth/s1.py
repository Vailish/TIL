# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

for case in range(1, 1 + int(input())):
    idx = list(input().split())

    stack = []
    for char in idx:
        if char == '.':
            if len(stack) == 1:
                print(f'#{case} {stack[-1]}')
            else:
                print(f'#{case} error')
                break

        elif char in '*/+-':
            if len(stack) >= 2:
                x = stack.pop()
                y = stack.pop()
                if char == '*':
                    stack.append(y * x)
                elif char == '/':
                    stack.append(y // x)
                elif char == '+':
                    stack.append(y + x)
                elif char == '-':
                    stack.append(y - x)
            else:
                print(f'#{case} error')
                break

        else:
            stack.append(int(char))
