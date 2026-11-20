
# Add new records without deleting existing content
with open("students.txt", "a") as file:
    file.write("Ali - 85\n")
    file.write("Ahmed - 92\n")
    file.write("Sara - 78\n")

# Read all records
with open("students.txt", "r") as file:
    print(file.read())
