from collections import deque

water_amount: int = int(input())
names_queue: deque[str] = deque()

name: str = input()
while name != 'Start':
    names_queue.append(name)

    name: str = input()

print(names_queue)
