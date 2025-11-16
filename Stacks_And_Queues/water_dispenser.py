from collections import deque

liters_total: int = int(input())
people_queue: deque[str] = deque()

person: str = input()
while person != 'Start':
    people_queue.append(person)
    person: str = input()

command: str = input()
while command != 'End':
    data: list[str] = command.split()

    if len(data) == 2:
        liters_refill: int = int(data[1])
        liters_total += int(liters_refill)

    else:
        liters_person = int(data[0])
        person: str = people_queue.popleft()

        if int(liters_person) <= liters_total:
            liters_total -= int(liters_person)

            print(f'{person} got water')

        else:
            print(f'{person} must wait')

    command: str = input()

print(f'{liters_total} liters left')


