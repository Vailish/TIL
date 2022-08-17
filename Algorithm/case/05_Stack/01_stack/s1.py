stack_size = 3
stack = [0] * stack_size
top = -1

# stack에 push하기
for num in range(1, 4):
    top += 1
    stack[top] = num

# stack에서 pop하기
for _ in range(3):
    temp = stack[top]
    top -= 1
    print(temp)

# stackSize = 10
# stack = [0] * stackSize
# top = -1

# top += 1        # 탑 증가
# stack[top] = 1  # stack에 push

# top += 1        # push(2)
# stack[top] = 2

# top -= 1
# temp = stack[top +1]
# print(temp)

# temp = stack[top]
# top -= 1