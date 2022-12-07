T = int(input())
for case in range(1, T + 1):
    N, K = map(int, input().split())
    A = range(1, 13)  # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = len(A)
    lst = []
    count = 0
    
    #2진수.format(i, 'b')로 바꿔줘도 되지만, len으로 걸러낼 수도 있음
    for i in range(1 << n): # 모든 부분집합을 lst에 담기 
        sub_set = []
        for j in range(n):
            if i & (1 << j):
                sub_set += [A[j]]
        if len(sub_set) == N and sum(sub_set) == K: # 조건에 맞는 부분집합 세기
            count  += 1
    print(f'#{case} {count}')

    #결국에는 지금 모든 부분집합을 다 담아서, 마지막에 한 번 더 세고 있지만
    #어차피 길이가 n이고 합이 k인 부분집합의 “개수”만 세는 거라면 lst에 다 담지않고
    #for문 안에서 즉석으로 세면서 count만 올려주는 방법도 고려해 볼만 합니다
    # -> s1을 수정하여 만들었습니다.
    # 그냥 if i & (1 << j) 이건 모든 부분 집합 전체다 이렇게 생각하면 끝!