n: int = int(input())
cars: set = set()

for _ in range(n):
    direction, number = input().split(', ')

    if direction == 'IN' and number not in cars:
        cars.add(number)
    elif direction == 'OUT' and number in cars:
        cars.remove(number)

if cars:
    print(*cars, sep='\n')
else:
    print('Parking Lot is Empty')
