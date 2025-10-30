user_input: str = input()
my_stack: list[int] = []

for i in range(0, len(user_input)):
    if user_input[i] == '(':
        my_stack.append(i)

    elif user_input[i] == ')':
        start_index: int = my_stack.pop()

        print(user_input[start_index:i + 1])
