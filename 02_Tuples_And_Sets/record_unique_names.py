n: int = int(input())
names: set = set()

for _ in range(n):
    names.add(input())

print(*names, sep='\n')
