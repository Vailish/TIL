# 핵심 개념 : 대소비교
# import sys
#
# sys.stdin = open('input.txt')

test_case = int(input())
for case in range(1, test_case+1):

    height = int(input()) # 필드
    box = list(map(int, input().split()))
    height_max = 0
    result = 0
    for i in range(height-1):
        for j in range(i+1, height):
            if box[i] > box[j]:
                height_max += 1
        if height_max > result:
            result = height_max
        height_max = 0
    print(f'#{case} {result}')