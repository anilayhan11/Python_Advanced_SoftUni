n, m = (int(x) for x in input().split())
set_n, set_m = set(), set()

for _ in range(n):
    set_n.add(int(input()))

for _ in range(m):
    set_m.add(int(input()))

intersection_set: set = set_n.intersection(set_m)
print(*intersection_set, sep='\n')
