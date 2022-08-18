# 제로 실버4
# https://www.acmicpc.net/problem/10773

stack = []

for case in range(int(input())):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))
