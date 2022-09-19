import sys
sys.stdin = open('input.txt')

for case in range(1, 1 + int(input())):
    data = input()
    length = len(data)
    for num in range(length//7):
        print(int(data[7*num:7*num+7], 2), end=' ')
    print()
