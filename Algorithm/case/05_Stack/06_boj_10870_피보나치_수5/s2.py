# 2. 피보나치 재귀 + Memoization 풀이
# 0 1 1 2 3 5 8 13 ...


def fibo(n):
    if len(memo) <= n:
        memo.append(fibo(n - 1) + fibo(n - 2))
    return memo[n]


memo = [0, 1]

print(fibo(5))
# print(fibo(40)) # 단순 재귀만 사용했을 때보다 더 빠르게 결과가 출력됨을 확인
