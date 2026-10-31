students = [
    {"name": "Anitas", "marks": 95},
    {"name": "Riya", "marks": 88},
    {"name": "Rahul", "marks": 106}
]


def add_student(student_list, name, marks):
    student_list.append({"name": name, "marks": marks})


def find_topper(student_list):
    topper = student_list[0]

    for student in student_list:
        if student["marks"] > topper["marks"]:
            topper = student

    return topper


def calculate_average(student_list):
    total = 0

    for student in student_list:
        total += student["marks"]

    return total / len(student_list)


def show_students(student_list):
    print("All Students:")

    for student in student_list:
        print(f"{student['name']} : {student['marks']}")


add_student(students, "Jana", 90)

show_students(students)

topper = find_topper(students)
average = calculate_average(students)

print(f"\nTopper: {topper['name']} : {topper['marks']}")
print(f"Average: {average:.2f}")