#A deque (double-ended queue) allows efficient insertion and deletion from both the left and right ends.
from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
print(dq)

dq.appendleft(5)
print(dq)

dq.pop()     #element from right gets popped
print(dq)

dq.popleft()
print(dq)

dq = deque([1, 2, 3, 4])
dq.rotate(1)                 #right rotation
print(dq)

dq.rotate(-2)            #left rotation
print(dq)

dq = deque(maxlen=3)
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)
dq.append(4)  #will not exceed maxlen and if new element is added prev element is deleted from left
print(dq)
