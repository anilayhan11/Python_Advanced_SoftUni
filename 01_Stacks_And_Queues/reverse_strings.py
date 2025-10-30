user_input: list[str] = list(input())
reversed_text: list[str] = []

for _ in range(len(user_input)):
    last_letter = user_input.pop()
    reversed_text.append(last_letter)

print(''.join(reversed_text))

# while user_input:
#     print(user_input.pop(), end='')