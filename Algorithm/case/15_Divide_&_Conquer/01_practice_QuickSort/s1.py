import sys
sys.stdin = open('input.txt')

def partition(A[], l, r):
    p = A[l]
    i = l, j = r
    while i <= j:
        while i <= and A[i] <=


def qsort(A[], l, r):
    if l < r:
        s  = partition(a, l, r)
        qsort(A[], l, s - 1)
        qsort(A[], s + 1, r)

