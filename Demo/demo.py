from collections import deque

customer_name: str = input()
customers_queue: deque = deque()

while customer_name != 'End':

    if customer_name == 'Paid':
        while customers_queue:
            print(customers_queue.popleft())
    else:
        customers_queue.append(customer_name)

    customer_name: str = input()

print(f'{len(customers_queue)} people remaining.')