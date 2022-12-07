arr = [1, 3, 3, 5, 6]
n = len(arr)
result = []
temp = []
for i in range(1<<n): #1<<n : 부분 집합의 개수
    for j in range(n): #원소의 수만큼 비트를 비교함
        if i & (1<<j): # i의 j번 비트가 1인경우
            temp.append(arr[j])
    result.append(sum(temp))
    temp = []
print(result)