tokens: list[str] = input().lower().split()
my_dict: dict[str, int] = {}

for el in tokens:
    if el not in my_dict:
        my_dict[el] = 0
    my_dict[el] += 1

# for el in my_dict:
#     if my_dict[el] % 2 != 0:
#         print(el, end=' ')

for k, v in my_dict.items():
    if v % 2 != 0:
        print(k, end=' ')
