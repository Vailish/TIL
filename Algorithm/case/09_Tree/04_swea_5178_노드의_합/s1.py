# 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# post_order(후위 순회)
def post_order(idx):
    global sum_node
    if idx <= N:
        left = post_order(idx * 2)  # 좌
        right = post_order(idx * 2 + 1)  # 우
        return left + right + value[idx]

    return 0

for case in range(1, 1 + int(input())):
    N, M, L = map(int, input().split())  # N : 노드의 개수, M : 리프노드의 개수, L : 출력 노드 번호(본인과 자손의 합)

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    value = [0] * (N + 1)  # 노드의 값
    sum_node = 0

    # input값 채우기
    for _ in range(M):
        idx, val = map(int, input().split())
        value[idx] = val
        ch1[idx] = 0
        ch2[idx] = 0

    print(post_order(idx))
