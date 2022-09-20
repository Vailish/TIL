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
    data_2 = '0' * (4 * len(data) - len(bin(data_10)[2:])) + bin(data_10)[2:]
    numbers = data_2
    result = ''
    while True:
        for n in range(len(numbers)-6):
            if numbers[n:n+6] in index_key:
                result += ' ' + str(index_key.index(numbers[n:n+6]))
                numbers = numbers[0:n] + numbers[n+6:]
                break
        if numbers[n:n+6] not in index_key:
            break
    print(result)
