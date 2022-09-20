dic_2 = {'0': '1',
         '1': '0'}
data_2 = '1010'
data_3 = '212'

# 2진수 한 자리 변경
print(data_2)
for num in range(len(data_2)):
    value = data_2[:num] + dic_2.get(data_2[num]) + data_2[num + 1:]
    print(value)