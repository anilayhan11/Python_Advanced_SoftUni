tokens: list[str] = input().split(' ')

# Solution 1 - Index-based iteration with a step
bakery = {}
for el in range(0, len(tokens), 2):
    food: str = tokens[el]
    count: int = int(tokens[el + 1])
    bakery[food] = int(count)
print(bakery)

# Solution 2 - Dict comprehension:
bakery = {tokens[el]: int(tokens[el + 1]) for el in range(0, len(tokens), 2)}
print(bakery)

# Solution 3 - zip with slicing:
bakery = dict(zip(tokens[::2], map(int, tokens[1::2])))
print(bakery)
