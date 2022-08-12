for turn in range(1, 11):
    location = int(input()) #건물 개수
    data = list(map(int, input().split())) # 건물 높이
    fine_views = 0 
    for x in range(2, location-2):
        if data[x] > data[x-1] and data[x] > data[x-2] and data[x] > data[x+1] and data[x] > data[x+2]:
            fine_views += data[x] - max([data[x-1], data[x-2], data[x+1], data[x+2]])
    print(f'#{turn} {fine_views}')