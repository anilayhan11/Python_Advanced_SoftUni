command: str = input()
stats: dict[str, int] = {}

while command != 'statistics':
    tokens: list[str, int] = command.split(': ')
    item: str = tokens[0]
    count: int = int(tokens[1])
    if item not in stats:
        stats[item] = 0
    stats[item] += count

    command: str = input()

print("Products in stock:")
for k, v in stats.items():
    print(f"- {k}: {v}")
print(f"Total Products: {len(stats.keys())}")
print(f"Total Quantity: {sum(stats.values())}")
