# 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수 D2
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 김성준
for case in range(1, int(input()) +1):  # case 번호 입력받기
    str1 = set(input())
    str2 = input()  # 조사할 문자열

    # 검사
    idx = []
    for word in str1:  # 각 문자를 넣어서, 빈도수를 리스트에 넣어줌!
        idx.append(str2.count(word))

        # idx = [str2.count(word) for word in str1]

    # 출력
    print(f'#{case} {max(idx)}')