tokens: list[str] = input().split(' ')
bakery: dict[str:int] = {tokens[el]: int(tokens[el + 1]) for el in range(0, len(tokens), 2)}

queries: list[str] = input().split(' ')
for item in queries:
    if item in bakery:
        print(f'We have {bakery[item]} of {item} left')
    else:
        print(f"Sorry, we don't have {item}")
