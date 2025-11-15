letters: list[str] = input().split(", ")

ascii_dict: dict[str, str] = {letter: ord(letter) for letter in letters}
print(ascii_dict)
