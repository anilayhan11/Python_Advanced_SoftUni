n: int = int(input())
student_data: dict = {}

for _ in range(n):
    name, grade = input().split()
    grade = float(grade)

    if name not in student_data:
        student_data[name] = []
    student_data[name].append(grade)

for name, grades in student_data.items():
    avg_grade = sum(grades) / len(grades)
    grades_str = ' '.join(f"{x:.2f}" for x in grades)
    print(f"{name} -> {grades_str} (avg: {avg_grade:.2f})")
