# 5356. 의석이의 세로로 말해요 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVWgkP6sQ0DFAUO

for case in range(1, 1 + int(input())):

    # 배열 생성
    words = []
    for num in range(5):
        word = input()
        word = word + '!'*(15-len(word))
        words += [word]

    # 출력
    result = ''
    for i in range(15):
        for j in range(5):
            result += words[j][i]
    result = result.replace('!', '')
    print(f'#{case} {result}')
