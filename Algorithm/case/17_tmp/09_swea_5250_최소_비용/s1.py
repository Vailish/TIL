# 5250. [파이썬 S/W 문제해결 구현] 7일차 - 최소 비용 D3
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 프림 한 번 써보자!
import sys
sys.stdin = open('input.txt')


for case in range(1, 1 + int(input())):
    N = int(input())  # N = 표의 가로길이
    field = [list(map(int, input().split())) for _ in range(N)]
    print()