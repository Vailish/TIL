arr = [3, 6, 7, 1]
n = len(arr) #원소의 개수
lst = []
for i in range(1<<n): #1<<n : 부분 집합의 개수
    temp = []
    for j in range(n): #원소의 수만큼 비트를 비교함
        if i & (1<<j): # i의 j번 비트가 1인경우
            temp += [arr[j]] # j번 원소 출력
    lst += [temp]
print(lst)