# 1242. [S/W 문제해결 응용] 1일차 - 암호코드 스캔 D5
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15JEKKAM8CFAYD&categoryId=AV15JEKKAM8CFAYD&categoryType=CODE&problemTitle=1242&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&

# import sys
# sys.stdin = open('input.txt')


def solution():
    return



for case in range(1, 1 + int(input())):
    N, M = map(int, input().split())  # N = 세로, M = 가로
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
