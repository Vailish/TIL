import sys
sys.stdin = open('input.txt')
# 3분할 -> 최대 - 최소

# 세로로 나누고
# 가로로 나누고
# 각 넓이를 계산해서
# 최대값 - 최소값 해서 최소가 되는 값을 출력한다.

def solution():
    result = []  # 결과값 모음
    # 세로로 나누기
    for j in range(1, N):
        # 세로(box_3) 넓이 구하기
        area_box3 = 0
        for a in range(j, N):
            for b in range(N):
                area_box3 += arrs[b][a]

        # 가로로 나누기
        for i in range(1, N):
            # 위(box_1), 아래(box_2) 넓이 구하기
            area_box1 = 0
            area_box2 = 0
            for a in range(0, j):
                # box_1
                for b in range(0, i):
                    area_box1 += arrs[b][a]
                # box_2
                for c in range(i, N):
                    area_box2 += arrs[c][a]

            # 최소값과 최대값 구해서 값 구하기
            max_box = max(area_box1, area_box2, area_box3)
            min_box = min(area_box1, area_box2, area_box3)
            result.append(max_box - min_box)
    return min(result)


for case in range(1, 1 + int(input())):
    N = int(input())
    arrs = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{case}', solution())
