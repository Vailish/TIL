# min heap 구현하기
# root가 최소값이 오게끔


def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2


def deq():
    global last
    temp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c] < heap[c+1]:
            c += 1
        if heap[c] > heap[p]:
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2
        else:
            break
    return temp


heap = [0] * 100
last = 0
enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)
while last:
    print(deq())
