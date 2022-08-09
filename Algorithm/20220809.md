# SORT(정렬)
- bubble sort
- counting sort

### Bubble sort(거품 정렬)

```python
sample = [55, 7, 78, 12 ,42]

def bubble_sort(a) # 정렬할 list
  for i in range(len(a) -1, 0, -1): # 범위의 끝 위치 1)
      for j in range(0, i):
          if a[j] > a[j +1]:
              a[j], a[j+1] = a[j +1], a[j]
  return a

# 1) why? 한 바퀴 돌때 개수인데, 뒤로 갈수록 줄어드니까 거꾸로 하는 것이고, i를 앞으로 오게끔 하는 이유는 한 바퀴 돌때 제일 큰 수가 제일 뒤에 가기 때문. 이를 반복하면서 채우는 것

sample_2 = [("철수", 55), ("영희", 7), ("민수", 78), ("기영", 12), ("유라", 42)]

def bubble_sort(a)
  for i in range(len(a) -1, 0, -1):
      for j in range(0, i):
          if a[j][1] > a[j +1][1]: # <- 여기에 [1]만 추가해주면 됨
              a[j], a[j+1] = a[j +1], a[j]
  return a
```

---

### Counting sort
- 비교연산이 없어서 빠르다.
- 메모리를 더 많이 씀
  

```python
def counting_sort(original, k):
    counter = [0] * (k+1)

    # 1. counter에 original 원소의 빈도수 담기
    for i in original # original = [0, 4, 1, 3, 1, 2, 4, 1]
      counter[i] += 1

    # 2. 누적(counter 업데이트)
    for i in range(1, len(counter)): # counter = [1, 3, 1 ,1 ,2] -> [1, 4, 5, 6, 8] 누적값
      counter[i] += counter[i -1]
    
    # 3. result 생성
    result = [-1] * len(original)

    # 4. result에 정렬하기(counter를 참조)
    # Stable 안정정렬의 이유로 뒤에서부터 처리하는 것(들어온 순서대로 정렬하기 위해서 같은 1이 1이 아니기 떄문에)
    for i in range(len(original) -1, -1, -1): # [0, 1, 1, 1, 2, 3, 4, 4]
        counter[original[i]] -= 1 # 썼으니까 빼자
        result[counter[original[i]]] = original[i]
    
    return result

a = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(a, 5)) # [0, 1, 1, 1, 2, 3, 4, 4]

```