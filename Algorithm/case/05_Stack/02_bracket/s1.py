for case in range(1, int(input()) + 1):
    ipt = input()
    stack_size = len(ipt)
    stack = [0] * stack_size
    top = -1
    for idx in ipt:
        if idx == '(':
            top += 1
            stack[top] = '('
        else:                    # idx == ')'
            top -= 1
    if top == -1:
        print('정상입니다.')
    else:
        print('괄호가 짝이 맞지 않습니다.')