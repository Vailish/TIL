# bubble sort 직접 해보기
sample = [55, 7, 78, 12 ,42]

def bubble_sort(a):
    for i in range(len(a) -1, 0, -1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


print(bubble_sort(sample))


# sample = [55, 7, 78, 12 ,42]

# def bubble_sort(a) # 정렬할 list
#   for i in range(len(a) -1, 0, -1): # 범위의 끝 위치 1)
#       for j in range(0, i):
#           if a[j] > a[j +1]:
#               a[j], a[j+1] = a[j +1], a[j]
#   return a