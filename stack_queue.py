#create an empty stack
from collections import deque
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

stack.pop()
print(stack)


#queue
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)
