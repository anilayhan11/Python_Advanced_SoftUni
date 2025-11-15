# string: str = input()
# my_dict: dict[str, int] = {}
#
# for c in string:
#     if c != " ":
#         if c not in my_dict:
#             my_dict[c] = 0
#         my_dict[c] += 1
#
# for k, v in my_dict.items():
#     print(f"{k} -> {v}")

from collections import Counter

string = input()
my_dict = Counter(c for c in string if c != " ")

for k, v in my_dict.items():
    print(f"{k} -> {v}")
