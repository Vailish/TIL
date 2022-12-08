# Bubble Sort

# 앞에서 한 자리씩 뒤로 가면서 해당 자리와 뒷 자리 수를 비교해서
# 작은 수를 앞으로 큰 수를 뒤로 바꾼 뒤 다음 자리로 넘어가서 똑같이 비교를 진행한다.
# 이때 끝자리 까지 비교를 하면 제일 뒤 자리가 결정이 된다.
# 다음번에는 똑같이 진행하되 이미 정해진 제일 끝자리를 제외하고 진행하는 방식으로 반복하게 되면 정렬이 완료된다.

# Bubble Sort

sample_1 = [55, 7, 78, 12 ,42]

def bubble_sort_A(a): # 정렬할 list
  for i in range(len(a) -1, 0, -1): # 범위의 끝 위치 1)
      for j in range(0, i):
          if a[j] > a[j +1]:
              a[j], a[j+1] = a[j +1], a[j]
  return a

# 1) why? 한 바퀴 돌때 개수인데, 뒤로 갈수록 줄어드니까 거꾸로 하는 것이고,
# i를 앞으로 오게끔 하는 이유는 한 바퀴 돌때 제일 큰 수가 제일 뒤에 가기 때문.
# 이를 반복하면서 채우는 것

sample_2 = [("철수", 55), ("영희", 7), ("민수", 78), ("기영", 12), ("유라", 42)]

def bubble_sort_B(a):
  for i in range(len(a) -1, 0, -1):
      for j in range(0, i):
          if a[j][1] > a[j +1][1]: # <- 여기에 [1]만 추가해주면 됨
              a[j], a[j+1] = a[j +1], a[j]
  return a

print(bubble_sort_A(sample_1))
print(bubble_sort_B(sample_2))

# practice
# sample = [55, 7, 78, 12 ,42]

# def bubble_sort(a):
#     for i in range(len(a) -1, 0, -1):
#         for j in range(0, i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
# print(bubble_sort(sample))
