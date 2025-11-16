nums_stack: list[str] = []

map_functions = {
    1: lambda x: nums_stack.append(x[1]),
    2: lambda x: nums_stack.pop() if nums_stack else None,
    3: lambda x: print(max(nums_stack)) if nums_stack else None,
    4: lambda x: print(min(nums_stack)) if nums_stack else None,
}

n = int(input())
for _ in range(n):
    numbers_data: list[int] = [int(x) for x in input().split()]
    command = numbers_data[0]
    map_functions[command](numbers_data)

nums_stack.reverse()
print(*nums_stack, sep=", ")
