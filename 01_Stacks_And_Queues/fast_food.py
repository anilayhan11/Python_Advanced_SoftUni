from collections import deque

food: int = int(input())
orders: deque[int] = deque(int(x) for x in input().split())

print(max(orders))

while orders and orders[0] <= food:
    food -= orders.popleft()

if orders:
    print(f'Orders left:', *orders)
else:
    print('Orders complete')


