# 순열을 이용해서 풀기, 완전탐색
def baby_jin(i, k):
    global ans

    if i == k:
        triplet = 0
        run = 0
        if card[0] == card[1] and card[1] == card[2]:
            triplet += 1
        if card[3] == card[4] and card[4] == card[5]:
            triplet += 1
        if card[0] +1 == card[1] and card[1] +1 == card[2]:
            run += 1
        if card[3] +1 == card[4] and card[4] +1 == card[5]:
            run += 1
        if triplet + run >= 2:
            ans = 'True'

    else:
        for j in range(i, k):
            card[i], card[j] = card[j], card[i]
            baby_jin(i+1, k)
            card[i], card[j] = card[j], card[i]


for case in range(1, 1 + int(input())):
    card = list(map(int, input()))
    ans = 'False'
    baby_jin(0, 6)
    print(f'#{case} {ans}')
