from collections import deque

names: deque[str] = deque(input().split(' '))
n: int = int(input())

# counter: int = 0
# while len(names) > 1:
#     counter += 1
#     kid: str = names.popleft()
#
#     if counter % n == 0:
#         print(f'Removed {kid}')
#     else:
#         names.append(kid)
#
# print(f'Last is {names[0]}')

while len(names) > 1:
    names.rotate(-(n - 1))
    print(f'Removed {names.popleft()}')

print(f'Last is {names.popleft()}')
