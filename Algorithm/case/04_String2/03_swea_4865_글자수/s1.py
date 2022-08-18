# 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

for case in range(1, int(input()) +1):
    str1 = list(input())
    str2 = input()

    # 중복제거
    str1 = list(set(str1))

    # 검사
    index = []
    for word in str1:
        index.append(str2.count(word))

    # 출력
    print(f'#{case} {max(index)}')
