#A deque (double-ended queue) allows efficient insertion and deletion from both the left and right ends.
from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
print(dq)

dq.appendleft(5)
print(dq)

dq.pop()
print(dq)

dq.popleft()
print(dq)

dq = deque([1, 2, 3, 4])
dq.rotate(1)
print(dq)

dq.rotate(-2)
print(dq)

dq = deque(maxlen=3)
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)
dq.append(4)
print(dq)
