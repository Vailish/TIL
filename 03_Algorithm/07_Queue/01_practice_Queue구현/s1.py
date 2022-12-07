queue = []  # 큐 역할을 할 빈 리스트

# 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
print(queue)  # 삽입 전 큐의 모습
for i in range(1, 4):
    queue.append(i)
print(queue)  # 삽입 후 큐의 모습

# 큐에서 세 개의 데이터를 차례로 꺼내어 출력
# 선입선출(FIFO)를 위해 pop 메서드의 인자로 인덱스 0을 줌
for i in range(3):
    print(queue.pop(0))