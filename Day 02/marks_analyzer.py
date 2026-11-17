

students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ahmed", "marks": 48},
    {"name": "Usman", "marks": 67},
    {"name": "Ayesha", "marks": 35}
]

def get_top_students(records):
    print("\nTop Students:")

    for student in records:
        if student["marks"] >= 80:
            print(student["name"], student["marks"])


def find_highest_scorer(records):
    highest_student = records[0]

    for student in records:
        if student["marks"] > highest_student["marks"]:
            highest_student = student

    print("\nHighest Scorer:")
    print(
        f'{highest_student["name"]} '
        f'with {highest_student["marks"]} marks'
    )

def count_results(records):
    passed = 0
    failed = 0

    for student in records:
        if student["marks"] >= 50:
            passed += 1
        else:
            failed += 1

    print("\nClass Summary:")
    print("Total Students:", len(records))
    print("Passed:", passed)
    print("Failed:", failed)


def assign_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def sort_students(records):
    sorted_students = sorted(
        records,
        key=lambda student: student["marks"],
        reverse=True
    )

    print("\nStudents Ranked by Marks:")

    for position, student in enumerate(sorted_students, start=1):
        print(
            position,
            student["name"],
            "-",
            student["marks"]
        )

def display_grades(records):
    print("\nStudent Grades:")

    for student in records:
        grade = assign_grade(student["marks"])
        print(student["name"], ":", grade)

def search_student(records, search_name):
    for student in records:
        if student["name"].lower() == search_name.lower():
            print("\nStudent Found:")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Grade:", assign_grade(student["marks"]))
            return

    print("\nStudent not found.")



def add_student(records, name, marks):
    if not validate_marks(marks):
        return

    new_student = {
        "name": name,
        "marks": marks
    }

    records.append(new_student)
    print(f"\n{name} has been added successfully.")



def validate_marks(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        return False

    return True



def check_result(marks):
    if marks >= 50:
        return "Pass"
    return "Fail"


def calculate_average(records):
    total = 0

    for student in records:
        total += student["marks"]

    return total / len(records)


def display_results(records):
    for student in records:
        result = check_result(student["marks"])

        print(
            f'{student["name"]}: '
            f'{student["marks"]} marks — {result}'
        )

import json


def save_students(records):
    with open("students.json", "w") as file:
        json.dump(records, file, indent=4)

    print("\nStudent records saved to students.json")


def load_students():
    try:
        with open("students.json", "r") as file:
            records = json.load(file)

        print("\nStudent records loaded successfully!")
        return records

    except FileNotFoundError:
        print("Student file not found.")
        return []

    
def generate_report(records):
    if not records:
        print("No student records available.")
        return

    total_students = len(records)
    average = calculate_average(records)

    passed = sum(
        1 for student in records
        if student["marks"] >= 50
    )

    failed = total_students - passed

    report = {
        "total_students": total_students,
        "average_marks": round(average, 2),
        "passed": passed,
        "failed": failed,
        "highest_scorer": max(
            records,
            key=lambda student: student["marks"]
        )["name"]
    }

    with open("class_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\nClass report generated successfully!")


display_results(students)


average = calculate_average(students)
print(f"\nClass Average: {average:.2f}")
get_top_students(students)
find_highest_scorer(students)
count_results(students)
display_grades(students)
sort_students(students)
search_student(students, "Ahmed")
add_student(students, "Haris", 88)
display_results(students)
add_student(students, "Haris", 88)
add_student(students, "Test", 150)
save_students(students)
loaded_students = load_students()
print("Loaded students:", len(loaded_students))
generate_report(students)


def show_menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Display all students")
        print("2. Show class average")
        print("3. Show top students")
        print("4. Find highest scorer")
        print("5. Search student")
        print("6. Add student")
        print("7. Save records")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            display_results(students)

        elif choice == "2":
            print("Class Average:", calculate_average(students))

        elif choice == "3":
            get_top_students(students)

        elif choice == "4":
            find_highest_scorer(students)

        elif choice == "5":
            name = input("Enter student name: ")
            search_student(students, name)

        elif choice == "6":
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            add_student(students, name, marks)

        elif choice == "7":
            save_students(students)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


show_menu()
