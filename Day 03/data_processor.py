
import csv
import json
from pathlib import Path

input_file = Path("students.csv")
output_file = Path("class_report.json")

try:
    # Read CSV data
    students = []

    with input_file.open("r", newline="") as file:
        reader = csv.DictReader(file)
        print("CSV columns detected:", reader.fieldnames)

        for row in reader:
            row["marks"] = float(row["marks"])
            students.append(row)

    # Process data
    total_students = len(students)
    average_marks = sum(s["marks"] for s in students) / total_students
    highest_student = max(students, key=lambda s: s["marks"])
    passed_students = [
        s for s in students if s["marks"] >= 50
    ]

    # Generate report
    report = {
        "total_students": total_students,
        "average_marks": round(average_marks, 2),
        "highest_scorer": highest_student,
        "passed_students": len(passed_students),
        "failed_students": total_students - len(passed_students),
        "student_records": students
    }

    # Export JSON
    with output_file.open("w") as file:
        json.dump(report, file, indent=4)

    print("Report generated successfully!")
    print(json.dumps(report, indent=4))

except FileNotFoundError:
    print("Error: students.csv was not found.")

except (ValueError, ZeroDivisionError) as error:
    print("Data processing error:", error)

except Exception as error:
    print("Unexpected error:", error)
