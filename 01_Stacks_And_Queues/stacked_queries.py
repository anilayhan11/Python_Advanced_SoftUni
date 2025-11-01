my_stack: list[int] = []
n: int = int(input())

for _ in range(n):
    query: list[int] = [int(x) for x in input().split(' ')]
    command: int = query[0]

    if command == 1:
        number = query[1]
        my_stack.append(number)
    elif command == 2:
        if my_stack:
            my_stack.pop()
    elif command == 3:
        if my_stack:
            print(max(my_stack))
    elif command == 4:
        if my_stack:
            print(min(my_stack))

my_stack.reverse()
print(*my_stack, sep=", ")  # -> Modifies the existing list

# print(*my_stack[::-1], sep=', ') -> creates a new list
