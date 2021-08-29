class Queue:
    def __init__(self, maxsize = 100) -> None:
        self.queue = [0 for _ in range(maxsize)]
        self.size = maxsize
        self.rear = 0   # 队尾初始位置
        self.front = 0  # 队首初始位置
    
    def push(self, element):
        if not self.is_filled():
            self.rear = ( self.rear + 1 ) % self.size # rear指针往后挪一个位置
            self.queue[self.rear] = element           # 加入元素到rear现在的位置
        else:
            raise IndexError("queue is filled!")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("queue is empty!")

    def is_empty(self):
        return self.front == self.rear

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

queue = Queue(5)
for i in range(5):
    queue.push(i)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())