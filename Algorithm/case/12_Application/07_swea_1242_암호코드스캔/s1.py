# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15JEKKAM8CFAYD&categoryId=AV15JEKKAM8CFAYD&categoryType=CODE&problemTitle=1242&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&


'''
1. 암호코드의 흰색, 파란색의 넓이 비(ratio)와 숫자 값을 딕셔너리로 매핑한다.
2. 비(ratio)가 3:1:1:2 라고 하면 사실 이를 판별하는 건 뒤에 세 자리(1:1:2)만 있어도 가능하다.
3. 따라서 암호코드를 "왼쪽->오른쪽"이 아니라 "오른쪽->왼쪽" 방향으로 읽는 것이 편하다.
4. 먼저 배열에 있는 모든 16진수 숫자 하나 당, 길이가 4인 2진수로 변환한다. (ex. 4 -> 0100, F -> 1111)
5. 그러면 16진수 배열은 2진수 배열이 된다. 이제 각 줄 마다 오른쪽에서 부터 읽어간다.
6. 오른쪽에서 부터 읽는 경우, 처음에는 1의 구간을, 그 다음에는 0의 구간, 그 다음에는 다시 1 구간, 그 다음에는 0의 구간이 반복되는 규칙을 이용한다.
7. 마지막 0의 구간은 사용하지 않는 비(ratio)이므로 1을 만날 때 까지 계속 지나쳐간다. 1을 만났다는 것은 다른 새로운 암호코드가 있다는 것이다.
8. 그래서 각 1과 0의 개수를 세고, 비(ratio)를 계산한다. 이 때 1:1:2가 아니라 길이가 2배라서 2:2:4 인 경우가 있을 수도 있으니, (2, 2 ,4) 중 가장 작은 2로 모두 나누면 (1, 1, 2)를 만들 수 있다.
9. 아까 만들었던 딕셔너리를 통해 조회하면 해당 암호코드에 해당하는 10진수가 나온다.
10. 이러한 10진수가 8개가 될 때까지 반복하고, 8개가 되면 `(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드` 식을 이용하여 10의 배수라면 결과값에 합을 더한다.
11. 배열의 한 줄에 2개 이상의 암호코드가 있을 수 있으므로, 10진수 8개가 나왔더라도 다른 새로운 암호코드가 없을 때 까지 계속 왼쪽으로 이동한다.
12. 모든 배열을 탐색하고 결과 값을 출력한다.
13. (주의) 동일 암호 코드의 중복 계산을 방지해야 한다.
'''

import sys
sys.stdin = open('input.txt')

idx = [
    '0001101', '0011001',
    '0010011', '0111101',
    '0100011', '0110001',
    '0101111', '0111011',
    '0110111', '0001011']


def solution():
    # 16진법을 2진법으로 변환!

    # 끝점과 시작점 찾기!

    # 검산하기!
    return


for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 세로, M = 가로
    arr = list(set(input().rstrip() for _ in range(N)))  # 중복 제거후 리스트로 저장
    print(f'#{case} {solution()}')









# idx = [
#     '0001101', '0011001',
#     '0010011', '0111101',
#     '0100011', '0110001',
#     '0101111', '0111011',
#     '0110111', '0001011']
#
#
# def dfs(n):
#     # visited는 안써도 상관없음 어차피 한쪽방향
#     global password
#     password += data[n]
#     if n != M - 1 and data[n+1] != '0':
#         k = dfs(n+1)
#     else:
#         return n
#     return k
# #return n이 된 후 전껄로 돌아가서 이녀석을 끝까지 출력되게 넣어주려면 k처리 필요
#
#
# for case in range(1, 1 + int(input())):
#     # input 받고 사용할 변수 정의하기
#     N, M = map(int, input().split())  # N = 세로, M = 가로
#     password = ''
#     passwords = []
#     recent_visited = -1
#     유효 암호 저장하기
#     for _ in range(N):
#         data = input()
#         recent_visited = -1
#         # 0이 아닌 수가 나올때까지 찾아보기
#         for num in range(M):
#             if data[num] != '0' and recent_visited < num:  # dfs 반복 방문 방지
#                 recent_visited = dfs(num)  # dfs호출하는 순간 password 하나 완성
#                 if password not in passwords:
#                     passwords.append(password)  # 암호는 따로 password에 모아서 저장하기
#                 password = ''
#         print(passwords)
#     # 해독하기
#     # 16진수를 2진수로 변환
#     for pw in passwords:
#         int_num = int(pw, 16)  # 16진수 -> 10진수
#         bin_num = '0' * (4 * len(pw) - len(bin(int_num)[2:])) + bin(int_num)[2:]  # 10진수 -> 2진수, 지워진 0채워주기
#         # print(pw, bin_num, int(bin_num, 2), bin(int_num)[2:])   # 먼가 이상함
#         # print(bin_num, int(bin_num, 2), bin(int_num)[2:])
#         # 이상한 이유는 16진수랑 상관 없이 16진수로 만들어지는 2진수에서 56개의 배수를 뽑아서 설정해줘야 하기 떄문임!
#         # 결론은 다시 짜야함 아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ
#         # 난 잠 택
#
#
#
#         # 7개씩 끊어서 idx와 비교하여 원 숫자들 찾기
#         code_numbers = []
#         for n in range(0, len(bin_num), 7):
#             print(idx.index(bin_num[n:n+7]))
#             code_numbers.append(idx.index(bin_num[n:n+7]))
#         print(code_numbers)
#         # 검증
#         chk = 0
#         result = [0]
#         for i in range(8):
#             if i % 2:  # 짝수이면
#                 chk += code_numbers[i]
#             else:  # 홀수이면
#                 chk += code_numbers[i] * 3
#         if chk % 10 == 0:
#             result.append(code_numbers[7])
#     print(f'#{case} {sum(result)}')
#
