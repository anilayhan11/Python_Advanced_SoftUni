countries: list[str] = input().split(", ")
capitals: list[str] = input().split(", ")

my_dict: dict[str:str] = dict(zip(countries, capitals))

for k, v in my_dict.items():
    print(f"{k} -> {v}")

