import sys
sys.stdin = open('input.txt')

for case in range(1, 1+int(input())):
    data = input()  # 16진수 24bit
    data_10 = int(data, 16)  # 10진수, 이 순간 앞의 0은 str에서 int로 바뀌면서 사라지게 됨
    data_2 = '0'*(4 * len(data) - len(bin(data_10)[2:])) + bin(data_10)[2:]  # 사라진 0을 살리기 위한 작업

    for num in range(len(data_2)//7+1):  # 15 -> 2 1
        print(int(data_2[7*num:7*num+7], 2), end=' ')
    print()
