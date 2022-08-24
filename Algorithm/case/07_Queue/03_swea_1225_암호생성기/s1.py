# 1225. [S/W 문제해결 기본] 7일차 - 암호생성기 D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14uWl6AF0CFAYD&categoryId=AV14uWl6AF0CFAYD&categoryType=CODE&problemTitle=1225&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1&&&&&&&&&&&&&&&&&&


for _ in range(1, 11):
    case = int(input())
    queue = list(map(int, input().split()))
    
    stop = False  # while 문 탈출 조건

    while not stop:
        for num in range(1, 6):  # 1 ~ 5까지 바퀴마다 빼준다
            if queue[0] - num <= 0:  # 0 이하로 내려가면 0을 붙이고 탈출한다
                queue.pop(0)
                queue.append(0)
                stop = True
                break
            queue.append(queue.pop(0) - num)
    print(f'#{case}', *queue)
