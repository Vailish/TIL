# ??????????????????? 1 번 케이스 안됨!!
import sys
sys.stdin = open('input.txt')

for case in range(1, 1+int(input())):
    data = input()  # 16진수
    data_10 = int(data, 16)  # 10진수
    data_2 = bin(data_10)[2:]  # 2진수
    # print(data)
    # print(data_10)
    # print(data_2)
    for num in range(len(data_2)//7+1):
        print(int(data_2[7*num:7*num+7], 2), end=' ')
    print()
