from collections import deque

q = deque([1,2,3,4,5], 5)
q.append(5)         # 队尾入队
print(q.popleft())  # 队首出队