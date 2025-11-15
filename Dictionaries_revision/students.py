command: str = input()
student_info: dict[str, list[int, str]] = {}

while ':' in command:
    tokens: list[str] = command.split(":")
    name: str = tokens[0]
    student_id: int = int(tokens[1])
    course: str = tokens[2].replace(" ", "_")

    student_info[name] = [student_id, course]

    command: str = input()

for student in student_info:
    if student_info[student][1] == command:
        print(f"{student} - {student_info[student][0]}")
