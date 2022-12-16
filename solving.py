def change_number(number, n):
    if number == 0:
        return '0'

    rev_base = ''

    while number > 0:
        number, mod = divmod(number, n)
        # 11진법 이상일 시 A ~ F로 변경
        if mod > 10:
            mod = ['A', 'B', 'C', 'D', 'E', 'F'][mod % 11]
        rev_base += str(mod)

    return rev_base[::-1]


# 문제풀이 메인 함수
def solution(n, t, m, p):
    # 1) n진법으로해서 문자열로 쭉 이어 붙인다
    tmp_number = ''
    for num in range(t+1):
        tmp_number += change_number(num, n)

    # 2) 그 다음 튜브의 순서만 뽑아서 이어붙인다
    answer = ''
    cnt = 0
    for value in tmp_number:
        cnt += 1
        if cnt == p:
            answer += value
        if cnt == m:
            cnt = 0

    return answer