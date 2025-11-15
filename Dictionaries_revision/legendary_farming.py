is_obtained = False
elements: dict[str, int] = {'shards': 0, 'fragments': 0, 'motes': 0}
junk: dict[str, int] = {}

while True:
    tokens: list[str] = input().lower().split()

    for i in range(0, len(tokens) - 1, 2):
        material: str = tokens[i + 1]
        count: int = int(tokens[i])

        if material in elements:
            elements[material] += count

        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += count

        if material in elements and elements[material] >= 250:
            elements[material] -= 250
            is_obtained = True

            if material == "shards":
                print("Shadowmourne obtained!")
                break
            if material == "fragments":
                print("Valanyr obtained!")
                break
            if material == "motes":
                print("Dragonwrath obtained!")
                break
        if is_obtained:
            break
    if is_obtained:
        break

for k, v in elements.items():
    print(f"{k}: {v}", end='\n')

for k, v in junk.items():
    print(f"{k}: {v}", end='\n')
