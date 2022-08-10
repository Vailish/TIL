def is_sum_zero(nums):
    arr = list(map(int, nums.split()))
    result = 0
    lst = []
    n = len(arr)
    for i in range(1<<n):
        temp = []
        for j in range(n):
            if i & (1<<j):
                temp += [arr[j]]
        lst.append(temp)
    for num in lst:
        if sum(num) == 0 and num != []: # 기본적으로 []가 들어가기 떄문에 이를 제거하지 않으면 모든 부분합은 최소 1개 이상의 0을 가지게 됨
            result = 1
    return result

tc = int(input())
for case in range(tc):
    print(f'#{case} {is_sum_zero(input())}')

'''
비트 마스크(bit masks)

- 간단하게 생각해서 리스트의 ‘자리’를 모아둔 것이라고 생각하면 됨
- 그래서 0일 때는 없는 것 1일 때는 존재하는 것이라고 생각하면
- [’A’, ‘B’, ‘C’]에서 100은 A가 있는 자리가 존재, B, C의 자리는 존재하지 않음
- 따라서 리스트가 [4, 6, 8]처럼 변경되어도 ‘자리’이기 때문에 100은 4를 나타냄

<<

- 1<<n 은 1을 기호 그대로 옆으로 민다라는 의미
- 만약에 n이 3이라면 1<<n은 1000이 됨
- [’ㄱ’, ‘ㄴ’, ‘ㄷ’, ‘ㄹ’] 의 경우에서는 1은 ‘ㄹ’을, 옆으로 3만큼 민다면 ‘ㄱ’을 의미.
- 따라서 for i in range(1<<n): # n개의 '자리'로 만들 수 있는 부분집합의 의미는
    - n = 0일때, 1자리 ‘1’(리스트 기준에서는 제일 우측, [::-1])를
    - n = 1일때, 2자리 ‘10’
    - n = 2일때, 3자리 ‘100’
    - n = k일때, k+1자리 ‘1과 k개의 0’
    - 즉, range를 쓴다는 말은 각 자리로 만들 수 있는 부분집합 전체를 만들겠다는 뜻

&는 집합 연산의 교집합과 같은 것

- if i & (1<<j): # i개의 자리수를 포함한 j(자리)은
- i자리를 포함한 부분집합이면을 의미

비트 마스크를 쓰는 이유

- 수행시간이 빠르다
- 코드가 짧다
- 메모리 사용량이 적다'''