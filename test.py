# print('apple'.find('p')) #1
# print('apple'.find('k')) #-1 (없음)
# print('apple'.index('k')) #Error



#extend
day_name = ('월', '화', '수', '목', '금')
print(type(day_name))
print(day_name[-3])
print(day_name * 2)
print(id(day_name))
day_name += False, True
print(id(day_name)) # 새로만든것
print(day_name)

#in 멤버십 연산자(Membership Operator)
print('apple' in 'a') # False
print('a' in 'apple') # True

