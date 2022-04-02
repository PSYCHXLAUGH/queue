from random import randint
from collections import deque

queue = deque()

lenght = randint(5, 10)

for x in range(lenght):
    print(queue)
    queue.append(randint(5, 10))

print("*" * lenght)

for x in range(lenght):
    print(queue)
    queue.popleft()

