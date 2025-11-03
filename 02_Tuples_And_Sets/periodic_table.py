n: int = int(input())
elements_set: set = set()

for _ in range(n):
    elements: list[str] = input().split()
    for el in elements:
        elements_set.add(el)

print(*elements_set, sep='\n')
