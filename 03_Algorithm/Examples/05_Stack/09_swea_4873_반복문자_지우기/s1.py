# 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# stack으로 풀기

for case in range(1, 1 + int(input())):
    words = input()
    stack_size = len(words)
    stack = [0] * stack_size
    top = -1

    for i in range(len(words)):
        if stack[top] == words[i]:
            stack[top] = 0
            top -= 1

        else:
            top += 1
            stack[top] = words[i]
    print(stack)
    print(f'#{case} {len(stack) - stack.count(0)}')
