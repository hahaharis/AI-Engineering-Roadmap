
import json

# 1. Write data to a text file
with open("notes.txt", "w") as file:
    file.write("I am learning Python file handling.\n")
    file.write("Day 3 - AI Engineering Roadmap.")

# 2. Read the text file
with open("notes.txt", "r") as file:
    content = file.read()

print("Text File Content:")
print(content)

# 3. Store data in JSON
student = {
    "name": "Haris",
    "course": "AI Engineering",
    "day": 3
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# 4. Read JSON data
with open("student.json", "r") as file:
    data = json.load(file)

print("\nJSON Data:")
print(data)
