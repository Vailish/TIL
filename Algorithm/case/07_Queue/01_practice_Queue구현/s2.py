class Queue:
    def __init__(self, n):
        self.size = n
        self.items = [None] * n
        self.front = -1  # 큐의 머리(앞쪽)
        self.rear = -1  # 큐의 꼬리(뒤쪽)
    
    # 1. 큐의 뒤쪽에 원소를 삽입하는 연산
    def enqueue(self, item):
        if self.is_full():
            # 여러가지 방식으로 대응 가능
            # 1) 큐의 크기를 확장하는 방식
            # 2) 이에 대한 예외처리를 해주는 방식
            print('큐가 가득차서 원소를 삽입할 수 없습니다.')
        else:
            self.rear += 1
            self.items[self.rear] = item
    
    # 2. 큐의 앞쪽에서 원소를 삭제하고 반환하는 연산
    def dequeue(self):
        if self.is_empty():
            print('큐가 비어서 원소를 삭제 및 반환할 수 없습니다.')
        else:
            self.front += 1
            return self.items[self.front]
    
    # 3. 큐가 공백상태인지 확인하는 연산
    def is_empty(self):
        return self.front == self.rear  # 머리와 꼬리가 같은 곳을 가리키면 공백상태

    # 4. 큐가 포화상태인지 확인하는 연산
    def is_full(self):
        return self.rear == self.size -1  # 꼬리가 큐의 마지막을 가리키면 포화상태
    
    # 5. 큐의 앞쪽에서 원소를 삭제 없이 반환하는 연산
    def q_peek(self):
        if self.is_empty():
            print('큐가 비어서 원소를 반환할 수 없습니다.')
        else:
            return self.items[self.front]

queue = Queue(3)  # 사이즈가 3인 큐 생성

# 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
print(queue.items)  # 삽입 전 큐의 모습
for num in range(1, 4):
    queue.enqueue(num)  # 나열해도 됨
print(queue.items)  # 삽입 후 큐의 모습

# 큐에서 세 개의 데이터 차례로 꺼내서 출력
for i in range(3):
    print(queue.dequeue())  # 나열해도 됨

# 이 방법은 번거롭고, 리스트를 활용하면 간단히 사용가능하다.