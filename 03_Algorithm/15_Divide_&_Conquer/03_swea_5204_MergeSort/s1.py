# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys
sys.stdin = open('input.txt')


def merge(left, right):
    global cnt
    i, j = 0, 0
    merged_arr = []

    if left[-1] > right[-1]:
        cnt += 1

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged_arr.append(right[j])
            j += 1
        else:
            merged_arr.append(left[i])
            i += 1
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    middle = len(arr)//2
    left_arr = merge_sort(arr[:middle])
    right_arr = merge_sort(arr[middle:])

    return merge(left_arr, right_arr)


for case in range(1, 1 + int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{case}', result[N//2], cnt)
