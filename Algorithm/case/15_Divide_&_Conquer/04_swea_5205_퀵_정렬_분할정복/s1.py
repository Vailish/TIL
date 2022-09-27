# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')


def partition(arr, left, right):
    pivot = arr[left]
    i, j = left, right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j


def quick_sort(arr, left, right):
    if left < right:
        middle = partition(arr, left, right)
        quick_sort(arr, left, middle-1)
        quick_sort(arr, middle+1, right)


for case in range(1, 1 + int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)
    print(f'#{case}', arr[N//2])
