#파이썬은 스택을 따로 구현할 필요 없이, 리스트 자료형을 스택처럼 사용할 수 있다.
# size와 is_full은 필요없다. 파이썬은 리스트의 크기를 자동으로 늘려주고 줄여주기 때문이다.
my_stack = []  # 스택 생성

# push
my_stack.append(1)
my_stack.append(2)

# pop
my_stack.pop()

# peek
print(my_stack[-1])

# is_empty
if not my_stack:
    print('스택이 비었습니다.')