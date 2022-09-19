#### 끄아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ?????????????????
import sys
sys.stdin = open('input.txt')

index_key = ['001101', '010011',
             '111011', '110001',
             '100011', '110111',
             '001011', '111101',
             '011001', '101111']

for case in range(1, 1+int(input())):
    data = input()
    data_10 = int(data, 16)
    data_2 = bin(data_10)
    k = 0
    while k <= 3:
        for idx in index_key:
            if idx in data_2[2:]:
                print(index_key.index(idx), end=' ')
                n = data_2.index(idx)
                data_2 = data_2[0:n] + data_2[n+6:]
        k += 1
    print()