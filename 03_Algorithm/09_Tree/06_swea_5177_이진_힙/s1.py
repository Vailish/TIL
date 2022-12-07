# 5177. [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')


def heap_push(n):
    heap.append(n)
    c = len(heap) - 1
    p = c // 2

    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2


for case in range(1, 1 + int(input())):
    N = int(input())  # N = 정점의 수
    arr = list(map(int, input().split()))

    heap = [0]
    for n in arr:
        heap_push(n)

    result = []
    while N > 0:
        N //= 2
        result.append(heap[N])

    print(f'#{case}', sum(result))
