# 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

for case in range(1, 1 + int(input())):
    str1 = input()
    str2 = input()

    # for num in range(len(str2)-len(str1)):
    #     if str2[:len(str2)-1]

    if str1 in str2:
        print(f'#{case} {str2.count(str1)}')
    else:
        print(f'#{case} 0')
